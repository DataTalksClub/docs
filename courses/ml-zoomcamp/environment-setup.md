---
title: "Environment Setup"
layout: default
nav_order: 4
parent: Machine Learning Zoomcamp
has_children: false
---

# Environment Setup

The Machine Learning Zoomcamp uses Python with scikit-learn, FastAPI, Docker, and AWS for cloud examples. This page covers the high-level setup decisions. For step-by-step setup, follow the videos in [Module 1](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/01-intro).

## Python and dependency management

The course recommends `uv` for Python dependency management. It is faster than pip/conda and handles virtual environments cleanly. See the [uv documentation](https://docs.astral.sh/uv/) for installation.

You can also use Anaconda. On Windows, Anaconda is often the easiest way to get Python plus scientific libraries running.

Plain `pip + venv` works too. The choice does not affect the course content.

## Notebook environment

The course uses Jupyter notebooks throughout. You can run them locally, in Google Colab, or in any Jupyter-compatible environment.

VS Code with the Python and Jupyter extensions is a popular choice and gives you both notebook and full IDE features.

## Cloud (AWS)

The course uses AWS for deployment in modules 9 and 10 (Lambda, EKS). New AWS accounts get free tier credits, though the free tier is more limited than GCP's.

You can complete the course without AWS:

- Module 5 (basic deployment) runs locally with Docker.
- Module 9 (serverless) can be done with the free Lambda tier or skipped.
- Module 10 (Kubernetes) can be done locally with `kind` or `minikube` instead of EKS.

For your project, you can use any cloud provider (AWS, GCP, Azure) or stay local. Document your choices for peer reviewers.

## AI tools (Cursor, ChatGPT, etc.)

The course welcomes AI tools like Cursor, ChatGPT, and Claude. You will get more out of the course if you understand the concepts well enough to debug AI-generated code, maintain control over your implementations, and build custom solutions when AI tools fall short.

## Operating system notes

Mac (Apple Silicon, M1/M2/M3):

- Most ML libraries now have native ARM builds.
- Docker Desktop sometimes shows "Malware Blocked" warnings on installation; allow it in System Settings if needed.

Windows:

- Anaconda is the smoothest path for the scientific Python stack.
- For deployment modules with Docker, WSL2 with Ubuntu is what most students use.

Linux:

- Native installation works without surprises.

## Common challenges

Module 4 (model evaluation) is consistently the most challenging section. Topics like ROC curves, precision-recall trade-offs, and cross-validation can feel abstract. Allocate extra time for this module and join study groups for additional explanations.

Set up your development environment early. Document your setup process with specific versions and commands. Use version control for all your work from the beginning.
