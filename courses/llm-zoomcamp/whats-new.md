---
title: "What's New"
layout: default
nav_order: 5
parent: LLM Zoomcamp
has_children: false
---

# Changes

Notable changes for the current cohort. The previous version of the course page described the 2025 flow, so this page focuses on what changed for 2026.

## 2026

Course structure

- Module 1 is now Agentic RAG. It combines the RAG introduction with function calling and the agentic loop.
- Agents are no longer a separate "Module A" after the dlt workshop. They are part of the main course flow from the first module.
- Module 2 is now dedicated to Vector Search. It covers embeddings, semantic search, minsearch, sqlitesearch, PGVector, and optional ONNX-based embedders.
- Module 3 is a new Orchestration module with Kestra. It covers context engineering, AI Copilot, RAG workflows, agentic workflows, multi-agent systems, and production considerations.
- The dlt workshop remains in the 2026 course, now focused on pulling LLM traces from a monitoring service and preparing them for analytics.
- Evaluation moved from Module 3 in 2025 to Module 4 in 2026. It now covers search evaluation, RAG answer evaluation, and the basics of agent evaluation.
- Monitoring is now a full Module 5. In 2025, the main course page ended after evaluation. In 2026, monitoring is part of the main sequence.
- Best Practices is Module 6 and End-to-End Project Example is Module 7. These are optional modules based on older material, but they are included in the 2026 syllabus as useful follow-up content.
- The capstone project remains the final requirement for certificate eligibility.

Tooling

- The course recommends modern Python and `uv` for dependency management.
- Docker is more central because several modules need services such as PostgreSQL, PGVector, and monitoring dashboards.
- The FAQ dataset now comes directly from the DataTalks.Club FAQ website.
- Kestra is used for orchestration.
- PostgreSQL, Streamlit, and Grafana are used for monitoring.

What stayed

- The course is still practical and incremental.
- RAG remains the main application pattern.
- The FAQ assistant remains an important running example.
- The course still does not require a GPU.
- You can still complete the course on a normal laptop with a few dollars of OpenAI credit, or with a compatible alternative provider.

For the full curriculum, see [Curriculum]({{ '/courses/llm-zoomcamp/curriculum/' | relative_url }}). For environment setup, see [Environment Setup]({{ '/courses/llm-zoomcamp/environment-setup/' | relative_url }}).
