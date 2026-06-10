---
title: "Environment Setup"
layout: default
nav_order: 4
parent: Data Engineering Zoomcamp
has_children: false
---

# Environment Setup

The Data Engineering Zoomcamp uses Docker, Terraform, Google Cloud Platform (GCP), and Python. This page covers the high-level setup decisions. For detailed step-by-step setup, follow the videos in [Module 1](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform).

## Runtime environment

You have three options. Pick one and stick with it for the cohort.

Local machine:

- Pros: full control, no time limits, free.
- Cons: setup is the most fiddly. Docker Desktop on Mac and Windows can be slow or finicky.

GitHub Codespaces:

- Pros: pre-configured Linux environment, no local setup.
- Cons: free tier has monthly hour limits. You may run out near the end of the cohort. GitHub Pro increases the quota.

GCP VM (Compute Engine):

- Pros: closest to a real production environment, integrates naturally with the GCS/BigQuery work later in the course.
- Cons: counts against your $300 GCP credits. Remember to stop the VM when not using it.

## Google Cloud Platform

The course uses GCP for storage (GCS), data warehouse (BigQuery), and (optionally) compute (Compute Engine, Dataproc).

New GCP accounts get $300 in free credits. This is enough for the entire course if you stop resources when you do not need them.

Common signup issues:

- Country availability: GCP free trial is not available in every country. Check the [free trial eligibility list](https://cloud.google.com/free/docs/free-cloud-features#country-restrictions).
- Card rejection (`OR_BACR2_34` or `OR_BACR2_44` errors): try a different card. Visa typically works better than Mastercard for some regions. Some prepaid cards do not work.
- Account already used: the $300 credits are one-time per Google account. If you used it before, create a new Google account.

If GCP signup is impossible for you, you can complete the course locally using Postgres and DuckDB. You can also use AWS or Azure. See "Other clouds" below.

## Service account credentials

For Terraform and the workflow tools to access GCP, you need a service account JSON key.

- Create a service account with appropriate roles (BigQuery Admin, Storage Admin, etc.) - the module 1 video walks through this.
- Download the JSON key.
- Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of the key file.

Never commit the JSON key to a public Git repository. Add it to `.gitignore` before committing.

## Other clouds (AWS, Azure, Oracle)

You can complete the course on AWS or Azure if GCP is not available to you. The videos use GCP, so you will need to translate concepts.

Common equivalents:

- GCS bucket → S3 bucket / Azure Blob.
- BigQuery → Athena, Redshift, Snowflake, or Synapse.
- Dataproc → EMR or Synapse.

There are community Slack channels for participants using alternative clouds:

- `#de-course-aws` for AWS users.

You can complete the project on any cloud regardless of what you used for the modules.

## Operating system notes

Mac (Apple Silicon, M1/M2/M3):

- Docker Desktop sometimes shows "Malware Blocked" warnings on installation. Allow it in System Settings if needed.
- Some images do not have ARM builds. Use `--platform linux/amd64` if you hit "no matching manifest" errors.
- Colima is a lighter alternative to Docker Desktop and works fine for the course.

Windows:

- Use WSL2 with Ubuntu. Native Windows Docker works but WSL2 is what the course videos demonstrate.
- Git Bash works for command-line examples in module 1.

Linux:

- Native installation works without surprises. Make sure to add your user to the `docker` group.

## Python and dependency management

The course recommends `uv` for Python dependency management. It is faster than pip/conda and handles virtual environments cleanly. See the [uv documentation](https://docs.astral.sh/uv/) for installation.

You can also use Anaconda or plain `pip + venv`. The choice does not affect the course content.

## Codespaces budget

If you are using GitHub Codespaces and run into the monthly quota:

- Stop your codespace when you are not actively using it (Codespaces bills by the hour).
- GitHub Pro (paid) increases the free quota.
- Switch to a local setup or a GCP VM for the rest of the cohort.
- Existing code is preserved when a codespace is stopped or paused. You do not lose work.
