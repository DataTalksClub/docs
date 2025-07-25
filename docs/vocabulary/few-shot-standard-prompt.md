---
layout: vocabulary_term
title: Few-Shot Standard Prompt
parent: Vocabulary
description: Standard prompts that have exemplars in them. Exemplars are examples of the task that the prompt is trying to solve, which are included in the prompt itself.
related_terms:
  - title: Prompt
    url: /docs/vocabulary/prompt
  - title: Zero-Shot Prompt
    url: /docs/vocabulary/zero-shot-prompt
lectures:
  - title: LLM Zoomcamp - Module 1 - Introduction to LLMs and RAG
    url: /docs/llm-zoomcamp/module-01-introduction/
---

## Examples

A few-shot standard prompt might look like:

```
Classify the following text as positive or negative:

Example 1:
Text: "I love this product, it works great!"
Classification: Positive

Example 2:
Text: "This is the worst purchase I've ever made."
Classification: Negative

Example 3:
Text: "It's okay, but not worth the price."
Classification: Negative

Now classify:
Text: "The customer service was excellent and they resolved my issue quickly."
Classification:
```

In this example, three exemplars are provided before asking the model to classify a new text.

## Benefits

Few-shot prompting helps the model understand the specific format and style of response you're looking for. It can significantly improve performance on tasks where the model might otherwise be uncertain about what's expected.

## When to Use

- When you need the model to follow a specific format
- For classification tasks with specific categories
- When consistency in output style is important
- When the task might be ambiguous without examples 