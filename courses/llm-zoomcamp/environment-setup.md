---
title: "Environment Setup"
layout: default
nav_order: 4
parent: LLM Zoomcamp
has_children: false
---

# Environment Setup

The LLM Zoomcamp uses modern Python, `uv`, Docker, and Jupyter notebooks. You also need a hosted LLM provider. This page covers the high-level setup decisions. For step-by-step setup, follow [Module 1](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/01-agentic-rag).

## Runtime environment

The course is designed to run on your own laptop.

You need:

- A modern Python version. Python 3.10 or newer works. Use Python 3.11 or 3.12 if you are setting up a new environment.
- `uv` for Python dependency management.
- Docker (for the supporting services like the search engine and the monitoring stack).
- An LLM provider API key.

You do not need a GPU or a paid cloud account.

You can also run the course in GitHub Codespaces or on a cloud VM if your laptop is constrained. Choose an environment where you can run Docker.

## Choosing an LLM provider

The course examples use OpenAI, but the only real requirement is "an LLM you can call from Python".

Practical options:

- OpenAI: the default in the course examples and the most common API in industry. Pricing is per million tokens. A few dollars of credit covers the whole course. Even $10 of credit is hard to spend during the cohort.
- Groq: free tier is generous and hosts open-weight models. You can complete the entire course on Groq for free, as long as you do not hammer the API.
- Anthropic, AWS Bedrock, Google AI Studio, and similar: any provider with a Python SDK works.
- Ollama (fully local): runs an open-weight model on your own machine, no API key needed. Useful if you cannot or do not want to use a hosted API. The course mentions it but does not depend on it.

For a curated list of OpenAI-alternative providers, see the `awesome-llms` file in the course repo.

If you want to learn the OpenAI ecosystem because most paid roles touch it, use OpenAI. If you want to optimise for "no credit card", use Groq or Ollama.

## Python and dependency management

The course recommends `uv` for Python dependency management. It is faster than pip or conda and handles virtual environments cleanly. See the [uv documentation](https://docs.astral.sh/uv/) for installation.

Anaconda or plain `pip + venv` also work. The choice does not affect the course content.

## Notebooks

Some course materials use Jupyter notebooks.

You can run them:

- Locally.
- In VS Code with the Python and Jupyter extensions.
- In any Jupyter-compatible environment that can reach the services you run with Docker.

Google Colab is not recommended as the main course environment. It can work for isolated notebooks. Many modules need Docker services such as PostgreSQL, PGVector, the monitoring stack, or local containers.

## Docker

Docker runs the search engine, monitoring stack, and other supporting services. Install Docker before module 1 starts. The course does not teach Docker - it is a hard prerequisite.

## Operating system notes

Mac (Apple Silicon, M1/M2/M3):

- Most libraries have native ARM builds.
- Docker Desktop sometimes shows "Malware Blocked" warnings on installation. Allow it in System Settings if needed.
- Colima is a lighter alternative to Docker Desktop and works fine for the course.

Windows:

- WSL2 with Ubuntu is the smoothest path. Native Windows works but is rougher around the edges for Docker.

Linux:

- Native installation works without surprises. Make sure your user is in the `docker` group.

## Cost

The course is free.

The only spend you may incur:

- A few dollars on OpenAI credit, if you choose OpenAI. Most participants spend $1 to $5 across the whole cohort.
- $0 if you use Groq or Ollama.

There is no required cloud spend.

## AI tools (Cursor, ChatGPT, Claude)

Using AI tools to help you work through the course is fine and encouraged. You will get more out of the course if you understand the material well enough to debug AI-generated code. You should also be able to adapt that code to your own setup. For the AI usage policy on homework, projects, and peer review, see [AI Usage Policy]({{ '/courses/zoomcamp-logistics/ai-usage/' | relative_url }}).
