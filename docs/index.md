---
title: "How To Contribute"
layout: default
nav_order: 3
description: "Course notes and resources for DataTalks.Club Zoomcamps"
has_children: true
---

# How To Contribute
{: .fs-9 }

Welcome to the DataTalks.Club Zoomcamps Notes repository! This is a community-driven resource that helps thousands of learners worldwide. Your contributions make a real difference in supporting fellow data enthusiasts on their learning journey.

## Ways to Contribute

- Contribute course notes and summaries
- Report typos, grammatical errors, or unclear explanations
- Fix broken links and outdated information
- Correct technical inaccuracies
- Improve existing explanations with better examples
- Add visual aids like diagrams or screenshots
- Reorganize content for better flow and readability

## Detailed Contribution Process

### 1. Getting Started

#### Prerequisites
- GitHub account
- Basic knowledge of Git and Markdown
- Familiarity with the course content you want to contribute to

#### **Repository Setup**
1. **Fork the Repository**: Click the "Fork" button on the main repository page
2. **Clone Your Fork**: 
   ```bash
   git clone https://github.com/YOUR_USERNAME/zoomcamps-notes-faq.git
   cd zoomcamps-notes-faq
   ```
3. **Add Upstream Remote**:
   ```bash
   git remote add upstream https://github.com/DataTalksClub/zoomcamps-notes-faq.git
   ```

### 2. Making Changes

#### **Branch Creation**
Always create a new branch for your changes:
```bash
git checkout -b feature/your-contribution-description
```

Use descriptive branch names like:
- `fix/ml-zoomcamp-week3-typos`
- `add/data-engineering-kafka-notes`
- `improve/llm-zoomcamp-rag-examples`

#### **Content Guidelines**

**Writing Style**:
- Use clear, concise language
- Write in an educational, friendly tone
- Include practical examples and real-world applications
- Structure content with proper headings and bullet points

**Technical Content**:
- Test all code examples before submitting
- Include necessary imports and dependencies
- Add comments explaining complex logic
- Provide context for when and why to use specific approaches

**Formatting Standards**:
- Use consistent Markdown formatting
- Follow the existing file structure and naming conventions
- Include proper front matter for new pages
- Optimize images and use appropriate alt text

### Submitting Your Contribution

#### **Commit Best Practices**
- Write clear, descriptive commit messages
- Make atomic commits (one logical change per commit)
- Use conventional commit format when possible:
  ```
  feat: add machine learning zoomcamp week 5 notes
  fix: correct linear regression formula in week 2
  docs: improve contribution guidelines
  ```

#### **Pull Request Process**
1. **Push Your Branch**:
   ```bash
   git push origin your-branch-name
   ```

2. **Create Pull Request**:
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Select your branch and the main repository's main branch
   - Fill out the pull request template

3. **Pull Request Description Should Include**:
   - Clear title summarizing the changes
   - Detailed description of what was added/changed
   - Context for why the change is beneficial
   - Any relevant issue numbers
   - Screenshots for visual changes

## Content Organization

### Repository Structure
```
docs/
├── machine-learning-zoomcamp/
│   ├── 01-intro/
│   ├── 02-regression/
│   └── ...
```

---

*Questions? Join our [Slack community](https://datatalks.club/slack.html) and ask in the `#general` channel or the course-specific channels. Our community is always happy to help new contributors get started!*