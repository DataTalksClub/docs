---
title: "Getting Started"
layout: default
nav_order: 2
parent: LLM Zoomcamp
has_children: false
---

# Getting Started

For the cross-course onboarding (registration, account setup, calendar, newsletter), read [Joining a Cohort]({{ '/courses/zoomcamp-logistics/joining/' | relative_url }}) first.

This page covers the LLM Zoomcamp specifics.

## Star the GitHub repository

[github.com/DataTalksClub/llm-zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp)

Star it so you can find it later. All course materials are here, with each module having its own folder. Cohort-specific homework, deadlines, and launch-stream links are added under `cohorts/` when published.

If a lot of new participants star the repo around launch time, the repo can surface on GitHub Trending and pull more people into the cohort. It is the easiest way to support the course.

## Join the LLM Zoomcamp Slack channel

After joining the [DataTalks.Club Slack workspace](https://datatalks.club/slack), find the channel:

`#course-llm-zoomcamp`

This is your primary support and Q+A channel for the course. Use threads when replying. Don't tag instructors directly - other participants often answer first, and tagging discourages that.

## Subscribe to LLM Telegram (optional, recommended)

[t.me/llm_zoomcamp](https://t.me/llm_zoomcamp) is the announcement-only channel. Telegram is the most reliable place to catch important updates because Slack gets noisy. Telegram announcements are auto-reposted to Slack, so you do not strictly need it.

## Subscribe to YouTube

The lectures are pre-recorded and live in two playlists on the [DataTalks.Club YouTube channel](https://www.youtube.com/@DataTalksClub):

- LLM Zoomcamp main playlist: the canonical pre-recorded module videos.
- LLM Zoomcamp 2026: cohort-specific recordings (launch stream, office hours).

For all the playlist links, see [Resources]({{ '/courses/llm-zoomcamp/resources/' | relative_url }}).

## Bookmark the FAQ

The [LLM Zoomcamp FAQ](https://datatalks.club/faq/llm-zoomcamp.html) collects answers to module-specific and technical questions from previous cohorts. Check it before posting in Slack.

There is also a community-built bot that answers questions using the FAQ and Slack history; the link is pinned in the course Slack channel.

## Pick your LLM provider

The course uses OpenAI in its examples. You are free to use any provider for your own work and project. Practical options:

- OpenAI: the default. A few dollars of credit covers the whole course.
- Groq: free tier is generous enough to complete the course end to end.
- Ollama or similar: for fully local, no-API workflows on a normal laptop.

For tradeoffs and the recommended setup, see [Environment Setup]({{ '/courses/llm-zoomcamp/environment-setup/' | relative_url }}).

## Set up your environment

The course uses Python with Docker for the supporting services (search engines, monitoring), and notebooks for most of the work. You will install:

- Python (3.10 or newer).
- Docker.
- Jupyter (covered in module 1).
- An LLM provider account (OpenAI key, Groq key, or both).

For the choices you need to make, see [Environment Setup]({{ '/courses/llm-zoomcamp/environment-setup/' | relative_url }}).

## Start Module 1

Begin with [Module 1: RAG and Vector Search](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/01-rag). Module 1 covers what LLMs are, what RAG is, and walks you through a FAQ assistant with keyword search and vector search. For what each module covers, see [Curriculum]({{ '/courses/llm-zoomcamp/curriculum/' | relative_url }}).

## Where to look next

- [Prerequisites]({{ '/courses/llm-zoomcamp/prerequisites/' | relative_url }}) - what you need to know before starting.
- [Curriculum]({{ '/courses/llm-zoomcamp/curriculum/' | relative_url }}) - the modules.
- [Environment Setup]({{ '/courses/llm-zoomcamp/environment-setup/' | relative_url }}) - Python, providers, local vs hosted.
- [Project]({{ '/courses/llm-zoomcamp/project/' | relative_url }}) - the project rubric.
- [Resources]({{ '/courses/llm-zoomcamp/resources/' | relative_url }}) - all LLM-specific links in one place.
- [What's New]({{ '/courses/llm-zoomcamp/whats-new/' | relative_url }}) - changes for the current cohort.
- [Learning in Public]({{ '/courses/zoomcamp-logistics/learning-in-public/' | relative_url }}) - hashtag for LLM is `#llmzoomcamp`.
