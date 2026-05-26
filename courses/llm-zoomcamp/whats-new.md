---
title: "What's New"
layout: default
nav_order: 5
parent: LLM Zoomcamp
has_children: false
---

# What's New

Notable changes for the current cohort. Older changes are folded into the curriculum.

## 2026

Course structure

- All core modules have been re-recorded to account for changes in LLM application development over the last two years.
- The course now covers agents, not only RAG. Module 2 introduces agents, function calling, the agentic loop, and how agents differ from a fixed RAG pipeline.
- Orchestration is back as a dedicated module. Module 3 covers AI orchestration with Kestra.
- Evaluation and monitoring are separate modules. Evaluation is still RAG-focused, with retrieval metrics and LLM-as-a-judge for answer quality. Monitoring focuses on a running application.
- The open-source LLMs module from previous cohorts is no longer part of the main flow.

Tooling

- The OpenAI examples use the Responses API instead of the older chat completions API.
- The course uses newer OpenAI models in examples and evaluation code.
- The FAQ dataset now comes directly from the DataTalks.Club FAQ website.
- Kestra is used for orchestration.
- PostgreSQL and Grafana are used for monitoring.

What stayed

- The simple FAQ assistant remains the running example.
- The lesson flow is still practical and incremental: build the basic pipeline first, then add search, agents, orchestration, evaluation, monitoring, and best practices.
- RAG remains the main application pattern and the center of evaluation.
- The course is still hands-on. It still does not require GPUs and can be completed on a normal laptop with a few dollars of OpenAI credit, or with a compatible alternative provider.

For the full curriculum, see [Curriculum]({{ '/courses/llm-zoomcamp/curriculum/' | relative_url }}). For environment setup, see [Environment Setup]({{ '/courses/llm-zoomcamp/environment-setup/' | relative_url }}).
