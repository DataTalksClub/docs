---
title: "Curriculum"
layout: default
nav_order: 3
parent: Production AI Agents for Generative Media
has_children: false
---

# Curriculum

The course has a welcome session, four modules, and a capstone project. You build one system, a Personalized Media Factory, and each module adds a layer: make it work, make it intelligent, make it scale, make it production-ready.

For the canonical curriculum (videos, code, exact homework), see the [GitHub repository](https://github.com/DataTalksClub/open-source-llm-zoomcamp). All times are CET, and modules run Monday to Sunday. Materials and dates may change.

## Schedule

- Tuesday, November 10, 2026: Module 0, Welcome, live (together with the pre-course Live Q&A).
- Monday, November 16, 2026: course launch, live.
- November 16 to 29: Module 1 (two weeks). Homework 1 and the capstone proposal.
- November 30 to December 6: Module 2. Homework 2, due Monday, December 7.
- December 7 to 13: Module 3. Homework 3 (leaderboard), due Monday, December 14.
- December 14 to 20: Module 4. Capstone brief, no homework.
- Friday, January 15, 2027: capstone submission, attempt 1.
- Friday, January 22, 2027: peer review, attempt 1.
- Friday, January 29, 2027: capstone submission, attempt 2.
- Friday, February 5, 2027: final peer review, attempt 2.

Check the [course platform](https://courses.datatalks.club/production-ai-agents-generative-media/) for exact deadlines.

## Modules

Module 0: Welcome

- Why media agents are an engineering problem, not a prompting problem.
- The factory end to end, and real projects from Nebius customers and partners.
- You leave with your starting point and setup.

Module 1: Consistent Media Generation on Serverless GPUs

- The media model landscape and your first media generation in a few minutes.
- Containers for generative AI, serving versus batch inference.
- Measuring startup, load, and generation costs.
- Homework 1, GPU Media Worker: your creative idea goes in, and an asset plus the cost per asset and the self-host breakeven come out.
- Capstone proposal.

Module 2: Multi-Agent Media Workflows

- The agent loop from scratch.
- GPU models as typed tools over MCP.
- Long-running tools.
- Planner, generator, and reviewer agents.
- Homework 2, Media Agent: a 10-second ad plus an execution trace.

Module 3: Batch Media Generation at Scale

- Fan-out with Jobs.
- Spot GPUs and designing for interruption.
- Optimizing cost per asset: cold start, VRAM, and speed.
- Breaking the pipeline on purpose.
- Homework 3, Factory Scale Challenge: 200 records over 10 parallel Jobs, with a public leaderboard.

Module 4: Evaluation, Observability and Production

- Evaluating generative systems at the system, agent, and media layers.
- Judge calibration and regression gates.
- Observability and tracing.
- Designing for production: architecture, SLO, dashboard, and alerts.
- Production concerns and the capstone brief: auth, quotas, abuse, prompt injection, content safety, licensing, and provenance.
- No homework: you apply Module 4 in your capstone.

## Tools

- Media runtimes: Hugging Face Diffusers and model-specific runtimes, with ComfyUI for prototyping.
- Models: Qwen-Image or FLUX-class and Sana for images, Wan for video, Kokoro or Chatterbox TTS and Whisper for audio. Any open-weights equivalent works.
- LLM: Nebius Token Factory (OpenAI-compatible), or any OpenAI-compatible API.
- Agents and tools: raw tool calling, then MCP.
- GPU compute: Nebius Serverless AI Jobs and Endpoints.
- Storage and API: S3-compatible Object Storage and FastAPI.
- Tracking, tracing, and evals: to be announced.

## Homework and capstone

Homework 1 to 3 is peer-reviewed in the live cohort. See [Capstone Project]({{ '/courses/production-ai-agents-generative-media/project/' | relative_url }}) for the capstone requirements and review rubric. A certificate is not confirmed yet.
