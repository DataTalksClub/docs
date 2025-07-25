---
layout: vocabulary_term
title: Retrieval-Augmented Generation (RAG)
parent: Vocabulary
description: Retrieval-Augmented Generation (RAG) is a technique that enhances language models by retrieving relevant information from external knowledge sources and incorporating it into the generation process. This allows LLMs to access up-to-date or domain-specific information beyond their training data.
related_terms:
  - title: Large Language Model (LLM)
    url: /docs/vocabulary/large-language-model
  - title: Prompt
    url: /docs/vocabulary/prompt
lectures:
  - title: LLM Zoomcamp - Module 1 - Introduction to LLMs and RAG
    url: /docs/llm-zoomcamp/module-01-introduction/
---

## How RAG Works

1. **Query Processing**: The user's query is processed and analyzed
2. **Retrieval**: Relevant documents or information are retrieved from a knowledge base
3. **Context Enhancement**: The retrieved information is combined with the original query
4. **Generation**: The enhanced context is sent to the LLM, which generates a response

## Benefits of RAG

- **Accuracy**: Reduces hallucinations by grounding responses in factual information
- **Up-to-date Knowledge**: Provides access to information beyond the model's training cutoff
- **Domain Expertise**: Can incorporate specialized knowledge from specific domains
- **Transparency**: Sources can be cited, making the system more trustworthy and verifiable

## Components of a RAG System

- **Document Store**: A database or vector store containing the knowledge base
- **Retriever**: A system that finds relevant documents based on queries
- **Generator**: The LLM that produces the final response
- **Orchestrator**: Coordinates the flow between components

## Use Cases

- Question answering systems
- Customer support chatbots
- Research assistants
- Documentation search tools
- Educational applications 