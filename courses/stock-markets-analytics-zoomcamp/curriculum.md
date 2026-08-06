---
title: "Curriculum"
layout: default
nav_order: 3
parent: Stock Market Analytics Zoomcamp
has_children: false
---

# Curriculum

The Stock Market Analytics Zoomcamp covers five modules plus a final project. Each module has a lecture and a homework assignment.

The modules build on each other. You start with data sources, combine them into one dataset, train a model on it, define a trading strategy on top of the predictions, and finally automate the whole workflow.

For the canonical curriculum (videos, code, exact homework), see the [GitHub repository](https://github.com/DataTalksClub/stock-markets-analytics-zoomcamp).

## Modules

[Module 1: Introduction and Data Sources](https://github.com/DataTalksClub/stock-markets-analytics-zoomcamp/tree/main/01-intro-and-data-sources)

- Data-driven decisions, the mindset of a long-term investor versus a short-term trader, and the landscape of personal investment options.
- Risk and reward.
- Setting up Google Colab and downloading your first financial data with yfinance.
- Choosing APIs as the primary data source, free versus paid, plus a brief look at web scraping and alternative data.

[Module 2: Working with the Data in Pandas](https://github.com/DataTalksClub/stock-markets-analytics-zoomcamp/tree/main/02-dataframe-analysis)

- Numpy, pandas, matplotlib, seaborn, and Plotly Express.
- Data types and manipulation, and the specifics of time series data.
- Feature generation: growth over different periods, hour and day of week, and technical indicators through TA-Lib.
- Data cleaning, joining multiple datasets, and descriptive and correlation analysis.

[Module 3: Analytical Modeling](https://github.com/DataTalksClub/stock-markets-analytics-zoomcamp/tree/main/03-modeling)

- Framing a hypothesis and turning it into a prediction problem.
- Heuristics and hand rules before any machine learning, which is where classical technical analysis fits.
- Time series predictions: trend, seasonality, and remainder.
- Regression and binary classification for the direction of growth, with neural networks as an optional extra.
- Feeding a large set of generated technical indicators into a model instead of hand-picking a few.

[Module 4: Trading Strategy and Simulation](https://github.com/DataTalksClub/stock-markets-analytics-zoomcamp/tree/main/04-trading-strategy-and-simulation)

- What a trading strategy adds on top of a model: when to trade, at what size, how to combine predictions, and how to time entry.
- Trading fees and why they decide whether a high-frequency idea can work at all.
- Strategy examples: single stock investment, diversified portfolios, market-neutral long and short positions, mean reversion, pairs trading, dividend strategies, and basic options.
- Simulating financial results on historical data, with metrics that differ from the model quality metrics of Module 3.
- Screenshots from real trading platforms such as Interactive Brokers and Degiro.

[Module 5: Deployment and Automation](https://github.com/DataTalksClub/stock-markets-analytics-zoomcamp/tree/main/05-deployment-and-automation)

- Moving from Colab notebooks to Python files that run from the command line.
- Persistent storage: files versus a simple database.
- Scheduling the workflow with cron jobs, GitHub Actions, or a workflow tool.
- Generating predictions systematically and monitoring the result, including email or chat notifications.

[Project](https://github.com/DataTalksClub/stock-markets-analytics-zoomcamp/tree/main/projects)

- Two weeks of work on your own project, then one week of peer review.

## Outside the scope

Some topics are deliberately left out:

- High-frequency and real-time trading. Real-time data is a paid product, and the course is designed to be free to complete.
- Connecting to a broker API to place trades automatically. The workflow produces a list of tickers you act on yourself.
- Market microstructure, personal finance management, and portfolio or risk management as standalone topics.

## Homework and project

Each module has a homework assignment. Most questions have a numeric or multiple-choice answer, with a few open-ended ones. Homework is scored and shown on the leaderboard, but it is not required for the certificate. To earn the certificate you complete the project and review three peers' projects during a live cohort. See [Project]({{ '/courses/stock-markets-analytics-zoomcamp/project/' | relative_url }}).

Each homework submission accepts up to 3 learning-in-public links, one point each. See [Learning in Public]({{ '/courses/zoomcamp-logistics/learning-in-public/' | relative_url }}).
