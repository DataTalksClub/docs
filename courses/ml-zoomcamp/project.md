---
title: "Project"
layout: default
nav_order: 6
parent: Machine Learning Zoomcamp
has_children: false
---

# Project

For the cross-course logistics (attempts, deadlines, peer review, certification mechanics), see [Final Project (Zoomcamp Logistics)]({{ '/courses/zoomcamp-logistics/project/' | relative_url }}).

This page covers what is specific to the Machine Learning Zoomcamp.

## Project structure

The ML Zoomcamp has three project slots: midterm, capstone, and a second capstone. To earn the certificate, you must complete two of three:

- Midterm + capstone, or
- Capstone + second capstone.

Each project follows a structured timeline:

- 2 weeks for development.
- 1 week for peer reviews.

You complete 3 peer reviews per project you submit.

## Required: deployed model

Every ML Zoomcamp project must include a working deployed model. You cannot just train a model in a notebook - you need to make it accessible through deployment, demonstrating real-world ML engineering skills.

Options for deployment:

- FastAPI in a Docker container (the course pattern).
- AWS Lambda with ONNX runtime.
- Streamlit, Gradio, or similar interactive demos that wrap your model.
- Kubernetes (EKS, kind, or minikube).

Document the deployment in your README so peer reviewers can either run it themselves or evaluate the deployment from screenshots and code.

## Tech stack flexibility

You are not restricted to the technologies covered in the course. Use any framework, model architecture, or cloud provider. However:

- Document your choices clearly. Your reviewers need full context to evaluate technologies they may not know.
- Make the project reproducible. If a reviewer cannot run it (or at least understand how it would run), you will lose reproducibility points.

## Dataset

You choose the dataset. It should:

- Have at least 100 rows for meaningful model development.
- Be public (so peer reviewers can verify).
- Reflect a problem worth solving.

Avoid datasets that are too clean (Titanic, Iris) - they do not let you demonstrate the data engineering and feature engineering skills the rubric looks for.

## Datasets you cannot use

You cannot use any dataset that the course itself uses in lectures or homework. The point of the project is to apply your skills to something new. Datasets used in the course include:

- Car price prediction (Module 2 / Linear Regression).
- Customer churn / Telco (Module 3 / Binary Classification).
- Loan default (Module 6 / Tree-Based Models).
- Datasets used in the deep learning, serverless, and Kubernetes modules.

For the canonical list, see the project rubric in the course repo.

## Evaluation criteria

Each course defines its own rubric. The platform shows the exact criteria when you review or are reviewed. Common criteria:

- Problem description and motivation.
- Data preparation and exploratory analysis.
- Model training, validation, and selection.
- Final model deployment.
- Reproducibility (can the reviewer run your code).
- Documentation quality.

The full rubric for the current cohort is on the course platform under the project window.

## Certification

Submit two of three projects on time, complete peer reviews for each, and reach the passing scores. That is the only requirement to graduate.

What is not required:

- Homework scores. Homework is for learning.
- Live session attendance.
- Leaderboard points.

The earliest you can receive your certificate is after the final project's peer-review deadline. For when the certificate is issued and how to add it to LinkedIn, see [Certification (Zoomcamp Logistics)]({{ '/courses/zoomcamp-logistics/certification/' | relative_url }}).

## Past projects for inspiration

- [ML Zoomcamp 2025 projects](https://courses.datatalks.club/ml-zoomcamp-2025/projects)
- Browse past cohorts on the [course platform](https://courses.datatalks.club/).

## Portfolio focus

Treat every project as a portfolio piece. Use meaningful repository names (`telecom-churn-prediction-xgboost`, not `homework3`). Include comprehensive setup instructions. Past graduates have used these projects to land roles at companies like Meta and to secure ML internships.
