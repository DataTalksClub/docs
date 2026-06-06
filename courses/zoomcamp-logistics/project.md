---
title: "Final Project"
layout: default
nav_order: 1
parent: Project and Certificate
grand_parent: Zoomcamp Logistics
---

# Final Project

The project is the only thing required for the certificate. This page covers the cross-course logistics. The exact rubric and required components are course-specific - see the project page on the individual course.

For platform UI (where to submit, how the form works), see [Course Management Platform: Projects]({{ '/courses/course-management-platform/projects/' | relative_url }}).

## What it is

A capstone piece of work where you apply what you learned. Each course defines what a "valid" project looks like:

- Data Engineering Zoomcamp: an end-to-end data pipeline (ingestion, warehouse, transformation, dashboard).
- Machine Learning Zoomcamp: a deployed ML model with peer-reviewed code.
- LLM Zoomcamp: an LLM-powered application.

Check the course page for the rubric.

## How many projects

Depends on the course:

- One project, multiple submission attempts.
- Two of three projects required (Machine Learning Zoomcamp: midterm + capstone, or capstone + second capstone).
- Single project with one window for some smaller cohorts.

The course page lists the exact structure for the current cohort.

## Solo, not team

Generally projects are individual work. Each participant earns their own certificate based on peer-reviewed scoring. Some cohorts have made exceptions for small teams, but the default is solo. Check with the cohort lead before pairing up.

## When to start

You can start at any point in the cohort. Most participants start during the last 2 to 3 weeks of modules, once they have seen the relevant material.

The submission window typically opens around 2 to 3 weeks before its deadline, after the last module. Window dates are on the course platform.

## Time commitment

- 2 to 3 weeks of focused work.
- The submission window is usually 2 to 3 weeks long.
- Peer review runs in the week after submission closes.

For courses with multiple project windows, each window is usually 2 weeks of submission plus 1 week of peer review.

## Multiple submission attempts

When a course offers multiple attempts, each attempt has its own deadline. The intent is to submit one project once - the second attempt exists as a backup if you fail the first or could not finish in time.

What you can submit in attempt 2:

- If you failed attempt 1: improve the project and resubmit it for attempt 2. This is allowed.
- If you passed attempt 1: you cannot resubmit the same project for attempt 2, even if you improved it. That counts as self-plagiarism and disqualifies you if attempt 1 had already given you a passing score. To submit something for attempt 2, it must be a different project (different problem, different dataset, different code).

Submitting two different projects across the two windows is possible but not the typical path. Leaderboard scores in that case are summed across attempts (attempt 1 score + attempt 2 score), not "best of two".

Skipping attempt 1 and only submitting in attempt 2 is fine.

## Resubmitting before the deadline

You can resubmit any number of times before the deadline closes. Only the latest submission counts. Common reasons to resubmit:

- You found a bug and pushed a fix; update the commit ID in the form to match.
- You added more learning-in-public links and want them counted.
- You forgot to set your certificate name.

Once the form is closed, no more updates are accepted. A typo in a link or a wrong commit ID cannot be fixed after the deadline.

## Dataset

Generally any dataset works, with one rule that applies to every zoomcamp:

- You cannot use a dataset that the course itself uses in lectures or homework. The point of the project is to apply your skills to something new, not to redo the course example.
- Each course's project page lists the specific datasets that are off-limits for that course.

Beyond that:

- Pick something you find interesting; you will work with it for weeks.
- Large enough to make the engineering meaningful, but does not have to be huge. A few hundred MB is fine.
- Public datasets (Kaggle, government open data, public APIs) are common.
- Private or proprietary data is not recommended because peer reviewers must be able to reproduce.

For DE-style projects specifically, pick something with a sensible pipeline shape: ingestion, warehouse, transformations, presentation.

## Tech stack

You are not required to use the same tools as the course. If the course taught GCP and you want to use AWS, that is fine. If the course taught Mage and you want to use Airflow, that is fine.

Caveats:

- Document your choices clearly in the README so reviewers can follow.
- Reviewers may not be familiar with your stack. Help them understand it.
- Make the project reproducible. If a reviewer cannot run it (or at least understand how it would run), you lose points on the reproducibility criterion.

## API keys and credentials

- Use environment variables. Never commit secrets.
- Document in the README how a reviewer would obtain the necessary credentials (for example, "sign up for a free API key at xyz.com").
- If the data source absolutely requires private credentials, accept that you may lose some reproducibility points. Document the trade-off.

## Cloud costs

Most projects can be built on free tiers. If you need cloud resources beyond the free tier:

- Use sample data instead of full data during development.
- Tear down expensive resources (clusters, large warehouses) when not actively using them.
- For DE projects, GCP free credits ($300) cover the project for most students.

## Repo gotchas

- Make your repo public before submitting. Submitted repos that are private or deleted at peer-review time count as not submitted.
- If you accidentally pushed secrets, do not delete the repo. Rotate the secrets, remove them from the repo (and history if possible), and keep the repo accessible.

## After submitting

You can share your project freely. Your project goes into the project gallery on the course platform after the cohort and is a great portfolio piece. Share on LinkedIn, X, your personal site.

For sharing in Slack, use the appropriate promotion channel (`#shameless-promotion`, `#interesting-content`) following the [promotion rules]({{ '/general/guidelines/promotion/' | relative_url }}).
