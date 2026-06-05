---
title: "Curriculum"
layout: default
nav_order: 3
parent: LLM Zoomcamp
has_children: false
---

# Curriculum

The LLM Zoomcamp covers the core flow for building LLM applications: RAG, agents, vector search, orchestration, evaluation, monitoring, best practices, and a capstone project. Each module has video lectures, code, and usually a homework assignment. The course is built around practical assistants that start from simple RAG and grow into more production-style applications.

For the canonical curriculum (videos, code, exact homework questions), see the [GitHub repository](https://github.com/DataTalksClub/llm-zoomcamp).

## Modules

[Module 1: Agentic RAG](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/01-agentic-rag)

- What LLMs and RAG are, and why LLMs need external context.
- A simple FAQ RAG pipeline with keyword search and minsearch.
- Prompt construction, calling an LLM, and wiring search plus prompts into a reusable RAG pipeline.
- Persistent keyword search with sqlitesearch.
- Function calling and the agentic loop, where the LLM decides when and what to search.
- The FAQ dataset comes directly from the DataTalks.Club FAQ website.

[Module 2: Vector Search](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/02-vector-search)

- Semantic search with embeddings.
- Generating embeddings for the FAQ dataset.
- Vector search with numpy and minsearch.
- RAG with vector search instead of keyword search.
- Persistent vector search with sqlitesearch and PGVector.
- Optional ONNX-based embedders for lightweight deployments.

[Module 3: Orchestration](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/03-orchestration)

- AI workflow orchestration with Kestra.
- Context engineering and why generic AI assistants can produce unreliable workflows.
- Using Kestra's AI Copilot to generate and refine flows.
- RAG workflows, agentic workflows, and multi-agent systems.
- Production considerations: cost, security, observability, and when to use each approach.

[Workshop: Data Ingestion](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/cohorts/2026/workshops/dlt.md)

- Pulling LLM traces from a monitoring service.
- Preparing trace data for analytics with dlt.
- This workshop runs between orchestration and evaluation in the 2026 syllabus.

[Module 4: Evaluation](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/04-evaluation)

- Systematic evaluation for search, RAG, and agent systems.
- Generating ground truth data with an LLM.
- Offline evaluation of retrieval quality with Hit Rate and MRR.
- Search parameter tuning based on evaluation metrics.
- Evaluating answer quality with LLM-as-a-judge.
- Capturing final answers and tool-call trajectories for agent evaluation.

[Module 5: Monitoring](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/05-monitoring)

- Online monitoring of a deployed RAG system.
- Building a Streamlit chat app.
- Tracking LLM call metrics, latency, and cost.
- PostgreSQL for storing conversations and feedback.
- User-feedback signals and built-in LLM-as-a-judge checks.
- Streamlit and Grafana dashboards.
- Docker Compose for running the app, database, and dashboards together.

[Module 6: Best Practices](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/06-best-practices)

- Optional module recorded in 2024.
- Hybrid search with Elasticsearch.
- Document reranking with Reciprocal Rank Fusion.
- Hybrid search with LangChain.
- The techniques are still relevant, but some code uses older libraries and approaches.

[Module 7: End-to-End Project Example](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/07-project-example)

- Optional module recorded in 2024.
- A complete project example: a fitness assistant built with LLMs.
- Search, evaluation, API, monitoring, and Docker containerization in one project.
- Chunking strategies for longer text sources.

[Capstone Project](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/project.md)

- Three weeks at the end of the cohort.
- Build a complete RAG application on your own knowledge base.
- Implement retrieval, answer generation, evaluation, a user-facing interface, and monitoring or feedback loops.
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

For the capstone project, plan two weeks of focused work plus one week of peer review.

## What changes between cohorts

For changes specific to the current cohort, see [What's New]({{ '/courses/llm-zoomcamp/whats-new/' | relative_url }}).
