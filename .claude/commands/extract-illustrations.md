---
description: Extract frames from video around timestamp and select best illustration
arguments:
  - name: video
    description: Path to video file
    required: true
  - name: timestamp
    description: Timestamp in MM:SS or HH:MM:SS format (estimated)
    required: true
  - name: name
    description: Illustration name (used for directory: _temp/frames/{name}/)
    required: true
  - name: description
    description: What content we're looking for (helps selection)
    required: true
  - name: context
    description: Article text around the illustration (for verification)
    required: true
---

# Extract Illustration Frames from Video

## Dependencies

- **ffmpeg** - For extracting keyframes from video
- **ImageMagick** (convert command) - For cropping and JPEG conversion

Install if needed:
```bash
# Windows (with Chocolatey)
choco install ffmpeg imagemagick

# macOS (with Homebrew)
brew install ffmpeg imagemagick

# Linux (Ubuntu/Debian)
sudo apt install ffmpeg imagemagick
```

## Process Overview

Extract keyframes in a narrow window around the timestamp, remove duplicates, then select the best frame for the article illustration.

## Steps

### 0. Setup Aliases

```bash
# Arguments: video=$1, timestamp=$2, name=$3, description=$4, context=$5
video=$1
timestamp=$2
name=$3
description=$4
context=$5
```

### 1. Create Output Directories (Parallel-Safe)

```bash
# Create dedicated directory for this illustration extraction
mkdir -p "_temp/frames/$name"
mkdir -p _temp/illustrations
```

### 2. Extract Frames Using FFmpeg

**First, try keyframes (natural scene changes):**

```bash
# Seek to timestamp, then extract keyframes from ±5 second window
ffmpeg -ss $timestamp -i "$video" -ss -00:00:05 -t 00:00:10 \
  -vf "select=eq(pict_type\,I)+setpts=N/TB" -vsync 0 \
  "_temp/frames/$name/%{pts:hms}.png"
```

This produces files like: `00_09_47.321.png` where the timestamp is the actual video time.

**Check if we got any keyframes:**
```bash
ls "_temp/frames/$name/" | wc -l
```

**If 0 keyframes found, extract 7 specific frames at exact offsets:**

```bash
# Extract frames at: -2, -1, -0.5, 0, +0.5, +1, +2 seconds
# Example: for timestamp 10:00, extract at 9:58, 9:59, 9:59.5, 10:00, 10:00.5, 10:01, 10:02

# Calculate timestamps based on $timestamp - adjust these values for your timestamp
# For $timestamp = 10:00:
ffmpeg -ss 00:09:58 -i "$video" -vframes 1 "_temp/frames/$name/00_09_58.000.png"
ffmpeg -ss 00:09:59 -i "$video" -vframes 1 "_temp/frames/$name/00_09_59.000.png"
ffmpeg -ss 00:09:59.5 -i "$video" -vframes 1 "_temp/frames/$name/00_09_59.500.png"
ffmpeg -ss 00:10:00 -i "$video" -vframes 1 "_temp/frames/$name/00_10_00.000.png"
ffmpeg -ss 00:10:00.5 -i "$video" -vframes 1 "_temp/frames/$name/00_10_00.500.png"
ffmpeg -ss 00:10:01 -i "$video" -vframes 1 "_temp/frames/$name/00_10_01.000.png"
ffmpeg -ss 00:10:02 -i "$video" -vframes 1 "_temp/frames/$name/00_10_02.000.png"
```

### 3. Remove Duplicate Frames (keyframes only)

First pass: Remove exact duplicates by file size:

```python
from pathlib import Path

frames_dir = Path("_temp/frames/$name")
sizes = {}
for f in frames_dir.glob("*.png"):
    size = f.stat().st_size
    if size not in sizes:
        sizes[size] = f
    else:
        f.unlink()  # Remove duplicate

print(f"After dedup: {len(sizes)} unique frames")
```

Second pass: Remove visually similar frames (optional, if still too many):

```python
from PIL import Image
import numpy as np

frames = sorted(Path("_temp/frames/$name").glob("*.png"))
to_remove = set()

for i in range(len(frames) - 1):
    img1 = np.array(Image.open(frames[i]))
    img2 = np.array(Image.open(frames[i + 1]))

    # Simple difference: mean absolute error
    diff = np.abs(img1.astype(float) - img2.astype(float)).mean()

    # Threshold: if difference < 5% of pixel range, consider duplicate
    if diff < 12.75:  # 255 * 0.05
        to_remove.add(frames[i + 1])

for f in to_remove:
    f.unlink()

print(f"After visual dedup: {len(frames) - len(to_remove)} frames remaining")
```

