---
title: "Curriculum"
layout: default
nav_order: 3
parent: Data Engineering Zoomcamp
has_children: false
---

# Curriculum

The Data Engineering Zoomcamp covers six modules over seven weeks plus the final project. Each module has video lectures, reading material, and a homework assignment.

For the canonical curriculum (videos, code, exact homework questions), see the [GitHub repository](https://github.com/DataTalksClub/data-engineering-zoomcamp).

## Modules

[Module 1: Containerization and Infrastructure as Code](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform)

- Docker and Postgres.
- Setting up a development environment locally and on GCP.
- Terraform for infrastructure provisioning.
- Module 1 gets two weeks because environment setup can be the trickiest part.

[Module 2: Workflow Orchestration](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/02-workflow-orchestration)

- Workflow orchestration with Kestra.
- Building data pipelines that schedule, retry, and backfill.
- Loading data to Google Cloud Storage and BigQuery.

Workshop: Data Ingestion with dlt

- Slotted between modules. Hands-on workshop on the dlt library for ingestion.
- Has its own homework. See [Workshops]({{ '/courses/zoomcamp-logistics/workshops/' | relative_url }}) for the workshop logistics.

[Module 3: Data Warehouse](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/03-data-warehouse)

- BigQuery as a data warehouse.
- Partitioning and clustering for performance.
- Cost optimization.

[Module 4: Analytics Engineering](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/04-analytics-engineering)

- dbt for analytics engineering.
- Building staging, intermediate, and mart models.
- Testing and documentation.
- Connecting BigQuery to a dashboard.

[Module 5: Batch Processing](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/05-batch)

- Apache Spark fundamentals.
- PySpark with the NYC taxi dataset.
- Running on Google Dataproc.

[Module 6: Streaming](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/06-streaming)

- Apache Kafka.
- Stream processing with Kafka and Flink.
- Schema registry and data serialization.

[Final Project](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/projects)

- Three weeks at the end of the cohort.
- Build an end-to-end pipeline of your choice.
- See the [Project page]({{ '/courses/data-engineering-zoomcamp/project/' | relative_url }}).

## What changes between cohorts

Most modules are stable across cohorts. Notable past changes:

- 2023: Mage replaced Prefect as the workflow orchestrator.
- 2025: Kestra replaced Mage.
- 2026: New workshop on dlt continues; some modules use updated tooling.

If a video references a tool you do not see in the current code, check the cohort folder ([cohorts/2026/](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/cohorts/2026)) for the current version.

## Pace

A typical week:

- Watch the module videos (3 to 5 hours).
- Work through the code examples (3 to 5 hours).
- Complete the homework (2 to 5 hours).

Plan for 10 to 15 hours per week. Module 1 takes more (two weeks instead of one).

For the final project, plan 2 to 3 weeks of focused work.
