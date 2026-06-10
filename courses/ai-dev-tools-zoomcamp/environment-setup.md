---
title: "Environment Setup"
layout: default
nav_order: 4
parent: AI Dev Tools Zoomcamp
has_children: false
---

# Environment Setup

The course is tool-agnostic: you can follow along with whichever AI coding tools you prefer. This page covers the high-level choices.

## AI coding tools

You'll use one or more of:

- Chat assistants: ChatGPT, Claude, Gemini, DeepSeek.
- Coding assistants / IDEs: Claude Code, GitHub Copilot, Cursor, Antigravity, Gemini CLI.
- Project bootstrappers: Bolt, Lovable.

Use whatever you're comfortable with. Codex, Gemini CLI, and Antigravity are good free or low-cost alternatives to a paid Cursor or Copilot subscription.

## What it costs

The course is designed to be doable on free or cheap tools:

- Module 1: free (works with free tools like Groq or Gemini).
- Module 2: a coding assistant helps; Cursor or GitHub Copilot offer free trials, and Gemini CLI or Antigravity are free alternatives.
- Module 4: a small API deposit (around $5) for OpenAI or Anthropic.

Free tiers have quota limits, so you may need to switch tools or wait when you hit them. Tracking usage (`/stats`, quota extensions) and using auto modes helps.

## Where to run it

You can work locally or in GitHub Codespaces (its free tier is usually enough). Python with uv is recommended for dependency management, and Docker is used for packaging and deployment in the later modules.

## Cloud and deployment

The end-to-end and project modules deploy real apps. Render, Google Cloud (free credits), and similar platforms all work. For projects that scrape external sites (for example YouTube transcripts), be aware that data-center IPs are often blocked and you may need a residential proxy.
