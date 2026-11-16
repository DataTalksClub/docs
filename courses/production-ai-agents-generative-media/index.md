---
title: "Production AI Agents for Generative Media"
layout: default
nav_order: 8
parent: Courses
description: "Free, application-only course by Nebius and DataTalks.Club on agents that run image, video, and audio models on serverless GPUs"
has_children: true
---

# Production AI Agents for Generative Media

Production AI Agents for Generative Media is a free, open-source (MIT), project-based course by Nebius and DataTalks.Club. You build, scale, and monitor agents that run image, video, and audio models on serverless GPUs.

The first cohort starts on Monday, November 16, 2026. The live cohort is application only, and applications are open until Monday, November 30, 2026. [Apply for the cohort](https://courses.datatalks.club/register/production-ai-agents-generative-media/) and use the [course platform](https://courses.datatalks.club/production-ai-agents-generative-media/) for deadlines, homework submissions, and scores.

## Links

- [Course platform](https://courses.datatalks.club/production-ai-agents-generative-media/) - schedule, deadlines, homework, scores.
- [Apply for the cohort](https://courses.datatalks.club/register/production-ai-agents-generative-media/)
- [GitHub repository](https://github.com/DataTalksClub/open-source-llm-zoomcamp) - all materials, MIT license.
- [Slack channel #course-ai-mediagen](https://app.slack.com/client/T01ATQK62F8/C0CEG1BUDKL) and the [Slack invite](https://datatalks.club/slack.html) if you are not in the workspace yet.
- [YouTube playlist](https://www.youtube.com/playlist?list=PLC73BZc0zZKM) - session recordings, including the [course launch](https://www.youtube.com/watch?v=Y5__PUmOTdg) and the [pre-course Q&A](https://www.youtube.com/watch?v=iACtrkiXndw).
- [Course FAQ](https://datatalks.club/faq/production-ai-agents-generative-media.html) and the [FAQ page in these docs]({{ '/courses/production-ai-agents-generative-media/faq/' | relative_url }}).
- [Nebius AI Builder Program](https://dev.nebius.com/builders) - GPU credits.
- [Learning in public]({{ '/courses/zoomcamp-logistics/learning-in-public/' | relative_url }}) and [Community Guidelines]({{ '/general/guidelines/' | relative_url }}).

## Docs order

Read in this order:

1. [Community Guidelines]({{ '/general/guidelines/' | relative_url }}) - code of conduct, how to ask questions, how to use Slack channels.
2. [Zoomcamp Logistics]({{ '/courses/zoomcamp-logistics/' | relative_url }}) - how DataTalks.Club courses work in general (homework, project, peer review). This course is application only, so the registration steps there do not apply.
3. [Getting Started]({{ '/courses/production-ai-agents-generative-media/getting-started/' | relative_url }}) - how to apply, GPU credits, and where to ask questions.
4. [Curriculum]({{ '/courses/production-ai-agents-generative-media/curriculum/' | relative_url }}) and [Capstone Project]({{ '/courses/production-ai-agents-generative-media/project/' | relative_url }}).
5. [FAQ]({{ '/courses/production-ai-agents-generative-media/faq/' | relative_url }}) - the most common questions before applying.

## What you build

The question behind the course: how do you build a production AI system when an agent can launch expensive, slow, failure-prone GPU workloads that produce large media artifacts? Media agents are an engineering problem, not a prompting problem.

You build one system, a Personalized Media Factory:

- Input: a brief made of a task prompt, a data record, and constraints such as format, style, and budget.
- Agent: an LLM plans the asset and writes its text, such as a card message or an ad script.
- GPU models: generate an image plus voice or video.
- Check: regenerates the asset when it is not good enough.
- Scale: from 1 to 1,000+ records, with a cost per asset.

## Course outcomes

- Run image, video, and audio models as Jobs and Endpoints on serverless GPUs, without managing a cluster.
- Give agents GPU models as tools (MCP) and build generate, evaluate, regenerate loops.
- Fan out batch workloads on spot GPUs, handle failures, and report cost per asset.
- Add evals, tracing, and SLOs, so you can say what a media agent costs and when it is good enough to ship.

## Who it is for

The course is for working builders running open or custom GPU media models:

- AI and ML engineers adding image, video, or audio generation to real systems.
- MLOps and ML platform engineers who own the batch pipeline, scheduling, and cost line.
- Technical founders and small teams paying for per-call media APIs who need to know when self-hosting wins.

The level is intermediate to advanced. You need Python, Docker basics, HTTP APIs, and the command line. Prior LLM or MLOps course experience helps but is not required.

The course does not cover diffusion maths, training foundation models, deep fine-tuning, CUDA, Kubernetes, RAG, or LLM fundamentals.

## Format and cost

- The course is free. Seats in the live cohort are limited, so it is application only.
- Lectures are pre-recorded. There is a weekly live office hour, and live classes are not mandatory.
- The code is MIT-licensed and OpenAI- and S3-compatible, so you can run it elsewhere. Nebius Serverless AI and Nebius Token Factory are the reference platform.
- The workloads run on GPUs, which cost money. Applicants get GPU credits through the [Nebius AI Builder Program](https://dev.nebius.com/builders). Usage beyond the credits is billed to your account.
- Each module reports cost per asset, so you know what a run costs before you scale it.
- A certificate is not confirmed yet. We will update this page when that is decided.

Materials and dates may change. The materials are public in the [GitHub repository](https://github.com/DataTalksClub/open-source-llm-zoomcamp), so you can also follow along on your own, with your own GPU access.
