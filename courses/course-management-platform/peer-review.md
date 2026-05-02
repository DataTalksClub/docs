---
title: "Peer Review"
layout: default
nav_order: 4
parent: Course Management Platform
has_children: false
---

# Peer Review

This page covers the platform UI for peer review. For why peer review exists, how many you do, what to do with 404 repos, and tips for writing good reviews, see [Peer Review]({{ '/courses/zoomcamp-logistics/peer-review/' | relative_url }}).

## Where to find your assigned projects

After the project submission deadline, your assigned projects appear on the platform. Open the project page for the cohort and look for "Projects to Review".

<img src="{{ '/assets/images/course-management-platform/peer-review-assignment.jpg' | relative_url }}" alt="Peer review assignment showing 3 projects to evaluate" width="80%">

If you submitted but do not see assignments yet, give it a day. The cohort lead releases assignments once after the deadline closes.

## Evaluation form

Click on a project card to open the evaluation form.

<img src="{{ '/assets/images/course-management-platform/peer-review-evaluation.jpg' | relative_url }}" alt="Peer review evaluation form with criteria" width="80%">

The form shows the course-specific rubric (criteria, point values per criterion). Score each criterion and add comments.

## Reviewing the project at the right commit

The author submitted a specific commit ID. Review the project as it was at that commit, not the latest version of the repo.

GitHub URL pattern to view a specific commit:

```
https://github.com/user/repo/tree/COMMIT_ID
```

You can browse the project on GitHub at this URL without downloading anything. If you want to run the code locally, check out the project at the submitted commit ID before running.

## Reproducing the project

Reproducing projects you review (running them locally, deploying them) is good learning when you have time.

Sometimes full reproduction is not possible - you may need cloud credentials you do not have, or the setup may take longer than the review window allows. Use your judgment. You can evaluate all the criteria from reading the code and the README without running it.

## Plagiarism

If you notice plagiarism while reviewing, give the project zero points for everything and note it in the comments. The cohort lead investigates flagged cases.

Self-plagiarism rules:

- You cannot reuse a project from another course without changes.
- If you passed attempt one, you cannot submit the same project for attempt two (you would get double the points).
- If you failed attempt one, you can improve and resubmit for attempt two.

## See also

- [Peer Review (logistics)]({{ '/courses/zoomcamp-logistics/peer-review/' | relative_url }}) for general logistics.
- [Project Submission]({{ '/courses/course-management-platform/projects/' | relative_url }}) for the platform UI when submitting your own project.
