---
title: "Dataset"
layout: default
nav_order: 4
parent: Resources
has_children: false
---

# Course Dataset

Throughout the course, you'll work with a real-world dataset: New York City taxi trips from 2019-2020.

<img src="{{ '/assets/images/data-engineering-zoomcamp/launch/taxi-data.jpg' | relative_url }}" alt="NYC Taxi Trip Data" width="80%">

## About the Dataset

The NYC Taxi Trip dataset includes trips with pickup/dropoff locations that you'll analyze using various data engineering tools. This dataset is ideal for learning data engineering because it represents a genuinely real-world scenario, not a simplified academic example.

### Why This Dataset

We specifically chose this dataset because it mirrors the challenges you'll face in actual data engineering work:

- Messy and imperfect: Real data is never clean. You'll encounter missing values, inconsistent formats, and data quality issues that require attention.

- Outliers and anomalies: The data contains unrealistic values (negative fares, impossible distances, trips from the future) that you need to identify and handle.

- Requires cleaning: You'll learn to validate, filter, and transform data before using it for analysis or modeling.

- Sufficiently large: The dataset is big enough to justify proper engineering techniques (batching, optimized storage, efficient processing), but not so large that it becomes unmanageable for learning.

- Evolving schema: Over time, the NYC TLC has modified the data structure, teaching you to handle schema changes and versioning.

- Well-documented: The [official documentation](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) provides data dictionaries and explanations, though you'll still need to explore and understand the data yourself.

- Free and publicly available: No API keys, permissions, or special access required.

Working with this dataset prepares you for the actual challenges of data engineering, where the data is rarely perfect and always requires thoughtful handling.

## Data Format

The NYC taxi data is provided in Parquet format. Parquet is a columnar storage file format that provides efficient compression and encoding schemes, making it ideal for data engineering workflows.

You'll work with two sources:

- Historical data (2019-2021): For learning data transformation, we demonstrate how to read CSV files and convert them to Parquet. The original CSV files are available in the [backup repository](https://github.com/DataTalksClub/nyc-tlc-data).

- Recent data (2025+): You'll read Parquet files directly from the [official NYC TLC Trip Record Data page](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page). This reflects real-world workflows where you consume data in modern formats.

## What You'll Do With It

Across the modules, you'll:

- Ingest the data into various storage systems
- Transform and clean the data
- Build batch and streaming pipelines
- Create analytics and visualizations

This hands-on approach ensures you gain practical experience with actual data, not just theoretical concepts.