### 4. Review Remaining Frames and Verify Match

Read each frame and evaluate based on:

**Selection Criteria:**
- **Clarity**: Text is readable, not motion-blurred
- **Completeness**: Full content visible (no cut-off elements)
- **Relevance**: Shows exactly what the description asks for
- **Visual Quality**: Good contrast, no visual artifacts
- **UI State**: Buttons/menus in clear, useful state

**Verification Step (CRITICAL - MUST use analyze_image tool):**

The `Read` tool alone CANNOT reliably verify image content. You MUST use the `analyze_image` tool with a detailed prompt.

**What is analyze_image?**
- A tool that analyzes images and returns detailed text descriptions
- Can read text, identify UI elements, describe layouts, and understand content
- Takes two parameters:
  - `imageSource`: URL of the image to analyze
  - `prompt`: What question to ask about the image

**Verification Process:**

1. **Use analyze_image with a dynamic prompt based on description and context:**

```
We expect this image to show: $description

Context from article: $context

Please analyze:
1. What does this image actually show? (describe type of page, main text, content)
2. Does this match what we expect? If not, what DOES it show?
3. For cropping: any browser chrome at top (how many pixels to remove)? Sidebars to crop?
```

2. **Compare the analyze_image output:**
   - The prompt tells the tool what we EXPECT (from $description)
   - The tool tells us what it ACTUALLY sees
   - Compare: Does the actual content match the expected content?

3. **Decision based on comparison:**
   - If the content matches → Proceed to save
   - If the content does NOT match → Wrong timestamp. Search transcript for keywords to find correct time.

**Example verification using analyze_image:**

Prompt expects: "Certificate example showing requirements: complete final project successfully, participate in peer reviews"

analyze_image result: "This is a Q&A interface from Slido... showing anonymous user questions about getting DE jobs without degrees"

Verdict: MISMATCH - The image shows Slido Q&A, NOT certificate requirements. Timestamp is wrong.

**Common verification failures (detected by analyze_image):**
- Article says "Docker & Infrastructure" → Image shows "Course logistics"
- Article says "Certificate example" → Image shows "Slido Q&A interface"
- Article says "YouTube channel" → Image shows only "LinkedIn"
- Article says "Project pipeline" → Image shows "GitHub repo/commits"

**Timestamp Proximity Rule:**
- We ONLY look within ±5 seconds of target timestamp - never more
- Frame names include ACTUAL timestamp (e.g., `09_58.png`, `10_00.png`, `10_02.png`)
- This makes it obvious the exact video time each frame represents

### 5. Select Best Frame

After reviewing all frames:
1. Identify the best frame
2. Explain why it was chosen
3. Note if cropping is needed

### 6. Crop if Necessary (using ImageMagick)

If the best frame needs cropping:

```bash
# First crop to temp filename to assess
convert "_temp/frames/$name/keyframe_XXXX.png" -crop {width}x{height}+{x}+{y} "_temp/frames/$name/keyframe_XXXX-cropped.png"

# Read and assess the cropped version, then finalize
convert "_temp/frames/$name/keyframe_XXXX-cropped.png" -quality 85 "_temp/illustrations/$name.jpg"
```

Common crop patterns:
- Browser chrome removal: `-crop 1280x650+0+70` (remove ~70px from top)
- Sidebars: Adjust width/x-offset to crop left or right

### 7. Clean Up

```bash
rm -rf "_temp/frames/$name"
```

## Selection Guidelines by Content Type

| Content Type | What to Look For |
|--------------|------------------|
| **UI Screenshots** | No loading spinners, fully populated data, clear labels |
| **Diagrams** | Complete diagram, no cutting off edges, clear text |
| **Code/Terminal** | Complete commands visible, no partial lines |
| **People** | Faces visible, not mid-blink, natural expression |
| **Data Visualizations** | Axes/labels visible, clear data points |
| **Websites/Pages** | Fully loaded, no broken images, header visible |

## Output Format

Save final illustration as:
- Filename: `[descriptive-name].jpg`
- Location: `_temp/illustrations/`
- Format: JPEG at quality 85 (~65% smaller than PNG)
- Reasoning: Document why this frame was chosen
