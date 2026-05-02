---
title: "Peer Review"
layout: default
nav_order: 11
parent: Zoomcamp Logistics
---

# Peer Review

Project scoring is done by peer review: every participant who submits a project also reviews other participants' projects. For platform UI, see [Course Management Platform: Peer Review]({{ '/courses/course-management-platform/peer-review/' | relative_url }}).

## Why peer review

- It scales. Cohorts have hundreds of participants; the cohort lead alone cannot grade all projects.
- It is a learning experience. Reading other projects' code teaches you patterns you would not see otherwise.
- It mirrors real work. Code review is a core engineering skill.

## How it works

After the project submission deadline:

1. Each project is randomly assigned to several reviewers (typically 3 reviewers per project).
2. Each participant who submitted is assigned several projects to review (typically 3).
3. Reviewers score each project against the course's rubric.
4. The final project score is aggregated from the reviewer scores.
5. Reviewers earn points for completing reviews on time.

## How many you review

Typically 3 projects per submission attempt. The exact number is shown on the course platform when you are assigned reviews.

If you submit in attempt 1 and again in attempt 2, you get a fresh set of projects to review for each submission.

## When assignments appear

Assignments do not appear automatically after the submission form closes. The cohort lead opens peer review separately and announces it in Slack and Telegram once it is open. After the announcement, your assigned projects appear on your course platform dashboard.

If the announcement has already gone out and you submitted but do not see assignments, post in the course Slack channel.

## Deadline for reviews

Typically one week from when reviews are assigned. The exact deadline is on the course platform.

If you do not complete your reviews by the deadline:

- You lose the points for those reviews.
- Your project still receives scores from the reviewers it was assigned to, but it fails the project regardless of those scores.
- A failed project means no certificate.

Skipping peer reviews is the most common reason participants who submitted a passing-quality project still do not receive a certificate.

## When a project repo is 404

Some submitted repos go private or get deleted between submission and review. If a repo you are assigned is unavailable:

- Wait a day; sometimes it is a temporary issue.
- If still unavailable, mark the project with a zero score and note in the review that the repo was unreachable.
- Do not skip the review. You still need to submit it for credit.

The cohort lead handles repeat issues. If you see a pattern (multiple bad repos), flag it in Slack.

## When the tech stack is unfamiliar

Some students use stacks the course did not teach (for example, AWS instead of GCP, Airflow instead of Mage). When reviewing such a project:

- Read the README carefully; the participant should explain their choices.
- Use the rubric criteria, which are mostly stack-agnostic ("is there a documented pipeline?", "is the data warehouse used correctly?").
- If something is genuinely unclear, give partial credit and note it in the comments rather than zero.

If you really cannot evaluate something, that is fair feedback in itself - the participant did not document well enough.

## Writing a good review

- Be honest. Inflated scores devalue the certificate.
- Be constructive. Point out what could be improved, not just what is missing.
- Be specific. "The README is unclear" is less useful than "the README does not explain how to set the GCP credentials."
- Be reasonable. Most projects have rough edges; do not penalize a good project for cosmetic issues.

## Beyond your assignment

You can voluntarily review additional projects. This usually does not earn extra points but it is useful learning and helps the community.

## Fairness

Peer-review scores are aggregated across multiple reviewers, which smooths out individual harshness or generosity. If you think one reviewer was clearly out of line (gave a low score with no justification), post in Slack so the cohort lead can take a look.

## AI-generated reviews

Using LLMs to draft reviews is fine. But if you let the LLM do the whole thing without actually looking at the project, you lose the main reason peer review exists - reading other people's code is one of the best learning opportunities in the course.

## When you find out your score

After the peer-review window closes, the cohort lead aggregates scores. Final scores typically appear on the course platform 1 to 2 weeks after the review deadline.

If you do not see your score after that window, post in Slack.
