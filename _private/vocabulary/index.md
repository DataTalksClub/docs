---
layout: default
title: Vocabulary
nav_order: 5
has_children: true
permalink: /docs/vocabulary
---

# Vocabulary

This page contains key terms and definitions used throughout the courses. Each term includes its definition and links to lectures where it's mentioned.

<div class="vocabulary-grid">
{% assign sorted_terms = site.pages | where: "parent", "Vocabulary" | sort: "title" %}
{% for term in sorted_terms %}
  <div class="term-card">
    <h2><a href="{{ term.url | relative_url }}">{{ term.title }}</a></h2>
    <div class="term-definition">{{ term.description | truncatewords: 30 }}</div>
    <div class="term-card-footer">
      <a href="{{ term.url | relative_url }}" class="term-read-more">Read more →</a>
    </div>
  </div>
{% endfor %}
</div>

<style>
  .vocabulary-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
  }
  
  .term-card {
    height: 100%;
    display: flex;
    flex-direction: column;
  }
  
  .term-definition {
    flex-grow: 1;
  }
  
  .term-card-footer {
    margin-top: 1rem;
    text-align: right;
  }
  
  .term-read-more {
    font-size: 0.875rem;
    font-weight: 500;
    color: #2563eb;
    text-decoration: none;
  }
  
  .term-read-more:hover {
    text-decoration: underline;
  }
  
  @media (max-width: 800px) {
    .vocabulary-grid {
      grid-template-columns: 1fr;
    }
  }
</style> 