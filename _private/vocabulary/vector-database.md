---
layout: vocabulary_term
title: Vector Database
parent: Vocabulary
description: A vector database is a specialized database designed to store, manage, and search vector embeddings - numerical representations of data like text, images, or audio. Vector databases are optimized for similarity search operations, making them essential for modern AI applications.
related_terms:
  - title: Retrieval-Augmented Generation (RAG)
    url: /docs/vocabulary/retrieval-augmented-generation
lectures:
  - title: LLM Zoomcamp - Module 1 - Introduction to LLMs and RAG
    url: /docs/llm-zoomcamp/module-01-introduction/
---

## What are Vector Embeddings?

Vector embeddings are numerical representations of data in a high-dimensional space. For text, these embeddings capture semantic meaning, allowing similar concepts to be positioned close to each other in the vector space.

For example, the embeddings for "dog" and "puppy" would be closer together than the embeddings for "dog" and "airplane".

## Key Features of Vector Databases

- **Similarity Search**: Find vectors that are most similar to a query vector
- **Approximate Nearest Neighbor (ANN) Algorithms**: Enable fast searches in high-dimensional spaces
- **Indexing Techniques**: Methods like HNSW (Hierarchical Navigable Small World) for efficient retrieval
- **Filtering**: Combine vector search with metadata filtering
- **Scalability**: Handle millions or billions of vectors efficiently

## Popular Vector Databases

- Pinecone
- Weaviate
- Milvus
- Qdrant
- Chroma
- FAISS (Facebook AI Similarity Search)
- Elasticsearch with vector search capabilities

## Use in RAG Systems

In RAG applications, vector databases store embeddings of documents or chunks of text. When a user query comes in:

1. The query is converted to a vector embedding
2. The vector database finds similar document embeddings
3. The corresponding documents are retrieved
4. These documents provide context for the LLM's response 