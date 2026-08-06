---
title: "Environment Setup"
layout: default
nav_order: 4
parent: Stock Market Analytics Zoomcamp
has_children: false
---

# Environment Setup

The course is designed to be completed for free, and a browser is enough for the first four modules.

## Where you write code

You have two environments during the course:

- Google Colab for Modules 1 to 4. All notebooks are shared so you can copy one, run it under your own account, and change parameters or markets.
- A local editor such as VS Code for Module 5, when notebooks become Python files.

## Python libraries

The stack is the standard analyst toolkit:

- numpy and pandas for the data work.
- matplotlib, seaborn, and Plotly Express for charts.
- TA-Lib for technical indicators.
- scikit-learn and similar libraries for the models.

## Data sources

The course does not provide a dataset. You download the data yourself, which is part of the point.

- yfinance is the default. It is a free, unofficial Yahoo Finance library with data on thousands of tickers across many exchanges. It occasionally goes down, and its data is delayed by 15 to 20 minutes, which is fine for weekly or monthly predictions.
- Alpha Vantage is a paid source with a free tier of 25 API calls. It is worth it for fundamental data over long histories, which is close to impossible to scrape.
- polygon.io has a free tier and a paid one, and is used for news data.

Paid data starts to make sense at around 10 to 50 dollars per month if you are actually trading. If you are only learning, the free sources are enough.

Real-time streaming data is not used in the course. It costs money everywhere, and the course is meant to be free to complete.

## Automation and deployment

Later cohorts moved away from cloud and Docker so the focus stays on analysis and simulation.

A no-cloud setup that costs nothing:

- GitHub Actions for scheduled workflows.
- A local or hosted database for storing the data.
- Streamlit for the dashboard.

Cron jobs on your own machine and a simple SQLite database also work. The two prep workshops linked from [Resources]({{ '/courses/stock-markets-analytics-zoomcamp/resources/' | relative_url }}) walk through this setup end to end.

## Brokerage account

Optional. You do not need one to complete the course or the project. If you want to place the trades your model suggests, you need an account with a broker; the course shows interfaces from Interactive Brokers, Degiro, and Trade Republic. Banking apps that offer stock trading usually cover only a limited set of tickers.
