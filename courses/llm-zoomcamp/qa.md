---
title: "Q&A"
layout: default
nav_order: 9
parent: LLM Zoomcamp
has_children: false
---

# Questions and Answers

LLM-specific questions about course scope and philosophy. For general zoomcamp logistics (joining, deadlines, certificate, project flow), see [Zoomcamp Logistics]({{ '/courses/zoomcamp-logistics/' | relative_url }}). For module-specific and technical issues, check the [LLM Zoomcamp FAQ](https://datatalks.club/faq/llm-zoomcamp.html).

## Why is there no agents module?

Agent tooling is moving too fast to record stable course content. The same wait-and-see approach was used before launching the original LLM Zoomcamp - LLMs themselves had to stabilise before the course made sense. Agents will likely show up in a future cohort once the ecosystem is more settled.

In the meantime, expect occasional standalone workshops on agentic workflows. A separate AI Dev Tools Zoomcamp will cover building agents as part of its curriculum.

## Why is RAG still the focus in 2026?

A year ago RAG was the most common LLM application in the wild. Today many providers offer RAG out of the box, but it remains the strongest illustrative use case for teaching the underlying concepts: how to combine retrieval, prompting, and evaluation in a real system. Skills you build for RAG transfer to most other LLM applications.

## Why no MCP, no LangGraph, no agentic frameworks?

Same reason as agents: the surface area is changing weekly. The course teaches RAG without any framework so that you understand the mechanics. Once you do, picking up MCP or LangGraph or whatever the framework of the month is takes a fraction of the time it would otherwise.

LangChain is the one exception - it has shown up in the best-practices module before (for document re-ranking) and may again, depending on the instructor's choice for the cohort.

## Why no fine-tuning, distributed training, or building our own LLM?

This course is about LLM engineering, not LLM internals. LLMs are treated as black boxes you call through an API.

Building your own LLM from scratch is not on the roadmap and there are already strong courses on that elsewhere.

## How is this different from the ML Zoomcamp?

ML Zoomcamp covers classical machine learning. It looks under the hood: how models learn, how to choose between regression and classification approaches, how to evaluate. LLM Zoomcamp does not look under the hood. It teaches you to build applications on top of hosted LLMs, including evaluation and monitoring of those applications.

If you are deciding between the two: take ML Zoomcamp if you want to understand machine learning. Take LLM Zoomcamp if you want to build with LLMs.

## How is this different from the MLOps Zoomcamp?

MLOps Zoomcamp covers the operational lifecycle of ML models: experiment tracking, model registry, deployment, monitoring, retraining. LLM Zoomcamp's monitoring module covers similar ground but for LLMs (request volume, latency, cost, response quality), without the training-side concerns.

## Should I retake the course if I did it last year?

The application focus is the same (RAG), but tooling and modules have changed: the open-source LLMs module is gone, evaluation and monitoring are now two modules, monitoring uses Phoenix instead of Grafana, the vector database is updated. There will also be a new competition. Worth retaking if you want to refresh and re-implement with current tools.

## I have a strong background in RAG already. Will I learn anything new?

Hard to say without knowing your level. The pragmatic answer: skim module 1, see if it feels familiar, and if so jump straight to the project. Identify gaps as you build, then go back and fill just those.

## Can I get a job after the course?

The course gives you the engineering skills companies want. Whether you land a job depends on what you do outside the course: build projects, learn in public, share your work, apply.

There is anecdotal evidence of past graduates landing AI roles after the course but no clean data on conversion rates. Treat it as one strong piece of a portfolio, not a guaranteed path.

If you are a data scientist who does not yet work with LLMs, this course is one of the strongest single ways to extend your profile - many DS roles now expect at least RAG-level familiarity.

## What if I have no LLM experience and am career-switching?

Possible, with effort. The course assumes you can program. If you can, the LLM-specific concepts are accessible in a few weeks. If you cannot program yet, build programming basics first; the course is genuinely hard without them.

## Final thoughts

LLM engineering is mostly the engineering you already know, with a few new patterns layered on. Pick a problem you find interesting, build something end to end, and share what you learn.

- Ask questions in Slack (after checking the FAQ first).
- Learn in public.
- Help your peers.
- Do not get stuck on one tool. The point is the patterns, not the brand names.
