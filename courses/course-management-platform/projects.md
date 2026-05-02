---
title: "Projects"
layout: default
nav_order: 3
parent: Course Management Platform
has_children: false
---

# Project Submission

This page covers the platform UI for submitting your project. For project structure, attempts logic, dataset choice, and tech stack flexibility, see [Final Project]({{ '/courses/zoomcamp-logistics/project/' | relative_url }}).

<div style="position: relative; padding-bottom: 56.25%; height: 0;">
  <iframe src="https://www.loom.com/embed/8f99d25893de4fb8aaa95c0395c740b6" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

## Where to find the project page

Log in to your course platform and open the project page. You will see the active project window, the deadline, and the submission form when it is open.

## Submission form

<img src="{{ '/assets/images/course-management-platform/project-submission.png' | relative_url }}" alt="Project submission form" width="80%">

The form fields:

- GitHub link - URL to your public project repository.
- Commit ID - the specific commit hash for your submission. Use the first seven characters of the commit hash.
- Learning in public links - links to your social media posts about the project (see [Learning in Public]({{ '/courses/course-management-platform/learning-in-public/' | relative_url }})).
- Time spent on project - number of hours invested.
- FAQ contribution - share insights for the [Course FAQ]({{ '/courses/faq/' | relative_url }}).
- Certificate name - name to appear on your certificate.

## Certificate name vs display name

Your certificate name and display name are separate:

- Display name appears on the leaderboard. You can keep it anonymous if you prefer.
- Certificate name is what gets printed on your certificate.

Set your certificate name before submitting; otherwise you may end up with a placeholder.

## Commit ID and updating it

If you keep committing after submission, update the commit ID in the form so reviewers see what you intended them to review. Reviewers will look at the repo at the commit ID you submitted, not the latest version.

To check a specific commit on GitHub, use:

```
https://github.com/user/repo/tree/COMMIT_ID
```

This is what reviewers will see. To run the project locally at that commit, check out the commit ID after fetching the repo.

## Project gallery

After cohorts complete, projects are visible in the platform's project gallery.

<img src="{{ '/assets/images/course-management-platform/project-gallery.png' | relative_url }}" alt="Project gallery" width="80%">

Browse past projects for inspiration:

- [ML Zoomcamp 2025 projects](https://courses.datatalks.club/ml-zoomcamp-2025/projects)
- [Data Engineering Zoomcamp 2025 projects](https://courses.datatalks.club/de-zoomcamp-2025/projects)
- [Data Engineering Zoomcamp 2024 projects](https://courses.datatalks.club/de-zoomcamp-2024/projects)

## See also

- [Final Project]({{ '/courses/zoomcamp-logistics/project/' | relative_url }}) for general project logistics (rubric, attempts, dataset, tech stack).
- [Peer Review]({{ '/courses/course-management-platform/peer-review/' | relative_url }}) for the platform UI for reviewing other students' projects.
- [Peer Review (logistics)]({{ '/courses/zoomcamp-logistics/peer-review/' | relative_url }}) for how peer review works overall.
