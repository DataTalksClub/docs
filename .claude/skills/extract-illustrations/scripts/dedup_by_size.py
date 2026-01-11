#!/usr/bin/env python3
"""
Remove duplicate frames by file size.

Frames with identical file sizes are likely exact duplicates.
This is a fast first-pass deduplication before visual similarity check.

Usage:
    python dedup_by_size.py <frames_directory>

Example:
    python dedup_by_size.py _temp/frames/leaderboard
"""

import sys
from pathlib import Path


def dedup_by_size(frames_dir):
    """
    Remove duplicate frames based on file size.
    
    Args:
        frames_dir: Path to directory containing PNG frames
    """
    frames_dir = Path(frames_dir)
    sizes = {}
    
    print(f"Checking for duplicates by file size in: {frames_dir}")
    
    for f in frames_dir.glob("*.png"):
        size = f.stat().st_size
        if size not in sizes:
            sizes[size] = f
        else:
            f.unlink()
            print(f"  Removed duplicate: {f.name} (same size as {sizes[size].name})")
    
    print(f"After dedup: {len(sizes)} unique frames")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python dedup_by_size.py <frames_directory>")
        sys.exit(1)
    
    dedup_by_size(sys.argv[1])
