---
title: "Curriculum"
layout: default
nav_order: 3
parent: LLM Zoomcamp
has_children: false
---

# Curriculum

The LLM Zoomcamp covers five content modules plus a final project. Each module has video lectures, code, and a homework assignment. The course is built around one central application of LLMs: RAG (retrieval-augmented generation), where you combine a knowledge base, a search engine, and an LLM to answer grounded questions.

For the canonical curriculum (videos, code, exact homework questions), see the [GitHub repository](https://github.com/DataTalksClub/llm-zoomcamp).

## Modules

[Module 1: Introduction to LLMs and RAG](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/01-intro)

- What LLMs are, how to use them through APIs, and what RAG is.
- A first end-to-end RAG implementation in Python.
- Module 1 gets two weeks because it doubles as setup and as the conceptual foundation for everything else.

[Module 2: Vector Search](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/02-vector-search)

- Embeddings and how vector search works.
- Indexing your knowledge base with a vector database.
- Comparison with keyword (text) search and hybrid search.
- The exact tooling for this module depends on the cohort sponsor; in 2026 the vector database is Quadrant.

[Module 3: Evaluation](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/03-evaluation)

- Offline evaluation of retrieval quality with classical IR metrics (hit rate, mean reciprocal rank, etc.).
- Offline evaluation of the full RAG flow using LLM-as-a-judge.
- Comparing search strategies (vector, text, hybrid) on the same dataset.

[Module 4: Monitoring](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/04-monitoring)

- Online monitoring of a deployed RAG system.
- Tracking request and response volumes, latency, and cost.
- User-feedback signals.
- The 2026 cohort uses Phoenix (open source, from Arize) instead of Grafana.

[Module 5: Best Practices](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/05-best-practices)

- Prompt patterns, document re-ranking, query rewriting, and other techniques for making a RAG system more accurate.
- The exact subset of techniques is updated each cohort.

Workshops

- One or more workshops are run alongside the modules, with their own homework. In 2026 there is a workshop with dlthub on data ingestion for LLMs.
- For workshop logistics see [Workshops]({{ '/courses/zoomcamp-logistics/workshops/' | relative_url }}).

[Final Project](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/project)

- Three weeks at the end of the cohort.
- Re-implement everything you learned, on your own knowledge base.
- See the [Project page]({{ '/courses/llm-zoomcamp/project/' | relative_url }}).

## What is not covered

To keep the course focused, several adjacent topics are intentionally out of scope. They are covered elsewhere or planned for future cohorts:

- Open-source LLMs (running, deploying, fine-tuning): covered in the separate [Open Source LLM Zoomcamp](https://github.com/DataTalksClub/open-source-llm-zoomcamp).
- Agents, agentic workflows, and MCP: ecosystem is still moving fast; possibly added in a future cohort and may appear in standalone workshops.
- Image generation, multimodal embeddings, prompt engineering as a deep topic, guardrails, distributed training: not in this course.
- Workflow orchestration of LLM applications: previous cohorts had this; removed for 2026 to focus on fundamentals.

## Pace

A typical week:

- Watch the module videos (3 to 5 hours).
- Code along and experiment (3 to 5 hours).
- Complete the homework (2 to 5 hours).

Plan for around 10 hours per week. Module 1 takes longer (two weeks), and the vector search module historically takes more time than the others.

For the final project, plan two weeks of focused work plus one week of peer review.

## What changes between cohorts

For changes specific to the current cohort, see [What's New]({{ '/courses/llm-zoomcamp/whats-new/' | relative_url }}).
