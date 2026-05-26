---
title: "Curriculum"
layout: default
nav_order: 3
parent: LLM Zoomcamp
has_children: false
---

# Curriculum

The LLM Zoomcamp covers the core flow for building LLM applications: RAG, agents, orchestration, evaluation, monitoring, best practices, and a final project. Each module has video lectures, code, and a homework assignment. The course is built around a practical FAQ assistant that starts as a simple RAG system and grows into a more production-style application.

For the canonical curriculum (videos, code, exact homework questions), see the [GitHub repository](https://github.com/DataTalksClub/llm-zoomcamp).

## Modules

[Module 1: RAG and Vector Search](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/01-rag)

- What LLMs and RAG are.
- A simple FAQ RAG pipeline with keyword search.
- Vector search with embeddings, minsearch, sqlitesearch, and pgvector.
- The FAQ dataset comes directly from the DataTalks.Club FAQ website.

[Module 2: Agents](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/02-agents)

- How agents differ from a fixed RAG pipeline.
- Function calling with the OpenAI Responses API.
- Building the agentic loop from scratch.
- Agent frameworks and how they relate to the course implementation.

[Module 3: Orchestration](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/03-orchestration)

- AI workflow orchestration with Kestra.
- Turning the application flow into repeatable, scheduled workflows.

[Module 4: Evaluation](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/04-evaluation)

- Offline evaluation of retrieval quality with classical IR metrics.
- Offline evaluation of the full RAG flow using cosine similarity and LLM-as-a-judge.
- The module is still centered on RAG evaluation, with some agent evaluation material.

[Module 5: Monitoring](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/05-monitoring)

- Online monitoring of a deployed RAG system.
- Tracking request and response volumes, latency, and cost.
- User-feedback signals.
- PostgreSQL for storing conversations and feedback.
- Grafana for monitoring dashboards.

[Module 6: Best Practices](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/06-best-practices)

- Hybrid search, document re-ranking, LangChain, and other techniques for making a RAG system more accurate.
- The exact subset of techniques is updated each cohort.

[Module 7: End-to-End Project Example](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/07-project-example)

- A complete example application.
- Retrieval, evaluation, interface, monitoring, and containerization in one project.

[Final Project](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/project)

- Three weeks at the end of the cohort.
- Re-implement everything you learned, on your own knowledge base.
- See the [Project page]({{ '/courses/llm-zoomcamp/project/' | relative_url }}).

## What is not covered

To keep the course focused, several adjacent topics are intentionally out of scope. They are covered elsewhere or planned for future cohorts:

- Open-source LLMs (running, deploying, fine-tuning).
- MCP and deeper agentic frameworks: the course covers agents from first principles, but not every current framework.
- Image generation, multimodal embeddings, prompt engineering as a deep topic, guardrails, distributed training: not in this course.

## Pace

A typical week:

- Watch the module videos (3 to 5 hours).
- Code along and experiment (3 to 5 hours).
- Complete the homework (2 to 5 hours).

Plan for around 10 hours per week. Module 1 takes longer (two weeks), and the vector search module historically takes more time than the others.

For the final project, plan two weeks of focused work plus one week of peer review.

## What changes between cohorts

For changes specific to the current cohort, see [What's New]({{ '/courses/llm-zoomcamp/whats-new/' | relative_url }}).
