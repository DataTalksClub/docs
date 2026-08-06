---
title: "Q&A"
layout: default
nav_order: 8
parent: Stock Market Analytics Zoomcamp
has_children: false
---

# Questions and Answers

Questions about the scope and philosophy of this course, collected from the cohort launch sessions. For general zoomcamp logistics, see [Zoomcamp Logistics]({{ '/courses/zoomcamp-logistics/' | relative_url }}). For module-specific and technical issues, check the [Stock Market Analytics Zoomcamp FAQ](https://datatalks.club/faq/stock-markets-analytics-zoomcamp.html).

## Automated trading bots

The course does not build a bot that places trades on its own. It ends at a workflow that produces a list of tickers to buy or sell, which you then act on manually. Connecting to a broker API and automating execution would take roughly as many lectures again as the course already has.

Keeping a human in the loop is also good practice: check the predictions against the previous week's output before money moves.

## Real-time and high-frequency trading

Not covered. Real-time data costs money everywhere, and the course is designed to be completable for free. Predictions in the course are made once per day, with a prediction horizon of a week or a month.

Everything you learn does apply to faster setups, but you would be paying for the data. And with high trade frequency, broker fees quickly eat the returns.

## Trading fees

Fees matter more than most people expect. In the instructor's own experience of a 40 percent return over two months, roughly a third of the return went to commissions. Fees are the first thing to consider when designing an algorithmic strategy: trade only on the predictions you are most confident in, or limit the number of trades.

## Crypto, forex, and non-US markets

All of them work. Any stock exchange available through Yahoo Finance is fair game, including Indian and European markets; you may need to convert positions to a common currency if you mix them.

Crypto works too, with one caveat. The macroeconomic and fundamental data sources used for stocks do not apply, so you would use technical indicators instead. ETFs, futures, and commodities are also possible, though derivatives need historical data that is expensive to get.

## News and sentiment analysis

Covered only in passing. The instructor wrote articles on it and did not find a strategy that worked. News histories long enough to model are paid, coverage is biased toward big companies, and articles usually appear after the move has already happened.

You can still use sentiment as a project feature. Expect to work with two to five years of data rather than the 25 years available for prices.

## Quant jobs

This course does not prepare you for one directly. Quant hiring runs through multi-stage competitions that test math and problem-solving speed rather than the analysis skills taught here.

Real experience does help: if you build something you run with your own money, that is credible in a way a portfolio project is not.

## Brokerage account

Not needed. No homework or project requires one. It does change how you engage with the material, though, because betting real money makes you think much harder about what your model actually claims.

## AI tools

Allowed, for homework and for the project. AI-assisted coding removes barriers when you do not know a library, and it gets you to a working baseline quickly. It is much weaker at the parts that matter here: optimizing models, improving prediction quality, and connecting the pieces into something that works end to end. Use it, but check the output. See [Using AI Tools]({{ '/courses/zoomcamp-logistics/ai-usage/' | relative_url }}).

## Taking two zoomcamps in parallel

Possible, but demanding. Each course is 10 to 15 hours per week, so two of them mean 20 to 30 hours on top of a job. Doable if your schedule genuinely has the room.

## Solo versus group work

Projects are solo, as in all DataTalks.Club zoomcamps. It scales better and peer review is much easier. You are encouraged to discuss ideas in Slack, form study groups, and hold each other accountable, but the code you submit must be your own.

## Finishing early

You can work through the modules and even build the project as fast as you like. The project can only be submitted once the window opens, though, and peer review happens for everyone in the same week, so the certificate does not come earlier. See [Certification]({{ '/courses/zoomcamp-logistics/certification/' | relative_url }}).

## Value of the certificate

The certificate is a PDF with your name and the instructors' signatures, plus a unique URL you can add to LinkedIn. It does not replace a university degree. The project behind it does the convincing: it is public, and any analyst or trader can look at it.

## Profitability

There are no guarantees. The course teaches how to do the analysis, not what to buy or when. Losses are possible, the instructors are not professional market participants or licensed advisers, and nothing in the course is investment advice.
