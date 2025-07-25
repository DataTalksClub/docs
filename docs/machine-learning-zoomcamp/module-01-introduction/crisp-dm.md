---
title: "What is CRISP-DM?"
parent: "Module 1: Introduction to Machine Learning"
nav_order: 4
---

# What is CRISP-DM?

> These notes are based on the video [ML Zoomcamp 1.4 - CRISP-DM](https://youtu.be/dCa3JvmJbr0?si=QixEZxWzDeCnSvCq)

<iframe width="560" height="315" src="https://www.youtube.com/embed/dCa3JvmJbr0?si=QixEZxWzDeCnSvCq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

CRISP-DM stands for **Cross-Industry Standard Process for Data Mining**, a methodology for organizing machine learning projects. Despite being developed in the 1990s by IBM, it has stood the test of time and remains relevant for modern ML projects with minimal modifications.

CRISP-DM is a methodology for organizing machine learning projects. It is a process that helps you understand the problem, the data, and the model. It is a process that helps you build a machine learning model that is accurate and reliable.

This methodology helps structure the entire ML workflow from problem understanding to deployment through six key steps:

1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Modeling
5. Evaluation
6. Deployment

Throughout this lesson, we'll use a spam detection example to illustrate how each step applies in practice.

## The Spam Detection Example

Our example involves creating a system that identifies spam emails:
- The system receives an email
- Features are extracted from the email
- A model processes these features
- The model outputs a score (e.g., probability of being spam)
- If the score exceeds a threshold (e.g., 50%), the email goes to the spam folder; otherwise, it goes to the inbox

Now let's explore each step of CRISP-DM using this example.

## Business Understanding

The first step involves identifying and understanding the problem we want to solve. Key activities include:

- **Problem identification**: For our spam example, we need to understand why spam detection matters. Are users complaining about spam? How many users? How severe is the problem?

- **Solution approach assessment**: We must determine if machine learning is the right tool for this problem or if simpler approaches (like rule-based systems) would suffice.

- **Success metric definition**: It's crucial to establish measurable goals. Instead of vaguely saying "reduce spam," we should specify "reduce spam messages by 50%." This concrete metric helps us evaluate success later.

The business understanding step ensures we're solving the right problem with appropriate tools and have clear success criteria.

## Data Understanding

Once we've defined the problem, we need to understand what data is available to solve it. This step involves:

- **Data availability assessment**: For spam detection, we might have data from users clicking a "mark as spam" button.

- **Data quality evaluation**: We need to verify if the data is reliable. Do we consistently record when users mark emails as spam? Are there cases where users incorrectly mark legitimate emails as spam?

- **Data volume assessment**: Is the dataset large enough for machine learning? If we only have 10 records, we might need to collect more data before proceeding.

This step might reveal issues that require revisiting the business understanding step. For example, if we discover that our data tracking is unreliable, we might need to redefine our approach.

## Data Preparation

After confirming we have sufficient, reliable data, we transform it into a format suitable for machine learning algorithms:

- **Data cleaning**: Remove noise and errors, such as instances where users accidentally marked legitimate emails as spam.

- **Feature extraction**: Convert raw data into features that algorithms can process. For spam detection, we might extract features like:
  - Sender information
  - Presence of specific words (e.g., "deposit")
  - Email length
  - Number of recipients
  - Other relevant characteristics

- **Pipeline building**: Create a sequence of transformations that convert raw data into a clean, tabular format with features (X) and target variables (y).

The goal is to produce data in the standard format we discussed previously: a feature matrix X and a target vector y.

## Modeling

This is where actual machine learning happens:

- **Model selection**: Try different algorithms (logistic regression, decision trees, neural networks, etc.) to see which performs best on our data.

- **Model training**: Train these models on our prepared data.

- **Model comparison**: Compare their performance to select the most effective one.

Often during this step, we discover that our features are insufficient or there are data issues, requiring us to return to the data preparation step. This iterative process helps refine our approach.

## Evaluation

After selecting the best model, we need to evaluate if it meets our business goals:

- **Goal assessment**: Return to the business understanding step and check if our model achieves the metrics we established (e.g., reducing spam by 50%).

- **Success determination**: If we aimed for a 50% reduction but only achieved 30%, we need to decide if this is acceptable or requires further iteration.

- **Project viability**: Based on results, we might continue improving the model, revise our goals, or determine the project isn't viable.

In modern ML workflows, evaluation often happens alongside deployment through online testing with real users.

## Deployment

The final step involves implementing the model in production:

- **Gradual rollout**: Often, we first deploy to a small percentage of users (e.g., 5%) to evaluate performance before full deployment.

- **Engineering focus**: While previous steps emphasized machine learning, deployment focuses on engineering aspects:
  - Monitoring
  - Maintainability
  - Service quality
  - Reliability
  - Scalability

This ensures our model works reliably in real-world conditions.

## Iteration: The Continuous Cycle

Machine learning projects don't end with deployment. The CRISP-DM process is cyclical:

- After deployment, we learn from real-world performance
- We return to the business understanding step with new insights
- We refine our goals and approach
- We go through the cycle again to improve our solution

A best practice is to start simple:
1. Complete a quick iteration with a simple model
2. Deploy and learn from this initial version
3. Return to business understanding with new insights
4. Gradually increase complexity in subsequent iterations

This approach delivers value quickly while allowing for continuous improvement.

## Summary

The CRISP-DM methodology provides a structured approach to machine learning projects through six key steps:

1. **Business Understanding**: Define measurable goals and determine if ML is appropriate
2. **Data Understanding**: Assess available data for quality, reliability, and sufficiency
3. **Data Preparation**: Clean data and extract features in a format suitable for ML
4. **Modeling**: Train and select the best performing model
5. **Evaluation**: Verify if the model meets business goals
6. **Deployment**: Roll out the model to users with proper engineering practices

The process is iterative, with each cycle building on lessons from previous iterations. Starting simple and gradually increasing complexity allows for faster delivery of value while maintaining a path for continuous improvement.

In the next lesson, we'll dive deeper into the modeling step to explore how to select and evaluate different machine learning models.