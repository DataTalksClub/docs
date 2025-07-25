---
title: "What is Supervised Machine Learning?"
parent: "Module 1: Introduction to Machine Learning"
nav_order: 3
layout: page_with_toc
---

# What is Supervised Machine Learning?

> These notes are based on the video [ML Zoomcamp 1.3 - Supervised Machine Learning](https://youtu.be/j9kcEuGcC2Y?si=ry3WplRUFQS1R3zt)

<iframe width="560" height="315" src="https://www.youtube.com/embed/j9kcEuGcC2Y?si=YEQcfY4wDsiTRt35" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Supervised machine learning is a branch of machine learning where we teach algorithms by showing them examples. The term "supervised" comes from the fact that we act as teachers or supervisors, guiding the learning process by providing labeled examples.

## The Core Concept

In supervised learning:
1. We show the algorithm many examples with known outcomes (labels)
2. The algorithm learns patterns from these examples
3. The algorithm applies these patterns to make predictions on new, unseen examples

## Examples We've Seen

In previous lessons, we explored:
- **Car price prediction**: We showed the model different cars with their known prices, allowing it to learn patterns that determine car values
- **Spam detection**: We showed the model examples of spam and non-spam messages, enabling it to identify patterns that distinguish between them

## The Mathematics of Supervised Learning

Supervised learning uses concepts from mathematics and statistics to extract patterns from data.

## Formal Notation

We represent our data using:

- **Feature Matrix (X)**: A two-dimensional array where:
  - Rows represent observations (examples)
  - Columns represent features (characteristics)
  
- **Target Vector (y)**: A one-dimensional array containing the values we want to predict

For example, in spam detection:
- X would contain features of emails (length, presence of certain words, etc.)
- y would contain labels (1 for spam, 0 for not spam)

## The Goal of Supervised Learning

The goal is to find a function g (our model) such that:

g(X) ≈ y

In other words, when we apply our model g to the feature matrix X, it should produce predictions that are as close as possible to our target values y.

## The Training Process

The process of finding this function g is called "training" and involves:

1. Feeding the feature matrix X into the model
2. Comparing the model's predictions with the actual target values y
3. Adjusting the model to minimize the difference between predictions and actual values

## Types of Supervised Learning Problems

Based on the nature of the target variable and the output of our model, we can classify supervised learning into different types:

### 1. Regression Problems

- **Output**: A continuous numerical value
- **Example**: Car price prediction (predicting a price in dollars)
- **Range**: Can be any number within a range (often from -∞ to +∞)
- **Other examples**: House price prediction, temperature forecasting, stock price prediction

### 2. Classification Problems

- **Output**: A category or class label
- **Example**: Image classification (identifying objects in images)

Classification can be further divided into:

#### a. Multi-class Classification Problems
- Classifying into more than two categories
- Example: Identifying if an image contains a car, cat, or dog (3 classes)

#### b. Binary Classification Problems
- Classifying into exactly two categories
- Example: Spam detection (spam or not spam)
- The model often outputs a probability between 0 and 1
- The target variable is typically encoded as 0 or 1

### 3. Ranking Problems

- **Output**: An ordered list of items
- **Examples**:
  - Recommender systems (showing products a user might like)
  - Search engines (ordering results by relevance)

How Ranking Problems Work?
1. The model assigns a score to each item (e.g., probability of user interest)
2. Items are sorted by their scores
3. Top N items are presented to the user

Examples include:
- E-commerce product recommendations
- Search engine results
- Content recommendation systems

## Next Steps

In the next lesson, we'll explore the bigger picture of organizing machine learning projects and discuss a methodology called CRISP-DM (Cross-Industry Standard Process for Data Mining), which provides a structured approach to planning and executing machine learning projects.