---
title: "Asking Questions"
layout: default
nav_order: 15
parent: Zoomcamp Logistics
description: "How to ask for help in DataTalks.Club zoomcamp Slack channels."
---

# Asking Questions

If you have a course question, ask it in the course-specific Slack channel. Use the course FAQ first, then post in Slack if you still need help. Do not ask technical questions in Telegram; Telegram is for announcements.

Course channels and FAQs:

- Data Engineering Zoomcamp: [`#course-data-engineering`](https://app.slack.com/client/T01ATQK62F8/C01FABYF2RG), [FAQ](https://datatalks.club/faq/data-engineering-zoomcamp.html).
- Machine Learning Zoomcamp: [`#course-ml-zoomcamp`](https://app.slack.com/client/T01ATQK62F8/C0288NJ5XSA), [FAQ](https://datatalks.club/faq/machine-learning-zoomcamp.html).
- MLOps Zoomcamp: [`#course-mlops-zoomcamp`](https://app.slack.com/client/T01ATQK62F8/C02R98X7DS9), [FAQ](https://datatalks.club/faq/mlops-zoomcamp.html).
- LLM Zoomcamp: [`#course-llm-zoomcamp`](https://app.slack.com/client/T01ATQK62F8/C06TEGTGM3J), [FAQ](https://datatalks.club/faq/llm-zoomcamp.html).
- AI Dev Tools Zoomcamp: [`#course-ai-dev-tools-zoomcamp`](https://app.slack.com/client/T01ATQK62F8/C09HWT76L95).
- Stocks Analytics Zoomcamp: [`#course-stocks-analytics-zoomcamp`](https://datatalks-club.slack.com/archives/C06L1RTF10F).

For Slack norms that apply across all DataTalks.Club channels, see [Community Guidelines]({{ '/general/guidelines/' | relative_url }}) and [Slack channels]({{ '/general/slack/' | relative_url }}). For which channel to use for what, see [Communication Channels]({{ '/courses/zoomcamp-logistics/communication/' | relative_url }}).

## Before Asking

Try to narrow the problem first. You do not need to solve it alone, but a few minutes of investigation makes it much easier for others to help.

1. Read the error message carefully. Check whether it names a file, line number, missing dependency, missing environment variable, port conflict, or permission problem.
2. Check the course FAQ and the module README.
3. Search Slack for the exact error message.
4. Search the web using the tool name and the core error text.
5. Check the documentation for the tool you are using.
6. Restart the application, notebook kernel, Docker container, or terminal session if the problem looks state-related.
7. If the setup may be broken, try reinstalling or recreating the environment, then record what changed.

It is normal for technical problems to take time. If you are stuck after trying the steps above, ask in Slack.

## How to Ask in Slack

Start a new message in the course channel with a short problem summary. Then put details in a thread so the main channel stays readable.

Include:

- What you are trying to do.
- The module, lesson, homework, or project step you are working on.
- The exact command you ran.
- The full error message as text.
- Your operating system.
- Your Python version, Docker version, or tool version when relevant.
- What you already tried.
- A link to your GitHub repository if the problem depends on your code.

Use triple backticks for code, commands, and error output:

<pre><code>```
paste the error here
```</code></pre>

## What to Avoid

- Do not post screenshots of code or error messages when text is available.
- Do not take photos of your screen with a phone.
- Do not tag instructors for ordinary troubleshooting questions.
- Do not create multiple posts for the same issue.
- Do not delete the question after it is solved. Other students may need the same answer later.

Screenshots are useful only when the visual state matters, such as a browser UI, dashboard, form, or chart. Even then, also include the relevant text and context.

## Threads

Use the same thread for the whole conversation. If the error output is long, put it in the thread rather than the main channel message.

If the issue reappears later, you can start a new post. Explain what changed since the previous issue: new module, new machine, different command, updated dependency, recreated environment, or different data.

## After You Get an Answer

Reply with what fixed the problem. If the answer is useful and missing from the FAQ, contribute it back:

- For public DataTalks.Club FAQ pages, use the [FAQ proposal form](https://github.com/DataTalksClub/faq/issues/new?template=faq-proposal.yml).
- For course-specific Google Docs FAQs, add the answer there if the course team allows edits, or post the suggested FAQ entry in Slack.

This keeps future students from getting stuck on the same issue.
