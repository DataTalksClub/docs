"""
Bucket extracted Slack question threads into theme buckets via keyword
patterns, count frequency, and emit a draft markdown for review.

Input: a .threads.jsonl produced by extract_slack_questions.py
Output: a markdown file with one section per theme, sorted by frequency.

Themes are channel-agnostic by default but tuned for DE Zoomcamp-style
course channels. Override THEMES below or pass --themes to use a JSON file.

Usage:
  python scripts/bucket_slack_questions.py <input.jsonl> <output.md> \\
      [--year 2025 2026] [--samples 5]
"""

import argparse
import json
import re
from collections import defaultdict


# Each theme: list of regex patterns (case-insensitive). A thread matches
# the theme if ANY pattern matches the question text.
THEMES = {
    "Course start / cohort schedule": [
        r"\bwhen (does|is|will|do)\b.*\b(course|cohort|zoomcamp|class|camp|bootcamp|module)\b.*\b(start|begin)",
        r"\bwhen.*\b(start|begin).*\b(course|cohort|zoomcamp|class|camp|bootcamp)",
        r"\bcourse.*start.*date\b",
        r"\bofficial.*start.*date\b",
        r"\bstart.?date\b",
        r"\bnext cohort\b",
        r"\bwhen.*next.*cohort\b",
        r"\bschedule.*course\b",
        r"\bschedule.*(camp|cohort|zoomcamp)\b",
        r"\b(course|cohort|class|camp).*starting\b",
        r"\bstarting.*\b(today|tomorrow|this week|next week|on the)",
        r"\bhas.*\b(course|class|cohort|zoomcamp|camp).*\bstart(ed)?\b",
        r"\b(course|cohort).*already.*start",
    ],
    "Joining mid-cohort / late start / what did I miss": [
        r"\bjust joined\b",
        r"\bjoin.*late\b",
        r"\blate.*join",
        r"\bcatch up\b",
        r"\bcatching up\b",
        r"\bstart.*late\b",
        r"\bbehind.*schedule\b",
        r"\bis it too late\b",
        r"\bjust arrived\b",
        r"\bwhat.*did i miss\b",
        r"\bcan i still (join|participate|enroll)\b",
        r"\bstill.*time.*join\b",
        r"\bnot too late\b",
    ],
    "How to join / register / enroll": [
        r"\bhow.*\b(do i|can i|to)\b.*\b(join|register|enroll|sign up|signup|apply)\b.*(course|cohort|zoomcamp|camp|class)",
        r"\b(register|enroll|sign up|signup).*\b(course|cohort|zoomcamp|camp|class)",
        r"\bregistration.*open\b",
        r"\bhow.*join.*this course\b",
        r"\bhow.*join.*course\b",
    ],
    "Where to start / first steps / what to install": [
        r"\bwhere.*\b(do i|to|should i)\b.*start\b",
        r"\bwhat.*should.*install\b",
        r"\bwhat.*tools.*install\b",
        r"\bwhich.*tools.*install\b",
        r"\bbefore.*course start\w*\b.*\b(install|prepare|do)\b",
        r"\bwhat.*\b(do|prepare)\b.*before.*start\b",
        r"\bnew here\b.*\b(start|begin|do)\b",
        r"\bgetting started\b",
        r"\bfirst steps\b",
    ],
    "Self-paced / previous cohort videos still relevant": [
        r"\bself[- ]paced\b",
        r"\bprevious cohort\b",
        r"\bold cohort\b",
        r"\bprevious.*videos\b.*\b(relevant|still)",
        r"\bvideos.*from.*\b(previous|last|old).*cohort",
        r"\b(use|using|watch).*\b(202[0-4])\b.*videos\b",
        r"\b(202[0-4]).*videos.*\b(relevant|valid|use)",
        r"\bare.*\b(old|past|previous).*videos.*\b(relevant|usable|fine)",
    ],
    "Tool substitutions (Podman, alternatives)": [
        r"\bpodman\b",
        r"\binstead of docker\b",
        r"\binstead of postgres\b",
        r"\binstead of terraform\b",
        r"\binstead of mage\b",
        r"\binstead of kestra\b",
        r"\bcan i use\b.*\binstead\b",
        r"\balternative to (docker|postgres|terraform|mage|kestra|airflow|prefect)\b",
    ],
    "Homework submission / form / link": [
        r"\bhomework.*submit\b",
        r"\bsubmit.*homework\b",
        r"\bsubmission.*form\b",
        r"\bhomework.*link\b",
        r"\bwhere.*submit\b",
        r"\bhomework.*url\b",
    ],
    "Homework deadline / late submission": [
        r"\bhomework.*deadline\b",
        r"\bdeadline.*homework\b",
        r"\blate.*homework\b",
        r"\bhomework.*late\b",
        r"\bmissed.*deadline\b",
        r"\bdeadline.*passed\b",
        r"\bextend.*deadline\b",
        r"\bdeadline.*extension\b",
    ],
    "Score / leaderboard / points": [
        r"\bleaderboard\b",
        r"\bmy score\b",
        r"\bwrong.*score\b",
        r"\bscore.*not.*updat\w+",
        r"\bpoints.*missing\b",
        r"\blearning in public.*point",
        r"\blip\b.*point",
        r"\bfaq.*point",
    ],
    "Certificate / passing criteria": [
        r"\bcertificate\b",
        r"\bpass.*course\b",
        r"\bgraduat\w+",
        r"\bminimum.*score\b",
        r"\bpassing.*score\b",
        r"\bhow many points.*pass\b",
    ],
    "Course platform login / account": [
        r"\bcourses\.datatalks\.club\b",
        r"\bcourse platform\b",
        r"\blog ?in.*platform\b",
        r"\bsign ?in.*platform\b",
        r"\baccount.*platform\b",
        r"\bregister.*course\b",
        r"\bregister.*cohort\b",
    ],
    "GCP free credits / billing / account": [
        r"\bgcp\b.*credit",
        r"\b\$?300.*credit",
        r"\bfree trial\b",
        r"\bgcp.*billing\b",
        r"\bgcp.*account\b",
        r"\bgoogle cloud.*credit",
        r"\bgcp.*expired\b",
        r"\bcredit.*expired\b",
        r"\bbilling.*enabled\b",
        r"\bcard.*required\b",
    ],
    "GCP service account / key / IAM": [
        r"\bservice account\b",
        r"\bsa key\b",
        r"\biam.*role\b",
        r"\bgoogle.*credentials\b",
        r"\bgoogle_application_credentials\b",
        r"\bjson key\b",
    ],
    "Docker / docker compose errors": [
        r"\bdocker.*error\b",
        r"\bdocker compose\b",
        r"\bdocker-compose\b",
        r"\bdocker.*permission\b",
        r"\bdocker.*not.*found\b",
        r"\bdocker.*build.*fail",
        r"\bdaemon.*not running\b",
    ],
    "Postgres / pgcli / pgAdmin": [
        r"\bpostgres\b",
        r"\bpgcli\b",
        r"\bpgadmin\b",
        r"\bpsql\b",
        r"\bport 5432\b",
    ],
    "Terraform setup / errors": [
        r"\bterraform\b",
        r"\bterraform.*init\b",
        r"\bterraform.*plan\b",
        r"\bterraform.*apply\b",
    ],
    "Workflow orchestration (Mage/Kestra/Airflow/Prefect/Dagster)": [
        r"\bmage\b",
        r"\bkestra\b",
        r"\bairflow\b",
        r"\bprefect\b",
        r"\bdagster\b",
    ],
    "BigQuery / data warehouse": [
        r"\bbigquery\b",
        r"\bbq\b",
        r"\bdata warehouse\b",
        r"\bpartitioning\b",
        r"\bclustering\b",
    ],
    "dbt cloud / dbt core / models": [
        r"\bdbt\b",
        r"\bdbt cloud\b",
        r"\bdbt core\b",
    ],
    "Spark / PySpark / cluster": [
        r"\bpyspark\b",
        r"\bspark\b",
        r"\bdataproc\b",
    ],
    "Kafka / streaming": [
        r"\bkafka\b",
        r"\bstreaming\b",
        r"\bflink\b",
    ],
    "Final project rules / scope / dataset": [
        r"\bfinal project\b",
        r"\bproject.*dataset\b",
        r"\bdataset.*project\b",
        r"\bproject.*requirements\b",
        r"\bproject.*scope\b",
        r"\bproject.*rubric\b",
        r"\bproject.*evaluation\b",
        r"\bproject.*criteria\b",
    ],
    "Project peer review process": [
        r"\bpeer review\b",
        r"\bevaluating.*project\b",
        r"\breview.*project\b",
        r"\bpeer.*feedback\b",
    ],
    "Project resubmission / second / last attempt": [
        r"\bresubmit\b",
        r"\bre-submit\b",
        r"\bsecond attempt\b",
        r"\blast attempt\b",
        r"\bproject.*attempt\b",
        r"\bredo.*project\b",
    ],
    "Learning in public / posting on social": [
        r"\blearning in public\b",
        r"\blip\b",
        r"\blinkedin.*post\b",
        r"\btwitter.*post\b",
        r"\bx.com.*post\b",
        r"\bblog post\b",
    ],
    "FAQ document / contributing to FAQ": [
        r"\bfaq.*document\b",
        r"\bcontribut\w+.*faq\b",
        r"\bedit.*faq\b",
        r"\badd to faq\b",
        r"\bfaq.*google doc\b",
    ],
    "Videos / playlist / where to watch": [
        r"\bwhich playlist\b",
        r"\bwhere.*video\b",
        r"\byoutube.*playlist\b",
        r"\bvideo.*links\b",
        r"\bwatch.*video\b",
        r"\bvideo.*missing\b",
        r"\bvideos.*available\b",
    ],
    "Codespaces / Gitpod / VM environment": [
        r"\bcodespace\b",
        r"\bgitpod\b",
        r"\bgithub.*vm\b",
        r"\bvirtual machine\b",
        r"\bvm.*setup\b",
        r"\bgcp vm\b",
        r"\bcompute engine\b",
    ],
    "Windows / WSL / Mac M1 / OS-specific": [
        r"\bwindows\b",
        r"\bwsl\b",
        r"\bm1\b",
        r"\bm2\b",
        r"\bapple silicon\b",
        r"\barm64\b",
        r"\bmac.*setup\b",
    ],
    "Telegram / Slack channel access": [
        r"\btelegram\b",
        r"\bslack.*invite\b",
        r"\bslack.*join\b",
        r"\bcan't find.*channel\b",
    ],
    "Quizzes / quiz access / quiz wrong answer": [
        r"\bquiz\b",
        r"\bquiz.*wrong\b",
        r"\bquiz.*answer\b",
        r"\bquiz.*not.*available\b",
    ],
    "Live session timing / timezone / format": [
        r"\bwhat time\b.*\b(session|class|live|stream|course|bootcamp|camp|zoom)\b",
        r"\b(session|class|live|stream).*\bwhat time\b",
        r"\btime.*session\b",
        r"\b(live|session).*timing\b",
        r"\btimings?\b.*\b(session|class|live|stream|cohort|bootcamp|camp|course)",
        r"\b(IST|EST|PST|CST|EET|CAT|CET|UTC|GMT|BST|AEDT)\b",
        r"\btimezone\b",
        r"\btime zone\b",
        r"\bdaily or weekly\b",
        r"\b(weekly|daily) (session|live|class|stream|format)",
        r"\bhow many.*live (sessions?|classes?|streams?)\b",
        r"\b(live|sessions?).*every (day|week|monday|tuesday|wednesday|thursday|friday)\b",
        r"\bsession.*today\b",
        r"\bsession.*tomorrow\b",
        r"\btoday.*session\b",
        r"\btomorrow.*session\b",
        r"\bnext.*(live|session|stream)\b",
    ],
    "Where is the live link / how to join the session": [
        r"\bhow.*join.*(today|live|session|stream|webinar|class|zoom)",
        r"\bwhere.*\b(link|join).*(session|live|stream|class|zoom|today)",
        r"\bcan.*share.*\b(link|stream)",
        r"\b(zoom|youtube).*link\b",
        r"\bhow.*ask questions\b",
        r"\bhow.*question.*ask\b",
    ],
    "Course calendar / google calendar / deadlines list": [
        r"\bgoogle calendar\b",
        r"\bcalendar invite\b",
        r"\bcalendar.*event\b",
        r"\bcourse.*calendar\b",
        r"\b(see|find).*deadlines?\b",
        r"\bdeadline.*spreadsheet\b",
        r"\bsyllabus\b",
        r"\bcurriculum\b",
        r"\btimeline.*course\b",
        r"\bcourse.*timeline\b",
        r"\bcourse.*schedule\b",
        r"\bschedule.*homework\b",
        r"\bhomework.*schedule\b",
    ],
    "Where to find videos / playlist (current cohort)": [
        r"\bwhere.*videos? (for|of).*\b(week|module|cohort|course|2025|2026|module|workshop)",
        r"\bvideos? for.*\b(2025|2026|cohort|module|week)",
        r"\bcohort.*playlist\b",
        r"\b(2025|2026).*playlist\b",
        r"\bplaylist.*(2025|2026|cohort)",
        r"\bonly.*(2|3|4|5|6) videos\b",
        r"\bnew.*videos.*\b(this|new|2026|2025) cohort\b",
        r"\b(updated|update|new).*videos\b",
        r"\bvideos.*missing\b",
        r"\bmissing.*videos\b",
        r"\bvideo.*not.*\b(found|available|posted|uploaded|ready)",
        r"\b(when|where).*new video\b",
        r"\bvideos? for.*module\b",
        r"\bmodule.*videos? available\b",
    ],
    "NYC taxi dataset URL / 403 forbidden / where to get data": [
        r"\b(403|forbidden|access denied)\b",
        r"\bwget.*nyc\b",
        r"\bwget.*tlc\b",
        r"\bwget.*amazonaws\b",
        r"\b(taxi|nyc|tlc).*dataset.*\b(url|link|where|find)",
        r"\b(url|link).*\b(taxi|nyc|tlc).*data",
        r"\b(where|how).*\b(get|find|download).*\b(taxi|nyc|tlc|zone|dataset)",
        r"\bzone.*lookup\b",
        r"\btaxi_zone_lookup\b",
        r"\bdataset.*csv\b.*\b(format|where)",
        r"\bcsv.*format.*\b(taxi|dataset|nyc)",
        r"\bparquet.*csv\b",
        r"\bcsv.*parquet\b",
        r"\b\.csv\.gz\b",
    ],
    "Cloud cost / how much will GCP cost / minimize expenses": [
        r"\bcost.*cloud\b",
        r"\bcloud.*cost\b",
        r"\bminimize.*\b(cost|expense)",
        r"\bcost.*efficient\b",
        r"\bextra cost\b",
        r"\bdo i need to pay\b",
        r"\bdo we need to pay\b",
        r"\bdoes it cost\b",
        r"\bwill (this|it|gcp).*cost",
        r"\bbudget\b.*\b(course|gcp|cloud)",
        r"\b(course|cloud).*\bbudget\b",
        r"\bafraid.*cost\b",
        r"\baccidental cost\b",
        r"\bdelete.*\b(data|gcs|bucket).*\b(cost|charge)",
        r"\b(stop|prevent).*charges?\b",
    ],
    "AWS / Azure / Oracle / alternative cloud": [
        r"\baws\b",
        r"\bazure\b",
        r"\b(oci|oracle).*cloud\b",
        r"\bother cloud\b",
        r"\banother cloud\b",
        r"\binstead of (gcp|google cloud)\b",
        r"\bnot use gcp\b",
        r"\bwithout gcp\b",
        r"\balternative.*\b(cloud|gcp)\b",
        r"\b(cloud|provider).*alternative\b",
        r"\bcan.*use\b.*\b(aws|azure|oracle|oci).*\b(course|module|hw|homework|assignment)",
    ],
    "Homework answer doesn't match options": [
        r"\bnot.*match.*\b(option|answer|choice)",
        r"\bdoesn'?t match.*(option|answer|choice)",
        r"\bdo not match.*(option|answer|choice)",
        r"\bnone of (the )?(options|answers|choices)\b",
        r"\b(answer|number|result|value).*not.*\b(among|in).*\b(option|choice)",
        r"\bgetting (different|wrong|odd|slightly different).*\b(answer|number|result)",
        r"\bdifferent.*(answer|number|result|values?).*\b(option|choice|expected)",
        r"\b(answer|values?|results?|count|rows?).*\b(off|different)\b.*\b(option|choice|expected)",
        r"\bnot in (the )?(option|choice|answer)",
        r"\bclose.*\b(but|to).*\b(option|choice|answer)",
    ],
    "Homework include code / SQL / screenshots in repo": [
        r"\b(should|do|need to).*include.*\b(sql|query|queries|code|screenshot|script)\b.*\brepo\b",
        r"\b(push|share|add|put|upload).*\b(sql|query|queries|code|screenshot|script).*\b(repo|github)",
        r"\bgithub.*\b(sql|query|queries|code|screenshot|script).*\bsubmit",
        r"\bsubmit.*\b(sql|query|code|screenshot)",
        r"\bonly.*(answer|test).*\b(submit|need)",
        r"\b(github|repo).*homework\b.*\bsubmit\b",
        r"\bsingle repo.*\b(homework|all)",
        r"\bdedicated folder.*\bhomework\b",
        r"\bsame repo.*all homework\b",
    ],
    "Forking the repo / git workflow / pull updates": [
        r"\bfork.*repo\b",
        r"\bforked repo\b",
        r"\bpull.*update\b",
        r"\bgit fetch upstream\b",
        r"\bclone.*repo\b",
        r"\b(should|do).*\b(fork|clone).*\brepo\b",
        r"\bnew repo\b.*\bhomework\b",
        r"\b(homework|notes).*\bbranch\b",
        r"\bcreate.*branch\b.*\bhomework\b",
    ],
    "Workshop (dlt / Bruin) - where to find / mandatory": [
        r"\bworkshop.*homework\b",
        r"\bhomework.*workshop\b",
        r"\bworkshop.*\b(mandatory|required|optional)",
        r"\bworkshop.*video\b",
        r"\bvideo.*workshop\b",
        r"\bworkshop.*content\b",
        r"\bwhere.*workshop\b",
        r"\bworkshop.*where\b",
        r"\bworkshop.*before module\b",
        r"\bdlt workshop\b",
        r"\bworkshop.*(dlt|bruin|ingestion)\b",
        r"\b(when|sign up).*\bworkshop\b",
    ],
    "Bruin (2026 cohort)": [
        r"\bbruin\b",
    ],
    "DuckDB": [
        r"\bduckdb\b",
    ],
    "Project: small dataset OK / dataset choice": [
        r"\bproject.*\b(dataset|data) (size|small|big|large)",
        r"\b(too small|small enough|big enough).*project\b",
        r"\bvolume.*data.*project\b",
        r"\bproject.*\b(volume|size).*data\b",
        r"\bkaggle.*project\b",
        r"\bproject.*kaggle\b",
        r"\bcan.*use.*\b(taxi|nyc|kaggle).*project\b",
        r"\bproject.*\b(taxi|nyc) data\b",
    ],
    "Project as a team / two people / collaboration": [
        r"\bproject.*team\b",
        r"\bteam.*project\b",
        r"\b(two|2|pair).*project\b",
        r"\b(team|collaborat\w+).*\bcertif\w+",
        r"\bsubmit.*together\b.*project\b",
    ],
    "Project: API key / private credentials / reproducibility": [
        r"\bapi key.*project\b",
        r"\bproject.*api key\b",
        r"\breproducibility\b",
        r"\bprivate.*credentials\b",
        r"\bprivate.*api\b",
        r"\bsecret.*project\b",
    ],
    "Project: dashboard / Looker / visualization tool": [
        r"\blooker studio\b",
        r"\blooker\b.*\b(dashboard|chart|visual)",
        r"\bdashboard.*tool\b",
        r"\bvisualization tool\b",
        r"\bwhich.*\b(dashboard|chart).*tool\b",
        r"\bdashboard.*screenshot\b",
        r"\bscreenshot.*dashboard\b",
        r"\bdashboard.*public\b",
        r"\bpublic.*dashboard\b",
        r"\bmetabase\b",
        r"\bsuperset\b",
        r"\bpowerbi\b",
        r"\bpower bi\b",
    ],
    "Project: architecture diagram / pipeline diagram tool": [
        r"\b(architecture|pipeline).*diagram\b",
        r"\bdiagram.*\b(architecture|pipeline|workflow|tool)",
        r"\bdraw\b.*\b(architecture|pipeline|workflow)",
        r"\bworkflow.*pictures?\b",
        r"\b(create|make|tool).*\b(architecture|pipeline) diagram",
    ],
    "Project deadline / extension / final attempt": [
        r"\bproject.*deadline\b",
        r"\bdeadline.*project\b",
        r"\bproject.*extension\b",
        r"\bextend.*project\b",
        r"\b(final|3rd|third).*attempt\b",
        r"\battempt.*deadline\b",
        r"\bdeadline.*attempt\b",
        r"\bsubmit.*late.*project\b",
        r"\bmissed.*project.*deadline\b",
    ],
    "Project: how to evaluate / find peer projects to review": [
        r"\bhow.*\b(evaluate|review).*\b(project|peer)",
        r"\bwhere.*\b(evaluate|review).*\b(project|peer)",
        r"\bfind.*\b(project|peer).*\breview\b",
        r"\b(assigned|find).*projects? to review\b",
        r"\bprojects? assigned\b",
        r"\b(can|where).*review.*project",
        r"\bdo.*peer review\b",
        r"\bhow many projects.*review\b",
        r"\bhow to do.*peer review\b",
        r"\bevaluation.*deadline\b",
        r"\bdeadline.*evaluation\b",
        r"\bdeadline.*peer review\b",
    ],
    "Project: minimum score / passing / how scored": [
        r"\bproject.*pass\b",
        r"\bpass.*project\b",
        r"\bproject.*score\b",
        r"\bpassing.*\b(score|points|marks)\b",
        r"\bminimum.*\b(points|score)\b.*project\b",
        r"\bhow.*scored\b",
        r"\bmax(imum)?.*(points|score).*project\b",
    ],
    "Certificate: when received / how to get": [
        r"\bcertificate.*available\b",
        r"\bwhen.*certificate\b",
        r"\bcertificate.*when\b",
        r"\bhow.*\b(get|receive).*certificate\b",
        r"\bcertificate.*receive\b",
        r"\bcertificate.*linkedin\b",
        r"\blinkedin.*certificate\b",
        r"\bt-?shirt\b",
    ],
    "Next zoomcamp / when does ML/MLOps/LLM start": [
        r"\bnext zoomcamp\b",
        r"\bupcoming zoomcamp\b",
        r"\bwhen.*\b(ml|mlops|llm).*zoomcamp\b",
        r"\bml zoomcamp\b.*\b(start|when)",
        r"\bmlops zoomcamp\b.*\b(start|when)",
        r"\bllm zoomcamp\b.*\b(start|when)",
        r"\bafter (this|the) (course|zoomcamp).*\b(next|do|learn)",
        r"\bwhat.*\b(next|after).*\b(course|zoomcamp)",
    ],
    "Removing oneself / changing email / account issues": [
        r"\bremove.*signup\b",
        r"\bsignup.*remove\b",
        r"\bunenrol\w+",
        r"\bunsubscribe.*course\b",
        r"\bdifferent email.*signed up\b",
        r"\bdifferent email.*homework\b",
        r"\bemail.*signup.*homework\b",
        r"\bdid.*receive.*confirmation\b",
        r"\bconfirmation email\b",
    ],
    "Codespaces budget / out of free usage": [
        r"\bcodespace.*\b(budget|limit|free|out of|exceed)",
        r"\b(budget|limit|free|out of|exceed).*codespace\b",
        r"\bspending limit\b",
        r"\bstorage limit\b",
    ],
    "Recommended IDE / Cursor / Antigravity": [
        r"\bcursor\b",
        r"\bantigravity\b",
        r"\bvscode\b.*\b(autocomplete|intellisense|extension)",
        r"\bjetbrains\b",
        r"\bpycharm\b",
        r"\bwhich ide\b",
        r"\brecommended ide\b",
    ],
    "AI / LLM / ChatGPT for course / project": [
        r"\bchatgpt\b.*\b(course|module|hw|homework|assignment|project)",
        r"\b(course|module|hw|homework|assignment|project).*chatgpt\b",
        r"\bai (tool|model|copilot|assistant)\b",
        r"\bvibe.?coding\b",
        r"\bclaude.*\b(course|hw|project)",
        r"\bgemini.*\b(course|hw|project)",
        r"\bcopilot\b.*\b(course|hw|project)",
        r"\b(detect|catch).*\bai\b.*project\b",
    ],
    "Country / city / study buddy lookup": [
        r"\banyone (from|in) [A-Z]",
        r"\banybody (from|in) [A-Z]",
        r"\bany(one|body) here from\b",
        r"\bstudy (partner|buddy|group)\b",
        r"\blearning buddy\b",
        r"\bteam up\b",
        r"\bpair up\b",
        r"\bconnect\b.*\b(timezone|country|city|region)\b",
    ],
    "Recordings / live sessions / office hours": [
        r"\brecording\b",
        r"\boffice hours?\b",
    ],
    "Prerequisites / can I take the course": [
        r"\bprerequisite\b",
        r"\bdo i need.*background\b",
        r"\bsuitable for beginner\b",
        r"\brequired knowledge\b",
        r"\bbeginner friendly\b",
        r"\b(beginner|newbie|new to (data|de|programming)).*\b(suitable|join|take|enough|friendly)",
        r"\b(level|amount).*\b(python|sql|docker).*\bneed\b",
        r"\bhow much.*\b(python|sql|docker)\b.*\b(know|need)\b",
        r"\b(python|sql).*before.*course\b",
    ],
}


