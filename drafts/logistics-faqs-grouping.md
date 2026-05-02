# Logistical FAQs - proposed grouping for the docs

Source: `drafts/de-zoomcamp-slack-faqs.md` (mined from #course-data-engineering, 2025-2026 cohorts).

This is a curation pass. Technical errors (Postgres/Docker/Terraform/dbt/BigQuery/Spark/Kafka/orchestrator stack traces) are excluded - those live in the public FAQ at https://datatalks.club/faq/.

For each theme: counts are total threads matching that theme keyword pattern in 2025-2026 of the DE channel. Sample Q+A is in `de-zoomcamp-slack-faqs.md` under each theme heading.

Three proposed destinations:

1. New `zoomcamp-logistics` section - common to all DTC zoomcamps. Suggested location: `general/zoomcamp-logistics/`
2. DE-specific page - lives under `courses/data-engineering-zoomcamp/`
3. Course Management Platform docs - lives under `courses/course-management-platform/`

---

## The course stages (skeleton for `zoomcamp-logistics`)

Every DTC zoomcamp follows the same lifecycle. The new section can be organized around these stages, with one page per stage. Each stage maps to a cluster of recurring questions:

Stage 0 - Before you sign up
- What is a DTC zoomcamp? Live cohort vs self-paced.
- Cost and certification - is it free, what does the certificate look like, do I have to pay.
- Prerequisites in general terms (programming, command line, git, docker - exact stack varies per course).
- Time commitment.
- Schedule of upcoming cohorts ("when does ML Zoomcamp start", "when is the next DE cohort").

Stage 1 - Registration and cohort kickoff
- How to register / enroll.
- Confirmation email - what to expect, what if it didn't arrive.
- Joining Slack and the course-specific channel.
- Joining Telegram and the newsletter.
- The course management platform (`courses.datatalks.club`) account - login, identity.
- Adding the public Google Calendar; cohort start date.
- Where to find the GitHub repo, the YouTube playlist, the FAQ.
- Live kickoff session - timing in your timezone, where to watch, will it be recorded.
- Joining mid-cohort - "I'm late, can I still participate?" "What did I miss?"

Stage 2 - Working through the modules
- Module / week cadence - new content drops weekly during a live cohort.
- Live sessions vs pre-recorded - which courses have weekly live sessions, where the link is, recordings.
- Where this cohort's videos are vs older cohort videos. Are previous-cohort videos still relevant.
- Setting up the development environment (course-specific tools - DE has Docker/GCP/Terraform; ML has Python/sklearn/AWS).
- Codespaces / cloud VM / local. Codespaces budget warnings.
- Tool substitutions - "can I use AWS instead of GCP", "can I use Podman instead of Docker".

Stage 3 - Homework
- Homework is published per module under `cohorts/<year>/<module>` in the course repo.
- Submission form is shared in Slack and on the course platform.
- Hard deadlines - the form closes after the deadline. Time zones.
- Late submissions - usually no grace, but policies for the leaderboard differ by course.
- What to put in the GitHub repo (code, queries, screenshots).
- Homework optional for certification (in most courses) but counts for the leaderboard.
- "My answer doesn't match the options" - common verification request.
- Quizzes and scoring - which courses use multiple-choice quizzes vs free-form.

Stage 4 - Workshops and special modules
- Workshops sit between modules and have their own homework. Where to find them, when they happen, are they mandatory.
- New modules in newer cohorts (e.g. Bruin in DE 2026) - how they fit into the curriculum.

Stage 5 - The leaderboard and learning in public
- How leaderboard points are calculated (homework, learning in public, FAQ contributions).
- Learning in public - what counts as a valid post, what doesn't, the misuse policy.
- FAQ contributions - how to propose entries, link to the FAQ bot flow.

Stage 6 - The final project (or projects)
- Project structure varies by course - DE has 1 project with 2-3 attempts; ML has midterm + capstone (2 of 3 needed); MLOps has its own structure.
- Project rubric - generic shape (problem statement, dataset, pipeline, deployment, reproducibility, dashboard) but exact criteria are course-specific.
- Dataset choice - "is this dataset too small?", "can I use Kaggle?", "can I reuse course data?"
- Tech stack flexibility - same answer across courses ("yes you can deviate, but document for reviewers").
- Project as a team - same answer across courses (usually solo).
- Submission mechanics live in CMP docs.

Stage 7 - Peer review
- Why peer review exists.
- How many projects you must review (typically 3 per attempt).
- How projects are assigned, when the assignment becomes visible.
- Evaluation criteria, tips for good reviews.
- What happens if a project repo is 404 or private.
- Deadline for reviews vs deadline for submissions.

Stage 8 - Results and certification
- When are projects scored.
- Minimum passing score.
- When certificates are issued.
- Adding the certificate to LinkedIn.
- The DataTalks T-shirt program.
- What's next - which zoomcamp to take after this one, how to use the project in interviews.

Cross-stage / community
- Asking for help effectively - same `general/guidelines/asking-for-help.md` content.
- Country / city / study-buddy threads - point to regional Slack channels.
- AI / Cursor / ChatGPT policy - generally welcomed; same caveat across courses about understanding the code.
- Removing yourself from the cohort, changing email.

---

## 1. `zoomcamp-logistics` section (common to all courses)

Mapping the FAQ themes to the stages above:

`zoomcamp-logistics/overview.md` - what is a zoomcamp, free, certificate, time commitment, upcoming cohort schedule
- Course start / cohort schedule (89)
- Self-paced / previous cohort videos still relevant (25)
- Next zoomcamp / when does ML/MLOps/LLM start (~10-15 implicit)

`zoomcamp-logistics/registration.md` - register, confirmation, account on platform
- How to join / register / enroll (34)
- Removing oneself / changing email / account issues (~5-10)
- Country / city / study buddy lookup (21) - point to regional Slack channels rather than answer

`zoomcamp-logistics/joining-mid-cohort.md` - the single most-repeated logistical question
- Joining mid-cohort / late start / what did I miss (108)

`zoomcamp-logistics/live-sessions.md` - timing, where to watch, recordings, calendar
- Live session timing / timezone / format (68)
- Where is the live link / how to join the session (30)
- Recordings / live sessions / office hours (17)
- Course calendar / google calendar / deadlines list (33)

`zoomcamp-logistics/dev-environment.md` - general dev setup that applies across courses
- Recommended IDE / Cursor / Antigravity (10)
- Codespaces budget / out of free usage (9)
- Forking the repo / git workflow / pull updates (14)
- AI / LLM / ChatGPT for course / project (12) - covers policy + caveat

`zoomcamp-logistics/finishing.md` - certificate, t-shirt, what's next
- Certificate when received / how to get (29)

---

## 2. DE-specific pages (under `courses/data-engineering-zoomcamp/`)

These belong on the DE page because they reference DE-specific tools, dataset, or curriculum.

Cloud setup (extend `getting-started.md` or new `gcp-setup.md`)
- GCP free credits / billing / account (64). $300 credits, OR_BACR2 errors when adding payment method - perennial blocker. Country-specific card issues.
- GCP service account / key / IAM (46). Where to put the JSON key, GOOGLE_APPLICATION_CREDENTIALS.
- Cloud cost / how much will GCP cost / minimize expenses (6).
- AWS / Azure / Oracle / alternative cloud (61). Same answer every cohort - point to `#de-course-aws` etc.

Environment setup (extend `getting-started.md` or new `environment.md`)
- Codespaces / Gitpod / VM environment (48) - DE-specific because of GCS/BigQuery integration.
- Windows / WSL / Mac M1 / OS-specific (81). Mac silicon, Docker Desktop "Malware Blocked", Colima, Podman.
- Tool substitutions (Podman, alternatives) (8).

Dataset access (extend the existing `resources/dataset.md`)
- NYC taxi dataset URL / 403 forbidden / where to get data (99). The recurring `wget https://s3.amazonaws.com/nyc-tlc/...` 403. Use the DataTalksClub mirror. Parquet vs CSV. Where the zone lookup files are.

Course content navigation (extend `resources/index.md` or `getting-started.md`)
- Where to find videos / playlist (current cohort) (44).
- Workshop (dlt / Bruin) - where to find / mandatory (51).
- Bruin (2026 cohort) (61).
- DuckDB (46).

Project guidance (extend `logistics/projects.md`)
- Final project rules / scope / dataset (115).
- Project: small dataset OK / dataset choice (~10-15).
- Project: API key / private credentials / reproducibility (9).
- Project: dashboard / Looker / visualization tool (14).
- Project: architecture diagram / pipeline diagram tool (~5).

---

## 3. Course Management Platform docs (under `courses/course-management-platform/`)

These are about the platform itself - same flow for every course.

Homework on the platform (extend `homework.md`)
- Homework submission / form / link (112).
- Homework deadline / late submission (51). Local time vs UTC vs CET.
- Homework include code / SQL / screenshots in repo (19).
- Homework answer doesn't match options (21).
- Score / leaderboard / points (17).
- Course platform login / account (49).

Project on the platform (extend `projects.md` and `peer-review.md`)
- Project deadline / extension / final attempt (81).
- Project resubmission / second / last attempt (89).
- Project: how to evaluate / find peer projects to review (60).
- Project: minimum score / passing / how scored (39).
- Project as a team / two people / collaboration (65) - mostly false-positive matches; one-line mention.

Learning in public (existing `learning-in-public.md` covers it)
- Learning in public / posting on social (28). The "is there a template for the LinkedIn post" question keeps coming back - link the template prominently.

---

## What's already in ml-zoomcamp docs that overlaps with the proposed `zoomcamp-logistics`

I checked `courses/ml-zoomcamp/` to see what's already course-specific that would naturally move (or be linked from) the new section. Several pages are de-facto general but currently live under ML:

- `ml-zoomcamp/getting-help.md` - this is the "asking for help" pattern. Same as `general/guidelines/asking-for-help.md`. Should consolidate.
- `ml-zoomcamp/resources.md` - GitHub / YouTube / Slack / Telegram / Newsletter / FAQ / Community Notes / Regional Meetups. Structurally identical for every zoomcamp. Would be a `zoomcamp-logistics/resources.md` template, with each course's `resources.md` linking out and adding only course-specific extras.
- `ml-zoomcamp/getting-started.md` "Course Structure and Flexibility" section - explains self-paced vs cohort. Generic.
- `ml-zoomcamp/getting-started.md` step 4 "Join the Learning Community" - Slack/Telegram intro. Generic.
- `ml-zoomcamp/assignments-and-scoring.md` sections 1, 2, 3 - "homework is published per cohort", "form closes after deadline", "homework optional for cert". The mechanics are identical across zoomcamps; only the cohort path differs.
- `ml-zoomcamp/certification.md` - the "what counts as required vs optional", "2 weeks dev + 1 week peer review" cadence, "use any tech but document for reviewers" guidance. The "2 of 3 projects" rule and "deployed model required" are ML-specific. Worth splitting: keep the project mechanics in the general section, keep the ML-specific scoring rules on the ML page.
- `ml-zoomcamp/success.md` - learning in public, study strategy, portfolio development. Generic across all courses.
- `ml-zoomcamp/prerequisites.md` sections 1, 4 - "command line, git, docker basics", "AI tools welcome". Generic. The Anaconda/UV/sklearn/AWS specifics are ML-only.

Recommendation: when building the `zoomcamp-logistics` section, lift the generic content from ML's pages, leave only ML-specific deltas on the ML pages, and have the ML pages link to the general section. Same approach when DE gets equivalent docs.

---

## Themes excluded (technical / not logistical)

These belong in the public FAQ at https://datatalks.club/faq/:

- Workflow orchestration (Mage/Kestra/Airflow/Prefect/Dagster): 385
- Postgres / pgcli / pgAdmin: 255
- dbt cloud / dbt core / models: 210
- BigQuery / data warehouse: 187
- Docker / docker compose errors: 139
- Terraform setup / errors: 138
- Spark / PySpark / cluster: 95
- Kafka / streaming: 67

Some have logistical sub-questions (e.g. "is Kafka in 2026?" or "Mage vs Kestra - which one is in this cohort?") - those belong in the DE curriculum overview, not a tech FAQ.

---

## Open questions for you

1. Location and naming of the new section. Proposing `general/zoomcamp-logistics/` (sibling of `general/slack.md`, `general/jobs/`, `general/guidelines/`). Alternative: top-level `/zoomcamp-logistics/`. Which?
2. The CMP docs already have `homework.md`, `projects.md`, `peer-review.md`, `leaderboard.md`, `learning-in-public.md`. Extend those in place, or add a single CMP-FAQ page that just lists the recurring questions and links to the relevant section?
3. Joining mid-cohort is the #1 logistical question. It deserves its own page (proposed `zoomcamp-logistics/joining-mid-cohort.md`) so the link can be pasted into Slack threads. Confirm?
4. For the AWS/Azure question, two options: (a) one paragraph in the DE getting-started saying "yes but you're on your own, see #de-course-aws"; (b) a small dedicated `alternative-cloud.md` page on the DE side that lists the alternative-cloud Slack channels and any community resources. Which?
5. Should I also mine #course-ml-zoomcamp / #course-mlops-zoomcamp / #course-llm-zoomcamp now (the script supports any channel) before drafting the general pages, to confirm the cross-course themes hold? Or proceed with the DE-only signal first?
