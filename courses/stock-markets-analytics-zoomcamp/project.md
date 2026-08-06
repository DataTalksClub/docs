---
title: "Project"
layout: default
nav_order: 6
parent: Stock Market Analytics Zoomcamp
has_children: false
---

# Project

For the cross-course logistics, see [Final Project (Zoomcamp Logistics)]({{ '/courses/zoomcamp-logistics/project/' | relative_url }}). That page covers attempts, deadlines, peer review, and certification mechanics.

This page covers what is specific to the Stock Market Analytics Zoomcamp.

## Goal

Build your own analytics and prediction system for a financial market. You pick the data, generate features, train a model, define a trading strategy on top of the predictions, and simulate the results. Ideally you also automate the workflow so it runs without you.

The project is the only requirement for the certificate. You can skip every homework and still graduate, though homework earns leaderboard points and is good preparation.

## Choosing a market

The course uses large US stocks, but the approach transfers:

- Any stock exchange works. Yahoo Finance covers thousands of tickers, including Indian, European, and other markets. You may need to convert positions to a single currency if you mix markets.
- ETFs, crypto, forex, and commodities work too. For crypto, expect to rely on technical indicators, since the macroeconomic and fundamental data used for stocks does not apply.
- Futures, options, and other derivatives are harder: good historical data is expensive and the modeling needs extra features.

Building a project about your local market is genuinely interesting, since most public analysis covers the same handful of big American companies.

## What fits and what does not

Good fits:

- Predictive modeling on time series price data.
- Quantitative trading strategies and backtesting or simulation.
- An automated workflow that refreshes predictions on a schedule.

Not what this course prepares you for:

- Personal finance management, expense tracking, or portfolio and risk management as the main topic.
- High-frequency trading and market microstructure.
- Sentiment analysis as the core idea. It is allowed, but long histories of news data are paid, and you may need to settle for two to five years of data rather than the 25 years available for prices.

## Practical advice

A few things that make the project go better:

- Start early. Many participants build the project as they work through the modules, and submissions appear the moment the form opens.
- Most people spend around 20 hours on it. Those coming from a non-technical background have spent considerably more.
- Projects are solo. You can discuss ideas, form study groups, and hold each other accountable, but the code you submit must be your own.
- Use GitHub for the project. Colab links are acceptable for homework, but the project should be a public repository a reviewer can read and run.
- Reviewing three peers' projects is required. Looking at previous cohorts' projects in the repository is also the fastest way to understand what a good submission looks like.

## Disclaimer

There is no expectation of a profitable strategy, and no guarantee of one. The project is graded on the analysis and the engineering, not on returns. Nothing you build here is investment advice, and if you trade with your own money you do so at your own risk.

## Certificate

Completing the project and reviewing three peers' projects during a live cohort earns the certificate, signed by the instructors. See [Certification]({{ '/courses/zoomcamp-logistics/certification/' | relative_url }}) for how it is issued and how to add it to LinkedIn.
