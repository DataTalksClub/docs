---
title: "Project"
layout: default
nav_order: 6
parent: LLM Zoomcamp
has_children: false
---

# Project

For the cross-course logistics (deadlines, peer review, certification mechanics), see [Final Project (Zoomcamp Logistics)]({{ '/courses/zoomcamp-logistics/project/' | relative_url }}).

This page covers what is specific to the LLM Zoomcamp.

## Project scope

Build a working RAG application on a knowledge base of your choice. Over two to three weeks, you apply modules 1 to 5 to your own data.

Your project should:

- Pick a domain.
- Ingest a knowledge base.
- Index it for retrieval.
- Wire up an LLM.
- Evaluate retrieval and the end-to-end RAG flow.
- Ideally include some monitoring.

Past projects from previous cohorts give a sense of the expected scope. Examples include a recipe search assistant, a fitness assistant, and a reference lookup tool for music notation. Most are modest in scope but cleanly built and well-documented.

## Project structure

The LLM Zoomcamp has a single project at the end of the cohort. The window typically runs for two weeks of submission, then one week of peer review. You complete three peer reviews of other participants' projects.

You can start working on the project before the window opens. The platform form opens once the cohort lead releases it.

## Tech stack flexibility

You are not restricted to the technologies covered in the course. Use any LLM provider, vector database, framework, or programming language.

Caveats:

- Document your choices clearly in the README. Reviewers may not know your stack.
- Make the project reproducible. If a reviewer cannot run it (or at least understand how it would run), you lose reproducibility points.
- If you write the project in JavaScript, Go, or anything other than Python, give explicit setup instructions. Python is the only stack you can assume reviewers have ready.

## Knowledge base / dataset

You choose the knowledge base. It can be in any language, including non-English. The README must still be in English so peer reviewers can evaluate the project. Pick a domain you find interesting because you will work with it for several weeks.

Avoid:

- Any dataset the course uses in its lectures or homework. Choose something new so the project shows your own work.
- Trivially small or toy data that does not exercise retrieval meaningfully.

## Required components

Every LLM Zoomcamp project must include:

- An ingestion path that turns your raw knowledge base into something searchable.
- A retrieval system (text search, vector search, or hybrid).
- An LLM-powered answering layer that uses the retrieved documents.
- A retrieval evaluation: which strategy you tried and how it scored.
- An end-to-end evaluation of the full RAG flow.
- Some form of interface that a reviewer can use, even if it is just a Python script or a notebook. A web UI (Streamlit, Gradio, Flask) is welcome but not required.

The rubric does not require these nice-to-haves:

- Monitoring with Grafana, PostgreSQL, or another tool.
- A deployed live system.

## Frameworks

The course teaches RAG without frameworks so that you understand the underlying concepts. For your project, frameworks are allowed. You can use LangChain, LlamaIndex, Haystack, or similar tools. Document why you chose the framework and what it gives you.

## Evaluation criteria

Each course defines its own rubric. The platform shows the exact criteria when you review or are reviewed.

Common criteria for LLM Zoomcamp projects:

- Problem description and motivation.
- Knowledge base preparation and ingestion.
- Retrieval setup and evaluation of retrieval quality.
- LLM integration and end-to-end RAG flow.
- End-to-end evaluation.
- Reproducibility (can a reviewer run the project from your README).
- Documentation quality.
- Bonus: interface, monitoring, deployment, advanced techniques.

The full rubric for the current cohort is on the course platform under the project window.

## Past projects

Use past projects to calibrate scope:

- Browse past LLM Zoomcamp cohorts on the [course platform](https://courses.datatalks.club/).
- The 2024 cohort's project gallery is a good starting reference for scope.

## Certification

Submit a passing project on time and complete your peer reviews. That is the requirement to graduate.

What is not required:

- Homework scores. Homework is for learning.
- Live session attendance.
- Leaderboard points beyond the project.

The earliest you can receive your certificate is after the peer-review deadline. For when the certificate is issued and how to add it to LinkedIn, see [Certification (Zoomcamp Logistics)]({{ '/courses/zoomcamp-logistics/certification/' | relative_url }}).

## Portfolio focus

Treat the project as a portfolio piece with a meaningful repository name such as `recipes-rag-assistant`, not `homework-final`. Include a clear README. Past graduates have used these projects in job applications and interviews.
