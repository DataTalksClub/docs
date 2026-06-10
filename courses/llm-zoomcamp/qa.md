---
title: "Q&A"
layout: default
nav_order: 9
parent: LLM Zoomcamp
has_children: false
---

# Questions and Answers

This page covers LLM-specific questions about course scope and philosophy. For general zoomcamp logistics, see [Zoomcamp Logistics]({{ '/courses/zoomcamp-logistics/' | relative_url }}). For module-specific and technical issues, check the [LLM Zoomcamp FAQ](https://datatalks.club/faq/llm-zoomcamp.html).

## Agents module

The 2026 course includes agents because the basic patterns are now stable enough to teach. Agents are part of Module 1: Agentic RAG.

The module still builds from first principles. It starts with a RAG pipeline, then adds function calling, tool use, and the agentic loop.

## RAG focus

A year ago RAG was the most common LLM application in the wild. Today many providers offer built-in RAG features, but RAG remains the strongest teaching example. It shows how to combine retrieval, prompting, and evaluation in a real system. Skills you build for RAG transfer to most other LLM applications.

## MCP and LangGraph

The surface area is still changing quickly. The course teaches agents without depending on a large framework so that you understand the mechanics. Once you do, picking up MCP, LangGraph, or another framework takes less time.

LangChain is the one exception - it appears in the optional best-practices module for hybrid search and document reranking.

## LLM internals

This course is about LLM engineering, not LLM internals. LLMs are treated as black boxes you call through an API.

Building your own LLM from scratch is not on the roadmap and there are already strong courses on that elsewhere.

## Difference from ML Zoomcamp

ML Zoomcamp covers classical machine learning and looks under the hood at how models learn. It also covers model selection and evaluation. LLM Zoomcamp does not look under the hood. It teaches you to build applications on top of hosted LLMs, including evaluation and monitoring.

If you are deciding between the two, take ML Zoomcamp if you want to understand machine learning. Take LLM Zoomcamp if you want to build with LLMs.

## Difference from MLOps Zoomcamp

MLOps Zoomcamp covers the operational lifecycle of ML models, including experiment tracking and model registry. It also covers deployment, monitoring, and retraining.

LLM Zoomcamp's monitoring module covers similar ground for LLMs:

- Request volume
- Latency
- Cost
- Response quality

It does not cover training-side concerns.

## Retaking the course

The RAG focus is still there, but the 2026 flow is different from 2025. Module 1 is now Agentic RAG, and agents are no longer a separate Module A. Module 3 covers orchestration with Kestra. Evaluation now includes agent evaluation basics. Monitoring is a full module with PostgreSQL, Streamlit, and Grafana.

It is worth retaking if you want to refresh and re-implement with the current course structure.

## Existing RAG experience

If you already know RAG, skim module 1 first. If it feels familiar, jump straight to the project. Identify gaps as you build, then go back and fill just those.

## Jobs after the course

The course gives you engineering skills companies want. Whether you land a job depends on what you do outside the course.

Use the course as a base for:

- Build projects
- Learn in public
- Share your work
- Apply

There is anecdotal evidence of past graduates landing AI roles after the course but no clean data on conversion rates. Treat it as one strong piece of a portfolio, not a guaranteed path.

For data scientists who do not yet work with LLMs, this course is a strong way to extend your profile. Many DS roles now expect RAG familiarity.

## Career switchers

It is possible, with effort. The course assumes you can program. If you can, the LLM-specific concepts are accessible in a few weeks. If you cannot program yet, build programming basics first. The course is hard without them.

## Final thoughts

LLM engineering is mostly the engineering you already know, with a few new patterns layered on. Pick a problem you find interesting, build something end to end, and share what you learn.

- Ask questions in [`#course-llm-zoomcamp`](https://app.slack.com/client/T01ATQK62F8/C06TEGTGM3J) after checking the FAQ first.
- Learn in public.
- Help your peers.
- Do not get stuck on one tool. The patterns matter more than the brand names.
