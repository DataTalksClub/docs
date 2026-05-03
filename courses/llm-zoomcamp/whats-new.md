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

- The open-source LLMs module from previous cohorts has been removed and turned into a standalone [Open Source LLM Zoomcamp](https://github.com/DataTalksClub/open-source-llm-zoomcamp), which runs in parallel and covers running, deploying, and fine-tuning open-weight models in more depth.
- Evaluation and monitoring, which used to be one module, are now two separate modules. Module 3 (Evaluation) focuses on offline metrics for retrieval and for the full RAG flow; Module 4 (Monitoring) focuses on online metrics for a deployed system.
- The orchestration module from previous cohorts has been removed. The 2026 cohort focuses on RAG fundamentals; orchestration may return in a future cohort.

Tooling

- Phoenix (open source, from Arize) replaces Grafana for monitoring.
- Quadrant joins as a sponsor and is the vector database for the vector-search module.

Sponsors

- Arize: monitoring platform; provides Phoenix.
- dlthub: ingestion library; runs a workshop on data ingestion for LLMs.
- Quadrant: vector database; appears throughout the vector-search module. New sponsor for this cohort.

What stayed

- The course is still about RAG. It is still hands-on. It still does not require GPUs and can be completed on a normal laptop with a few dollars of OpenAI credit (or zero dollars on Groq).
- Best practices module is still taught by Timur and may pick up some new techniques.
- A competition is planned again, similar in spirit to last year's math-problem challenge but with a different format.

What will likely change next year

- Some agent or agentic-search content, once tooling stabilises. The same wait-and-see approach was used before launching the original LLM Zoomcamp.

For the full curriculum, see [Curriculum]({{ '/courses/llm-zoomcamp/curriculum/' | relative_url }}). For environment setup, see [Environment Setup]({{ '/courses/llm-zoomcamp/environment-setup/' | relative_url }}).
