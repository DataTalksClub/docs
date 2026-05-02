"""
Extract question threads from a Slack channel dump.

Expects the dump to be laid out as one JSON file per day under
  <slack_dir>/<channel>/YYYY-MM-DD.json
Each JSON file is a list of message objects in Slack export format.

For each top-level message that looks like a question, collect:
- date, user, original question text
- text of all replies (joined as the answer)

Outputs (in <out_dir>):
- <channel>.threads.jsonl  - one JSON object per question thread
- <channel>.threads.txt    - human-readable concatenation for skimming/grep

Usage:
  python scripts/extract_slack_questions.py <channel> [--slack-dir DIR] [--out-dir DIR]

Example:
  python scripts/extract_slack_questions.py course-data-engineering \
    --slack-dir _temp/slack --out-dir _temp/slack
"""

import argparse
import glob
import json
import os
import re


def is_question(text: str) -> bool:
    if not text:
        return False
    if "?" in text:
        return True
    lowered = text.lower().strip()
    starters = (
        "how ", "what ", "where ", "when ", "why ", "which ", "who ",
        "can i", "can someone", "can anyone", "could ", "should i",
        "is it", "are there", "do i", "does anyone", "anyone know",
        "help", "i'm getting", "im getting", "i am getting",
        "i'm stuck", "im stuck", "i am stuck",
    )
    return any(lowered.startswith(s) for s in starters)


def clean_text(text: str) -> str:
    if not text:
        return ""
    # Remove user mentions like <@U01234>
    text = re.sub(r"<@[UW][A-Z0-9]+>", "@user", text)
    # Replace channel refs <#C123|name> with #name
    text = re.sub(r"<#C[A-Z0-9]+\|([^>]+)>", r"#\1", text)
    # Replace plain channel refs <#C123>
    text = re.sub(r"<#C[A-Z0-9]+>", "#channel", text)
    # Replace <url|label> with label (url)
    text = re.sub(r"<(https?://[^|>]+)\|([^>]+)>", r"\2 (\1)", text)
    # Replace plain <url>
    text = re.sub(r"<(https?://[^>]+)>", r"\1", text)
    return text.strip()


def collect_threads(channel_dir: str):
    """Walk all daily JSON files and group messages into threads keyed by thread_ts."""
    threads = {}  # thread_ts -> {root, replies, date}
    files = sorted(glob.glob(os.path.join(channel_dir, "*.json")))
    for fname in files:
        try:
            with open(fname, encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            continue
        date_str = os.path.basename(fname)[:10]
        for msg in data:
            if msg.get("type") != "message":
                continue
            if msg.get("subtype") in (
                "channel_join", "channel_leave", "bot_message", "channel_topic",
            ):
                continue
            ts = msg.get("ts")
            tts = msg.get("thread_ts") or ts
            if tts not in threads:
                threads[tts] = {"root": None, "replies": [], "date": date_str}
            if ts == tts:
                threads[tts]["root"] = msg
                threads[tts]["date"] = date_str
            else:
                threads[tts]["replies"].append(msg)

    for t in threads.values():
        t["replies"].sort(key=lambda m: float(m.get("ts", "0")))
    return threads, len(files)


def write_outputs(threads, out_dir: str, channel: str, min_question_len: int = 15):
    jsonl_path = os.path.join(out_dir, f"{channel}.threads.jsonl")
    txt_path = os.path.join(out_dir, f"{channel}.threads.txt")
    kept = 0
    with open(jsonl_path, "w", encoding="utf-8") as out_jsonl, \
         open(txt_path, "w", encoding="utf-8") as out_txt:
        # Sort by date for stable, browsable output
        for tts, t in sorted(threads.items(), key=lambda kv: kv[1]["date"]):
            root = t["root"]
            if not root:
                continue
            text = clean_text(root.get("text", ""))
            if not is_question(text):
                continue
            if len(text) < min_question_len:
                continue

            replies_text = []
            for r in t["replies"]:
                rt = clean_text(r.get("text", ""))
                if rt:
                    replies_text.append(rt)

            profile = root.get("user_profile") or {}
            user = (
                profile.get("real_name")
                or profile.get("display_name")
                or root.get("user", "?")
            )
            record = {
                "date": t["date"],
                "thread_ts": tts,
                "user": user,
                "question": text,
                "n_replies": len(replies_text),
                "answer": "\n---\n".join(replies_text),
            }
            out_jsonl.write(json.dumps(record, ensure_ascii=False) + "\n")

            out_txt.write(
                f"### [{record['date']}] {record['user']} ({record['n_replies']} replies)\n"
            )
            out_txt.write("Q: " + text.replace("\n", "\n   ") + "\n")
            if replies_text:
                out_txt.write("A:\n")
                for i, r in enumerate(replies_text, 1):
                    out_txt.write(f"  [{i}] " + r.replace("\n", "\n      ") + "\n")
            out_txt.write("\n")
            kept += 1
    return jsonl_path, txt_path, kept


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("channel", help="Channel name (matches subdirectory name)")
    parser.add_argument(
        "--slack-dir",
        default=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_temp", "slack"),
        help="Directory containing per-channel subdirectories (default: _temp/slack)",
    )
    parser.add_argument(
        "--out-dir",
        default=None,
        help="Output directory (default: same as --slack-dir)",
    )
    parser.add_argument(
        "--min-question-len",
        type=int,
        default=15,
        help="Skip questions shorter than this many characters (default: 15)",
    )
    args = parser.parse_args()

    out_dir = args.out_dir or args.slack_dir
    channel_dir = os.path.join(args.slack_dir, args.channel)
    if not os.path.isdir(channel_dir):
        raise SystemExit(f"Channel directory not found: {channel_dir}")
    os.makedirs(out_dir, exist_ok=True)

    threads, n_files = collect_threads(channel_dir)
    jsonl_path, txt_path, kept = write_outputs(
        threads, out_dir, args.channel, args.min_question_len
    )

    print(f"Channel: {args.channel}")
    print(f"Daily files scanned: {n_files}")
    print(f"Total threads: {len(threads)}")
    print(f"Question threads kept: {kept}")
    print(f"Output: {jsonl_path}")
    print(f"Output: {txt_path}")


if __name__ == "__main__":
    main()
