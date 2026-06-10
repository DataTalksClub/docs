---
title: "Environment Setup"
layout: default
nav_order: 4
parent: MLOps Zoomcamp
has_children: false
---

# Environment Setup

The MLOps Zoomcamp uses Python with common ML and MLOps tooling: MLflow, Prefect, Docker, Evidently, Grafana, Prometheus, Terraform, and AWS for cloud examples. This page covers the high-level setup decisions. For step-by-step setup, follow the videos in [Module 1](https://github.com/DataTalksClub/mlops-zoomcamp/tree/main/01-intro).

## Where to run the course

You can work locally or on a cloud VM. Module 1 demonstrates both:

- A local machine with Python and Docker installed.
- GitHub Codespaces.
- A cloud VM (the course shows an AWS EC2 instance).

A cloud VM is convenient because the later modules use AWS services anyway, and it keeps your environment consistent.

## Python and dependency management

The course uses Python with the scientific stack (pandas, scikit-learn) plus MLOps libraries. You can manage dependencies with `uv`, conda, or pip + venv. The choice does not affect the course content.

On Windows, Anaconda is often the easiest way to get Python plus scientific libraries running. Docker Desktop covers the container side.

## Docker

Docker is used throughout the course for packaging models, running services, and reproducing environments. Install Docker and Docker Compose early. Module 1 includes the installation steps.

## Cloud (AWS)

The course uses AWS for several modules:

- Module 4 deploys a streaming service with Kinesis and Lambda.
- Module 6 provisions infrastructure with Terraform.

New AWS accounts get free tier credits. You introduce each service as the modules reach it, so you do not need prior AWS experience.

## Tools introduced per module

- Module 2: MLflow.
- Module 3: a workflow orchestrator.
- Module 4: Flask, AWS Kinesis, AWS Lambda, Docker.
- Module 5: Evidently, Grafana, Prometheus, Prefect, MongoDB.
- Module 6: pytest, pre-commit, GitHub Actions, Terraform.

Each module README lists exactly what to install for that module.
