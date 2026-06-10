---
title: "Resources"
layout: default
nav_order: 8
parent: Data Engineering Zoomcamp
has_children: false
---

# Resources

Course-specific links for the Data Engineering Zoomcamp. For general zoomcamp logistics, see [Zoomcamp Logistics]({{ '/courses/zoomcamp-logistics/' | relative_url }}).

## GitHub Repository

The repository is your primary navigation tool throughout the course.

[github.com/DataTalksClub/data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp)

<img src="{{ '/assets/images/data-engineering-zoomcamp/launch/github-repo.jpg' | relative_url }}" alt="GitHub repository" width="80%">

How to use it:

1. Start in the module folder you are working on.
2. Read the README in that folder for an overview.
3. Follow the links to video lectures.
4. Complete the homework assignment.
5. Check the cohort folder for any cohort-specific materials.

Repository structure (one folder per module):

- [`01-docker-terraform/`](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform) - Docker, PostgreSQL, Terraform, Google Cloud setup.
- [`02-workflow-orchestration/`](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/02-workflow-orchestration) - Workflow orchestration with Kestra.
- [`03-data-warehouse/`](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/03-data-warehouse) - Data warehousing with BigQuery.
- [`04-analytics-engineering/`](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/04-analytics-engineering) - Analytics engineering with dbt.
- [`05-batch/`](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/05-batch) - Batch processing with PySpark.
- [`06-streaming/`](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/06-streaming) - Stream processing with Kafka and Flink.
- [`projects/`](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/projects) - Final project guidelines.

Cohort folders contain materials specific to each edition:

- [`cohorts/2026/`](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/cohorts/2026)
- [`cohorts/2025/`](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/cohorts/2025)
- [`cohorts/2024/`](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/cohorts/2024)
- [`cohorts/2023/`](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/cohorts/2023)
- [`cohorts/2022/`](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/cohorts/2022)

The 2026 cohort folder contains per-module subfolders, the cohort [README.md](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2026/README.md), and the [project guidelines](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2026/project.md).

## YouTube

Subscribe to the [DataTalks.Club YouTube channel](https://www.youtube.com/@DataTalksClub) for new content.

<img src="{{ '/assets/images/data-engineering-zoomcamp/youtube.png' | relative_url }}" alt="YouTube channel" width="80%">

There are two playlist types:

Main playlist (pre-recorded lectures, the core curriculum):

- [Data Engineering Zoomcamp main playlist](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)

Cohort playlists include live sessions and extra material:

- [2025 cohort](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJZdpLpRHp7dg6EOx828q6y)
- [2024 cohort](https://www.youtube.com/playlist?list=PL3MmuxUbc_hKihpnNQ9qtTmWYy26bPrSb)
- [2023 cohort](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJjEePXIdE-LVUx_1ZZjYGW)
- [2022 cohort](https://www.youtube.com/playlist?list=PL3MmuxUbc_hKVX8VnwWCPaWlIHf1qmg8s)

Cohort playlists are supplementary, so focus on the main playlist first. Explore the cohort playlist for extra insights.

## Course Platform

The [course management platform](https://courses.datatalks.club/de-zoomcamp-2026/) is where you submit homework, track your progress, and submit your project.

<img src="{{ '/assets/images/data-engineering-zoomcamp/launch/course-platform.jpg' | relative_url }}" alt="Course platform interface" width="80%">

For the platform UI in detail, see [Course Management Platform]({{ '/courses/course-management-platform/' | relative_url }}).

## Slack

DE-specific channel: [#course-data-engineering](https://app.slack.com/client/T01ATQK62F8/C01FABYF2RG).

Use this channel for all DE-specific questions, homework discussion, and project Q+A. For all DTC Slack channels, see the [Slack guide]({{ '/general/slack/' | relative_url }}).

## Telegram

DE announcements channel: [t.me/dezoomcamp](https://t.me/dezoomcamp). It is announcement-only, so questions are not monitored there.

<img src="{{ '/assets/images/data-engineering-zoomcamp/telegram.png' | relative_url }}" alt="Telegram channel" width="80%">

## FAQ

The [Data Engineering Zoomcamp FAQ](https://datatalks.club/faq/data-engineering-zoomcamp.html) contains answers to module-specific and technical questions from previous cohorts. Check it before posting in Slack.

## Community Notes

Past cohort participants contribute notes that summarize the course content. They live in the course repository (typically under a `notes/` or per-module folder). Browse the [GitHub repo](https://github.com/DataTalksClub/data-engineering-zoomcamp) and look for community-contributed notes referenced from each module's README.

## Course Dataset

Throughout the course you work with the New York City taxi trips dataset.

<img src="{{ '/assets/images/data-engineering-zoomcamp/launch/taxi-data.jpg' | relative_url }}" alt="NYC Taxi Trip Data" width="80%">

Why this dataset:

- Messy and imperfect. You will encounter missing values, inconsistent formats, and quality issues.
- Outliers and anomalies. Negative fares, impossible distances, trips from the future.
- Requires cleaning. You learn to validate, filter, and transform.
- Sufficiently large. Big enough to justify proper engineering, small enough to remain manageable.
- Evolving schema. The NYC TLC has modified the structure over time, so you learn to handle schema changes.
- Well-documented. The [official documentation](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) provides data dictionaries.
- Free and publicly available.

Data format:

- Historical data (2019-2021): CSV files in the [DataTalksClub mirror repository](https://github.com/DataTalksClub/nyc-tlc-data). The course uses these for some modules to demonstrate CSV-to-Parquet conversion.
- Recent data (2025+): Parquet files directly from the [official NYC TLC Trip Record Data page](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).

If you get a 403 Forbidden error when using the original `s3.amazonaws.com/nyc-tlc/...` URLs, NYC TLC has changed the source. Use the DataTalksClub mirror or the official NYC TLC parquet files instead.
