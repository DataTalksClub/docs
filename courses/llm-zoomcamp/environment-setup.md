---
title: "Environment Setup"
layout: default
nav_order: 4
parent: LLM Zoomcamp
has_children: false
---

# Environment Setup

The LLM Zoomcamp uses Python, Docker, Jupyter notebooks, and a hosted LLM provider. This page covers the high-level setup decisions. For step-by-step setup, follow the videos in [Module 1](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/01-intro).

## Where the work runs

The course is designed to run on your own laptop. You do not need a GPU. You do not need a paid cloud account. You do need:

- Python 3.10 or newer.
- Docker (for the supporting services like the search engine and the monitoring stack).
- An LLM provider API key.

You can also run the course in GitHub Codespaces or on a cloud VM if your laptop is constrained. The choice does not affect the course content.

## Choosing an LLM provider

The course examples use OpenAI, but the only real requirement is "an LLM you can call from Python". Practical options:

- OpenAI: the default in the course examples and the most common API in industry. Pricing is per million tokens. A few dollars of credit covers the whole course; even $10 of credit is hard to spend during the cohort.
- Groq: free tier is generous and hosts open-weight models. You can complete the entire course on Groq for free, as long as you do not hammer the API.
- Anthropic, AWS Bedrock, Google AI Studio, and similar: any provider with a Python SDK works.
- Ollama (fully local): runs an open-weight model on your own machine, no API key needed. Useful if you cannot or do not want to use a hosted API. The course mentions it but does not depend on it.

For a curated list of OpenAI-alternative providers, see the `awesome-llms` file in the course repo.

If you want to learn the OpenAI ecosystem on the way (because most paid roles touch it), use OpenAI. If you want to optimise for "no credit card", use Groq or Ollama.

## Python and dependency management

The course recommends `uv` for Python dependency management. It is faster than pip/conda and handles virtual environments cleanly. See the [uv documentation](https://docs.astral.sh/uv/) for installation.

Anaconda or plain `pip + venv` also work. The choice does not affect the course content.

## Notebooks

Most of the course is written in Jupyter notebooks. You can run them locally, in VS Code (with the Python and Jupyter extensions), in Google Colab, or in any Jupyter-compatible environment. Module 1 covers installing Jupyter.

## Docker

Docker is used to spin up the search engine, the monitoring stack, and other supporting services. You should already have Docker installed before module 1 starts. The course does not teach Docker - it is a hard prerequisite.

## Operating system notes

Mac (Apple Silicon, M1/M2/M3):

- Most libraries have native ARM builds.
- Docker Desktop sometimes shows "Malware Blocked" warnings on installation; allow it in System Settings if needed.
- Colima is a lighter alternative to Docker Desktop and works fine for the course.

Windows:

- WSL2 with Ubuntu is the smoothest path. Native Windows works but is rougher around the edges for Docker.

Linux:

- Native installation works without surprises. Make sure your user is in the `docker` group.

## Cost

The course is free. The only spend you may incur:

- A few dollars on OpenAI credit, if you choose OpenAI. Most participants spend $1 to $5 across the whole cohort.
- $0 if you use Groq or Ollama.

There is no required cloud spend. The previous cohort had an open-source LLMs module that benefited from a cloud GPU; that material has moved to the [Open Source LLM Zoomcamp](https://github.com/DataTalksClub/open-source-llm-zoomcamp).

## AI tools (Cursor, ChatGPT, Claude)

Using AI tools to help you work through the course is fine and encouraged. You will get more out of the course if you understand the material well enough to debug AI-generated code and adapt it to your own setup. For the AI usage policy on homework, projects, and peer review, see [AI Usage Policy]({{ '/courses/zoomcamp-logistics/ai-usage/' | relative_url }}).
