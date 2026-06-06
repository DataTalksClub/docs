---
title: "Homework"
layout: default
nav_order: 7
parent: Zoomcamp Logistics
---

# Homework

When homework opens, when it closes, what to do with it. For the platform UI (where to click on the submission page), see [Course Management Platform: Homework]({{ '/courses/course-management-platform/homework/' | relative_url }}).

## Optional, but recommended

In every DataTalks.Club zoomcamp, homework is optional for certification. Only the project (or projects) is required.

Homework is still worth doing:

- Checks your understanding of the module.
- Earns leaderboard points.
- Builds material for your portfolio.
- Good preparation for the project.

## Release

Each module's homework is published when the module starts. You find it in the course's GitHub repo at `cohorts/<year>/<module>/homework.md` (path varies slightly per course).

The submission form on the [course platform](https://courses.datatalks.club/) opens when the homework is officially released. Until then, even if you can read the questions in the repo, the form is not yet active.

## Deadlines

- Strict deadlines, announced on the course platform and in Slack and Telegram.
- Typically one week to ten days after release.
- Exact deadline (with time and time zone) is on the course platform.
- Most platform deadlines are shown in your local time zone.

## After the deadline

- The course team closes the submission form. Submitting is no longer possible after that.
- You can no longer submit for leaderboard points.
- Existing submissions stay.
- You can still do the homework on your own and push it to your repo.

There are no individual extensions. In rare cases (server outage, bug in the questions) the cohort lead may extend the deadline for everyone, announced in Slack.

## Submission

The form on the course platform asks for:

- Your answer to each question (multiple choice, numbers, or short answers).
- A link to your public GitHub repository for the homework code.
- Optionally a link to your social media post (earns learning-in-public points).

For the platform UI, see [Course Management Platform: Homework]({{ '/courses/course-management-platform/homework/' | relative_url }}).

## What goes in your repository

The form mostly checks your answers, not your code. Your repo should:

- Be public so peer reviewers and graders can see it.
- Contain the code or queries you used to arrive at your answers.
- Have a README that explains how to run it.
- Use meaningful file names (`week_3_data_warehouse/` rather than `hw3/`).

Whether to include screenshots, SQL queries, or notebooks depends on the question. Generally include enough that someone can follow what you did.

You can use a single repository for all homework (one folder per module) or one repository per module. Either works.

## When your answer does not match

If your numerical answer is close to one of the options, pick the closest. Small differences usually come from:

- Slightly different filtering (inclusive vs exclusive date boundaries).
- Different versions of the dataset.
- Floating-point or rounding differences.

If your answer is far from any option, double-check the question (they often specify a precise filter) and the dataset version. Ask in the course Slack thread if you are stuck. Other students often have the same issue and the cohort lead may clarify.

## Solutions

Solutions are usually published in the course repository after the deadline closes, under `cohorts/<year>/<module>/`. If you do not see them, ask in Slack - they may not be published yet, or community contributions to the FAQ have the breakdown.

## Quizzes vs free-form answers

- Multiple-choice quizzes in some courses.
- Free-form answers in others.
- Some mix the two.

The format is described in each module's homework page in the repo. All formats use the same submission flow on the course platform.

## Where to keep your homework code

Create a separate personal repo for your homework code. Do not work directly inside the course repository.

- Browse course materials on GitHub (the web UI lets you read each file or download just the ones you need).
- Keep your homework solutions in your own public repo so peer reviewers and graders can see them.
