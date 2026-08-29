---
name: extract-illustrations
description: Extract frames from video around a timestamp, verify content matches expected description, crop browser chrome, and save as illustration. Use when creating article illustrations from video content.
---

# Extract Illustration from Video

Extract keyframes around a timestamp, verify each one, select the best match, crop if needed, and save as JPEG. Falls back to step-based extraction if keyframes don't yield matches.

## Required Arguments

When using this skill, you need:
- `video` - Path to video file
- `timestamp` - Timestamp in MM:SS or HH:MM:SS format (estimated)
- `name` - Illustration name (for filename: name.jpg)
- `description` - What content we're looking for (for verification)
- `context` - Article text around the illustration

## Process

### 1. Try keyframes first (natural scene changes)

Extract I-frames from ±10 seconds around the target timestamp:

```bash
mkdir -p "_temp/frames/$name" _temp/illustrations

cd "$(dirname "$video")" && ffmpeg -ss $timestamp -i "$(basename "$video")" \
  -ss -00:00:10 -t 00:00:20 \
  -vf "select=eq(pict_type\,I)" -vsync 0 \
  "C:/Users/alexe/git/notes/_temp/frames/$name/keyframe_%{pts:hms}.png" -y 2>&1 | tail -3
```

Check if keyframes were extracted:
```bash
ls "_temp/frames/$name/" | wc -l
```

### 1b. Remove duplicate keyframes by file size

```bash
python .claude/skills/extract-illustrations/scripts/dedup_by_size.py "_temp/frames/$name"
```

### 2. Verify keyframes (content match)

Starting with the keyframe closest to the target timestamp, use `analyze_image`:

```
We expect: $description
Context: $context

What does this image actually show? Does it match what we expect?
```

### 3. Select best match

- **If frame matches**: Proceed to step 4.
- **If frame doesn't match**: Check the next closest keyframe.
- **If NO keyframes match after checking all candidates**: Go to step 3b (fallback).

### 3b. Fallback: Extract frames at 1-second intervals

If keyframes didn't yield a match, extract specific frames:

```bash
cd "$(dirname "$video")" && for offset in -5 -4 -3 -2 -1 0 1 2 3 4 5; do
  ffmpeg -ss $timestamp -i "$(basename "$video")" -ss "00:00:$offset" -vframes 1 \
    "C:/Users/alexe/git/notes/_temp/frames/$name/frame_${offset}.png" -y 2>&1 | tail -1
done
```

Then verify each frame starting from offset 0.

### 4. Remove visually similar frames (optional)

If many frames remain, use the deduplication script:

```bash
python .claude/skills/extract-illustrations/scripts/dedup_frames.py "_temp/frames/$name"
```

### 5. Assess cropping needs

Now that a matching frame is found, use `analyze_image` to determine crop dimensions:

```
Please assess cropping needs for this image:
1. Is there browser chrome at the top? If yes, exactly how many pixels should be removed?
2. Are there sidebars on left/right edges? If yes, exactly how many pixels to crop from each side?
3. What are the original image dimensions?

Provide the final crop dimensions in the format: widthxheight+x+y
```

### 6. Crop and save

Use the dimensions from analyze_image:

```bash
# Example: analyze_image reports crop dimensions "1180x630+50+90"
convert "_temp/frames/$name/best_frame.png" -crop {width}x{height}+{x}+{y} +repage "_temp/illustrations/$name.jpg"
```

### 7. Cleanup

```bash
rm -rf "_temp/frames/$name"
```

## Output

Saved to: `_temp/illustrations/$name.jpg`

## Selection Guidelines

| Content Type | What to Look For |
|--------------|------------------|
| **UI Screenshots** | No loading spinners, fully populated data, clear labels |
| **Diagrams** | Complete diagram, no cutting off edges, clear text |
| **Code/Terminal** | Complete commands visible, no partial lines |
| **People** | Faces visible, not mid-blink, natural expression |
| **Data Visualizations** | Axes/labels visible, clear data points |
| **Websites/Pages** | Fully loaded, no broken images, header visible |

## Example

```
video=C:/Users/alexe/Downloads/video.mp4
timestamp=00:24:44
name=leaderboard
description="leaderboard showing student points for homework"
context="The Leaderboard gamified element where students earn points"
```

## Scripts

- `scripts/dedup_frames.py` - Remove visually similar frames based on pixel difference
