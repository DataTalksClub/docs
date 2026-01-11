---
description: Create an article from a transcript with illustration placeholders
arguments:
  - name: transcript
    description: Path to the transcript file
    required: true
---

# Create Article from Transcript

## Process Overview

Read the transcript file and create a well-structured article based on its content. Include illustration placeholders with estimated timestamps for later extraction from the video.

## Formatting Rules

### Header Structure
- Use `#` for the title only (first line)
- Use `##` for major sections
- Use `###` for subsections

### Dashes
- Always have spaces around dashes: ` – ` (en-dash)

### Section Dividers
- Never use `---` to divide sections

### Bold Formatting
- Keep bold to minimum
- Only use for essential emphasis (key warnings, critical points)
- Don't bold names, list items, or regular emphasis

### Illustration Placeholders

Format: `**[Illustration placeholder: description - timestamp ~MM:SS]**`

#### When Illustrations Are Needed

Only add illustrations when text alone is insufficient to understand what's happening:

- **UI screenshots**: Interfaces students need to navigate (GitHub repo, course platform, Slack, etc.)
- **Diagrams**: Architecture diagrams, flowcharts, system layouts described but not shown
- **Data visualizations**: Charts, graphs, plots containing key information
- **Code/terminal**: Actual code snippets or terminal output shown on screen
- **Technical concepts**: Docker containers, workflows, pipelines explained visually
- **Illustrative examples**: Sample outputs, posts, or results that demonstrate format
- **Complex relationships**: Mind maps or diagrams showing connections between topics

#### When Illustrations Are NOT Needed

Skip illustrations for:
- Simple lists or bullet points (even if presented as infographic in video)
- People photos or headshots (names are sufficient)
- Text-only explanations clearly described in words
- Decorative elements (logos, title cards, motivational graphics)
- Quotes or spoken content
- Things already visible in nearby illustrations
- Checklists when text already has numbered steps

#### Placement

- Place immediately before or after the relevant content
- Don't add redundant illustrations for the same thing
- Estimate timestamps based on content flow (rough percentage of total length)

#### Timestamp Estimates Are Approximate

**Important**: Timestamps in placeholders are estimates based on content flow. During illustration extraction:

1. **Extract frames** around the estimated timestamp (±5 seconds)
2. **Verify the frame matches** the article description - read the article text around the placeholder to understand what should be visible
3. **If mismatch occurs**: The timestamp estimate was wrong. Search the transcript for relevant keywords discussed in that section to find the actual timestamp
4. **Re-extract** from the corrected timestamp

Example: Article says "taxi trip data visualization" at ~12:00, but extracted frame shows GitHub repo. Search transcript for "taxi data" or "NYC taxi" to find where that topic was actually discussed (may be ~10:50 instead).

## Steps

0. **Check for timestamps**: The transcript MUST contain timestamps for illustration placement. If the transcript doesn't have timestamps (format like `0:00`, `1:23`, etc. on separate lines), DO NOT proceed - illustrations cannot be extracted without accurate timestamps.

1. Read the transcript file at `{{transcript}}`

2. Analyze the content and identify:
   - Main topics and sections
   - Key points and quotes
   - Natural breaks for illustrations
   - **Actual timestamps** from the transcript for each illustration topic
   - Overall narrative arc

3. Structure the article:
   - Title (clear, descriptive)
   - Introduction (what is this about)
   - Main sections (group related content)
   - Subsections as needed
   - Conclusion/final thoughts

4. Write the content:
   - Use clear, concise language
   - Preserve key quotes accurately
   - Maintain speaker voice where appropriate
   - Add illustration placeholders with **ACTUAL TIMESTAMPS FROM TRANSCRIPT** (not estimates)

5. Save to `_temp/` directory with descriptive filename

## Output Format

Save as markdown file in `_temp/`:
- Filename: `[topic-name].md`
- Title: `# Title`
- Sections: `## Section Name`
- Subsections: `### Subsection Name`
- Illustration placeholders: `**[Illustration placeholder: description - timestamp ~MM:SS]**`

## Content Guidelines

- Prioritize clarity over completeness
- Group related ideas together
- Use lists for sequential information
- Preserve important quotes in blockquotes
- Keep paragraphs short (3-5 sentences)
- Use tables for structured comparisons when appropriate
