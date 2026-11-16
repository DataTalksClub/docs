---
title: "Project"
layout: default
nav_order: 7
parent: Production AI Agents for Generative Media
has_children: false
---

# Capstone Project

For the shared project rules, see [Final Project (Zoomcamp Logistics)]({{ '/courses/zoomcamp-logistics/project/' | relative_url }}). For this course, follow the requirements here. The canonical version is in the [projects folder](https://github.com/DataTalksClub/open-source-llm-zoomcamp/tree/main/projects) of the repository.

## Goal

Build a production multimodal agent and share it publicly. The capstone starts in Module 1 and has its first submission deadline on January 15, 2027.

## Requirements

- A multimodal agent that uses at least 2 GPU media models (any combination of image, video, and audio), with an agent that has 2 or more tools.
- An async workload: the agent orchestrates long-running GPU jobs with job IDs, state persistence, and resume, not blocking calls.
- Assets stored in object storage.
- A batch run: 100 records for image and audio assets, 10 records for video assets.
- Evaluation: a golden set plus a regression gate, at the system, agent, and media layers.
- Observability: a trace per request that answers why this cost and why this long, plus metrics, logs, and a dashboard.
- An SLO and a cost report.
- Proof that a killed run resumes without redoing finished work.
- Runs on Nebius Serverless AI (Jobs, Endpoints) as the reference execution layer.
- The code is open source (MIT), OpenAI- and S3-compatible.

Bring your own records: a CSV or JSONL file with an id column. Records go in, generated media comes out.

Ideas: a marketing studio, podcast producer, video localization, storybook generator, product ad agent, or paper-to-explainer video.

## Timeline

- Module 1 (November 16 to 29): pick your records, get the first GPU generation working, and fill in the capstone proposal template.
- Modules 2 to 4 (November 30 to December 20): teaching, with the capstone brief in Module 4.
- Attempt 1: submit by January 15, 2027, and complete peer reviews by January 22, 2027.
- Attempt 2: submit by January 29, 2027, and complete the final peer reviews by February 5, 2027.
- Submission and peer-review deadlines are 23:59:59 UTC on these dates.

## Peer review

Capstones are peer-reviewed against an 8-area rubric. Peers score each area 0, 1, or 2:

- System: a working end-to-end system on Nebius Serverless AI with the required batch.
- Agent: at least two tools, orchestrating long-running GPU jobs with job IDs and persisted state.
- Media: at least two GPU media models, with assets stored in object storage.
- Cost: a cost report that explains the cost per asset or per request.
- Reliability: a killed run resumes without redoing finished work.
- Observability: a trace per request, plus metrics, logs, and a dashboard.
- Reproducibility: the run is reproducible from public MIT code, with pinned versions and inputs.
- Presentation: the work is shared publicly with a clear write-up of what was built, how to run it, and the results.

To pass, submit your project, review peers, and share your work publicly. See the repository for the full score descriptions.

## Certificate

A certificate is not confirmed yet. We will update this page when that is decided.
