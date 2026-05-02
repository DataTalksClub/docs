---
title: "Q&A"
layout: default
nav_order: 9
parent: Data Engineering Zoomcamp
has_children: false
---

# Questions and Answers

DE-specific questions. For general zoomcamp logistics (joining, deadlines, certificate, project flow), see [Zoomcamp Logistics]({{ '/courses/zoomcamp-logistics/' | relative_url }}). For module-specific and technical issues, check the [Data Engineering Zoomcamp FAQ](https://datatalks.club/faq/data-engineering-zoomcamp.html).

## Why Google Cloud Platform instead of AWS or Azure?

Three reasons:

- $300 free credits for new accounts. AWS's free tier is limited and many services exclude the free tier; Azure's $200 expires after 30 days. GCP gives the most generous credits with the fewest service restrictions.
- No service limitations during the free trial. The course exercises all run on the free tier.
- Historical compatibility. dbt worked better with BigQuery when the course launched, and the curriculum was built around the GCP stack.

For the project, you can use any cloud. See [Environment Setup]({{ '/courses/data-engineering-zoomcamp/environment-setup/' | relative_url }}) for notes on alternatives.

## Can I get a DE job without a degree?

Short answer: yes.

Multiple success stories from past cohorts:

- Students who landed jobs through the course network.
- Bruno (no formal degree, now Senior DE at US companies).
- Career switchers from analytics, support, and unrelated fields.

What works:

- A strong portfolio of projects.
- Networking (learning in public helps).
- Consistency and going beyond the basics.

## Is 31 (or 35, or 40) too old to start?

No. In data engineering, the industry cares about skills, not age. In Germany, many DEs start their careers at 30+ after extended education. Career switchers from other engineering, finance, or analytics backgrounds are common.

Tip: do not put your age on your CV to avoid unconscious bias.

## How much time does the course take?

- Two weeks for Module 1, one week each for modules 2 to 6.
- Two to three weeks for the project.
- Plan for 10 to 15 hours per week.

See [Prerequisites]({{ '/courses/data-engineering-zoomcamp/prerequisites/' | relative_url }}) for details.

## What is NOT covered (the other 80%)?

The course covers the essential 20% that handles 80% of real-world DE work. Areas the course does not cover that you will encounter in real DE jobs:

- Polars: a modern pandas alternative for data manipulation.
- Delta Lake / Apache Iceberg: advanced table formats for data lakes.
- Snowflake / Redshift / ClickHouse: other data warehouses (the course uses BigQuery).
- dbt incremental models: optimizing dbt for large datasets.
- Apache Flink: real-time streaming. Module 6 introduces it but only briefly.
- Data governance and catalogs: DataHub, Unity Catalog.
- Databricks: increasingly common in industry but not in the course.

The remaining 80% comes with experience in your first DE role.

## Final thoughts

Data engineering is a field that's "5 feet deep and 50 miles wide."

- Ask questions in Slack (after checking the FAQ and the Q+A in this section).
- Learn in public.
- Help your peers.
- Do not get discouraged. It gets challenging.
- You got this.
