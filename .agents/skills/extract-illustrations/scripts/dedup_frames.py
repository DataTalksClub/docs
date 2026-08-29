#!/usr/bin/env python3
"""
Remove visually similar frames from a directory of PNG images.

Calculates pixel-wise difference between consecutive frames.
If difference is below threshold, removes the later frame.

Usage:
    python dedup_frames.py <frames_directory>

Example:
    python dedup_frames.py _temp/frames/leaderboard
"""

import sys
from pathlib import Path
from PIL import Image
import numpy as np


def dedup_frames(frames_dir, threshold=12.75):
    """
    Remove visually similar frames.
    
    Args:
        frames_dir: Path to directory containing PNG frames
        threshold: Mean absolute error threshold (default: 12.75 = 5% of 255)
                   Lower = more aggressive dedup, Higher = keep more frames
    """
    frames_dir = Path(frames_dir)
    frames = sorted(frames_dir.glob("*.png"))
    
    if len(frames) < 2:
        print(f"Only {len(frames)} frame(s) found. Nothing to dedup.")
        return
    
    to_remove = set()
    
    print(f"Analyzing {len(frames)} frames for visual similarity...")
    
    for i in range(len(frames) - 1):
        img1 = np.array(Image.open(frames[i]))
        img2 = np.array(Image.open(frames[i + 1]))
        
        # Calculate mean absolute error between frames
        diff = np.abs(img1.astype(float) - img2.astype(float)).mean()
        
        # If difference is below threshold, mark second frame for removal
        if diff < threshold:
            to_remove.add(frames[i + 1])
            print(f"  Similar: {frames[i].name} -> {frames[i+1].name} (diff={diff:.2f})")
    
    # Remove duplicates
    for f in to_remove:
        f.unlink()
        print(f"  Removed: {f.name}")
    
    kept = len(frames) - len(to_remove)
    print(f"\nResult: {kept} frames kept ({len(to_remove)} removed)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python dedup_frames.py <frames_directory> [threshold]")
        sys.exit(1)
    
    frames_dir = sys.argv[1]
    threshold = float(sys.argv[2]) if len(sys.argv) > 2 else 12.75
    
    dedup_frames(frames_dir, threshold)
