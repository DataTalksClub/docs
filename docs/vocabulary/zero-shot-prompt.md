---
layout: vocabulary_term
title: Zero-Shot Prompt
parent: Vocabulary
description: A prompt that does not include any examples of the task being requested. The model must perform the task without seeing any demonstrations of what is expected.
related_terms:
  - title: Prompt
    url: /docs/vocabulary/prompt
  - title: Few-Shot Standard Prompt
    url: /docs/vocabulary/few-shot-standard-prompt
lectures:
  - title: LLM Zoomcamp - Module 1 - Introduction to LLMs and RAG
    url: /docs/llm-zoomcamp/module-01-introduction/
---

## Examples

A zero-shot prompt might look like:

```
Classify the following text as positive or negative:

"The customer service was excellent and they resolved my issue quickly."
```

In this example, no examples of classifications are provided, and the model must rely on its pre-trained knowledge to perform the task.

## Benefits

Zero-shot prompting is simpler and requires less prompt engineering. It works well when:
- The task is common and straightforward
- The model has likely seen similar tasks during training
- You want to test the model's inherent capabilities

## When to Use

- For simple, common tasks that the model likely understands
- When you want to minimize prompt length
- When testing a model's baseline capabilities
- For tasks where providing examples might bias the model's output 