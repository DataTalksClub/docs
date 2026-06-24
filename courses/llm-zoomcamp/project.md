---
title: "Project"
layout: default
nav_order: 6
parent: LLM Zoomcamp
has_children: false
---

# Project

For the cross-course logistics (deadlines, peer review, certification mechanics), see [Final Project (Zoomcamp Logistics)]({{ '/courses/zoomcamp-logistics/project/' | relative_url }}).

For the platform UI (where to submit, commit ID, project gallery), see [Course Management Platform: Projects]({{ '/courses/course-management-platform/projects/' | relative_url }}).

This page covers what is specific to the LLM Zoomcamp: what kind of project to build, how to choose a good idea, and what the reviewers expect to see.

## Project scope

Build a working LLM-powered application on a knowledge base of your choice. In most projects, this means a RAG application. You apply modules 1 to 5 to your own data and show that you can build, evaluate, and document an end-to-end system.

Your project should:

- Pick a domain.
- Ingest a knowledge base.
- Index it for retrieval.
- Wire up an LLM.
- Evaluate retrieval and the end-to-end RAG flow.
- Ideally include some monitoring.

Past projects from previous cohorts give a sense of the expected scope. Examples include a recipe search assistant, a fitness assistant, and a reference lookup tool for music notation. Most are modest in scope but cleanly built and well-documented.

## Choosing a project idea

A good project starts with a real question someone would ask, not with a tool choice. Before deciding on a stack, write down:

- Who the user is.
- What they need help with.
- What knowledge base the assistant will use.
- What a useful answer should look like.
- How you will tell whether the answer is good.

Good project ideas usually have these properties:

- The domain is specific enough that generic ChatGPT would not be enough.
- The knowledge base is available, clean enough to process, and large enough to make retrieval meaningful.
- The answers can be checked against the source documents.
- The scope fits into a few weeks.
- The README can explain the problem to someone outside the domain.

Avoid vague ideas like "a chatbot for documents" unless you make the user, documents, and task concrete. For example:

- Instead of a generic PDF chatbot, build an assistant for a specific set of product manuals, public policies, internal notes, or course materials.
- Instead of "medical assistant", build a tool that answers questions from a public clinical guideline dataset and clearly cites sources.
- Instead of "career assistant", build a tool that searches a curated set of job descriptions and explains which skills are repeatedly requested.

## Using the AI Engineering Field Guide

The [AI Engineering Field Guide]({{ '/courses/llm-zoomcamp/resources/#ai-engineering-field-guide' | relative_url }}) is a good source of project ideas. Its [home-assignments section](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/interview/questions/06-home-assignments.md) collects take-home assignments from 100+ company GitHub repositories.

Do not copy an assignment blindly. Use it as a prompt for a project you can finish and explain:

- Pick an assignment that sounds like work you would like to do in a real AI engineering role.
- Identify the core user problem in the assignment.
- Replace any missing or proprietary data with public data you can share.
- Adapt the task to the LLM Zoomcamp rubric: ingestion, retrieval, LLM answer generation, evaluation, and reproducibility.
- Keep the scope small enough that you can finish it, but real enough that it is useful as a portfolio piece.

The Field Guide is especially useful if you want the project to support your job search. Look at assignments from companies or roles you care about, then build a smaller version that demonstrates the same skills.

## More project inspiration

These write-ups show examples of finished AI engineering and agentic projects. Use them for scope, architecture ideas, and problem framing:

- [9 Real-Life AI Projects from AI Engineering Buildcamp Graduates](https://alexeyondata.substack.com/p/9-real-life-ai-projects-from-ai-engineering)
- [5 ideas for AI agents and OpenAI's hidden skills](https://alexeyondata.substack.com/p/5-ideas-for-ai-agents-and-openais)

## Knowledge base / dataset

You choose the knowledge base. It can be in any language, including non-English. The README must still be in English so peer reviewers can evaluate the project. Pick a domain you find interesting because you will work with it for several weeks.

Avoid:

- Any dataset the course uses in its lectures or homework. Choose something new so the project shows your own work.
- Trivially small or toy data that does not exercise retrieval meaningfully.

Strong sources for a knowledge base:

- Documentation for an open-source project.
- Public policy, legal, or government documents.
- Product manuals or technical support pages.
- Public datasets with text fields, reviews, complaints, or Q&A.
- Your own notes, if you can make enough of them public for reviewers.

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

## Tech stack flexibility

You are not restricted to the technologies covered in the course. Use any LLM provider, vector database, framework, or programming language.

Caveats:

- Document your choices clearly in the README. Reviewers may not know your stack.
- Make the project reproducible. If a reviewer cannot run it, or at least understand how it would run, you lose reproducibility points.
- If you write the project in JavaScript, Go, or anything other than Python, give explicit setup instructions. Python is the only stack you can assume reviewers have ready.

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

- [LLM Zoomcamp 2025 project gallery](https://courses.datatalks.club/llm-zoomcamp-2025/projects)
- [LLM Zoomcamp 2024 project gallery](https://courses.datatalks.club/llm-zoomcamp-2024/projects)
- Browse other cohorts on the [course platform](https://courses.datatalks.club/).
- Use the project gallery flow described in [Course Management Platform: Projects]({{ '/courses/course-management-platform/projects/' | relative_url }}).

## Portfolio focus

Treat the project as a portfolio piece with a meaningful repository name such as `recipes-rag-assistant`, not `homework-final`. Include a clear README. Past graduates have used these projects in job applications and interviews.

A few habits make the difference between finishing the course and building something employers notice:

- Start building from day one. Do not wait for the project window to open. Read the project guidelines at the start, decide what you want to build, and apply each module to your own project as you learn it. Putting concepts into practice immediately beats going through the material passively.
- Build more than one project. Everyone finishes the course with a RAG app on the same course dataset, so that alone does not stand out. Build several projects on data and problems you chose yourself. A small portfolio of varied projects, such as a RAG app, an agent, or something in a different domain, is far stronger than a single one.
- Make them your own. The strongest projects solve a problem you actually have, on data you picked, cleaned, and structured yourself. That work is what shows your skills.