def load_threads(path, years):
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            if years and r["date"][:4] not in years:
                continue
            out.append(r)
    return out


def classify(text, compiled):
    matches = []
    for theme, patterns in compiled.items():
        for p in patterns:
            if p.search(text):
                matches.append(theme)
                break
    return matches


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", help="Input .threads.jsonl path")
    ap.add_argument("output", help="Output markdown path")
    ap.add_argument("--year", nargs="+", default=None, help="Filter to these years (e.g. --year 2025 2026)")
    ap.add_argument("--samples", type=int, default=5, help="Number of sample Q/A per theme to include")
    ap.add_argument("--themes", default=None, help="Optional JSON file with theme->patterns map")
    ap.add_argument("--unmatched-limit", type=int, default=0, help="How many unmatched questions to list at the end of main file (0 = none, write to separate --unmatched-file)")
    ap.add_argument("--unmatched-file", default=None, help="Write all unmatched questions to this separate file (default: <output>.unmatched.md)")
    args = ap.parse_args()

    themes = THEMES
    if args.themes:
        with open(args.themes, encoding="utf-8") as f:
            themes = json.load(f)

    compiled = {t: [re.compile(p, re.IGNORECASE) for p in pats] for t, pats in themes.items()}

    threads = load_threads(args.input, set(args.year) if args.year else None)
    print(f"Loaded {len(threads)} threads after year filter")

    by_theme = defaultdict(list)
    unmatched = []
    n_with_replies = 0
    n_without_replies = 0
    for r in threads:
        if r["n_replies"] > 0:
            n_with_replies += 1
        else:
            n_without_replies += 1
        matches = classify(r["question"], compiled)
        if not matches:
            unmatched.append(r)
            continue
        for m in matches:
            by_theme[m].append(r)

    # Write markdown
    with open(args.output, "w", encoding="utf-8") as out:
        years_str = ", ".join(args.year) if args.year else "all years"
        out.write(f"# Slack FAQ candidates - draft\n\n")
        out.write(f"Source: {args.input}\n\n")
        out.write(f"Years included: {years_str}\n\n")
        out.write(f"Total threads analyzed: {len(threads)}\n\n")
        out.write(f"  - threads with at least one reply: {n_with_replies}\n")
        out.write(f"  - threads with NO replies (unanswered questions): {n_without_replies}\n\n")
        out.write(f"Themes matched: {len(by_theme)}\n\n")
        out.write(f"Threads not matching any theme keyword (need new themes / manual review): {len(unmatched)}\n\n")
        out.write("Note: 'unmatched' = the question text didn't fire any theme regex; it does NOT mean the thread has no replies. Both answered and unanswered threads can be unmatched.\n\n")
        out.write("---\n\n")

        sorted_themes = sorted(by_theme.items(), key=lambda kv: -len(kv[1]))
        out.write("## Theme frequency summary\n\n")
        for theme, items in sorted_themes:
            out.write(f"- {theme}: {len(items)}\n")
        out.write("\n---\n\n")

        for theme, items in sorted_themes:
            out.write(f"## {theme} ({len(items)} threads)\n\n")
            # Sort items: prefer those with answers, then most recent
            items.sort(key=lambda r: (r["n_replies"] == 0, r["date"]), reverse=False)
            shown = 0
            for r in items:
                if shown >= args.samples:
                    break
                out.write(f"### [{r['date']}] {r['user']} (replies: {r['n_replies']})\n\n")
                q = r["question"].strip()
                if len(q) > 600:
                    q = q[:600] + " ..."
                out.write("Q: " + q.replace("\n", "\n   ") + "\n\n")
                if r["answer"]:
                    a = r["answer"].strip()
                    if len(a) > 1200:
                        a = a[:1200] + " ..."
                    out.write("A: " + a.replace("\n", "\n   ") + "\n\n")
                shown += 1
            out.write("---\n\n")

        if args.unmatched_limit > 0:
            out.write("## Questions not matched by any theme (sample)\n\n")
            out.write(
                f"These didn't fire any theme regex. Showing first {args.unmatched_limit} of {len(unmatched)}. "
                "Full list in the unmatched file. [r:N] = reply count (r:0 = unanswered).\n\n"
            )
            for r in sorted(unmatched, key=lambda x: x["date"], reverse=True)[: args.unmatched_limit]:
                q = r["question"].strip().replace("\n", " ")
                if len(q) > 240:
                    q = q[:240] + " ..."
                out.write(f"- [{r['date']}] [r:{r['n_replies']}] {q}\n")

    # Write the full unmatched list to a separate file
    unmatched_path = args.unmatched_file or args.output.rsplit(".", 1)[0] + ".unmatched.md"
    with open(unmatched_path, "w", encoding="utf-8") as out:
        out.write("# Unmatched questions (no theme bucket fired)\n\n")
        out.write(f"Source: {args.input}\n\n")
        years_str = ", ".join(args.year) if args.year else "all years"
        out.write(f"Years: {years_str}\n\n")
        out.write(f"Total: {len(unmatched)}\n\n")
        out.write("[r:N] = reply count (r:0 = unanswered). Sorted oldest first.\n\n")
        out.write("---\n\n")
        for r in sorted(unmatched, key=lambda x: x["date"]):
            q = r["question"].strip().replace("\n", " ")
            if len(q) > 400:
                q = q[:400] + " ..."
            out.write(f"- [{r['date']}] [r:{r['n_replies']}] {q}\n")
    print(f"Wrote unmatched: {unmatched_path}")

    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
