#!/usr/bin/env python
import os
import re
import glob
import csv
import argparse

"""
This is a script for extracting a list of Modules, Topics and corresponding YouTube links from the original repository of ML Zoomcamp: https://github.com/DataTalksClub/machine-learning-zoomcamp
"""

def extract_youtube_links(file_path):
    """
    Extract YouTube links from markdown files that start with <a href=
    
    Args:
        file_path: Path to the markdown file
        
    Returns:
        List of YouTube URLs found in the file
    """
    youtube_links = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Look for lines starting with <a href=
                if line.strip().startswith('<a href='):
                    # Extract URL between quotes
                    match = re.search(r'<a href="([^"]+)"', line)
                    if match and 'youtube.com' in match.group(1):
                        youtube_links.append(match.group(1))
        
        return youtube_links
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return []

def process_folders(folder_list):
    """
    Process each folder in the list and extract YouTube links from markdown files.
    
    Args:
        folder_list: List of folder paths to process
        
    Returns:
        List of tuples containing (folder_name, file_name, youtube_url)
    """
    results = []
    
    for folder in folder_list:
        if not os.path.exists(folder):
            print(f"Folder not found: {folder}")
            continue
            
        # Find all markdown files in the folder
        md_files = glob.glob(os.path.join(folder, "*.md"))
        
        for md_file in md_files:
            file_name = os.path.basename(md_file)
            youtube_links = extract_youtube_links(md_file)
            
            for link in youtube_links:
                results.append((folder, file_name, link))
    
    return results

def main():
    parser = argparse.ArgumentParser(description='Extract YouTube links from markdown files in specified folders')
    parser.add_argument('--output', default='youtube_links.csv', help='Output CSV file path')
    
    args = parser.parse_args()
    
    # List of folders to process
    folders = [
        '01-intro',
        '02-regression',
        '03-classification',
        '04-evaluation',
        '05-deployment',
        '06-trees',
        '08-deep-learning',
        '09-serverless',
        '10-kubernetes',
        '11-kserve'
    ]
    
    print(f"Processing folders: {', '.join(folders)}")
    results = process_folders(folders)
    
    # Save results to CSV
    with open(args.output, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header
        csv_writer.writerow(['Folder', 'File', 'YouTube URL'])
        # Write data
        csv_writer.writerows(results)
    
    print(f"Found {len(results)} YouTube links")
    print(f"Results saved to {args.output}")

if __name__ == "__main__":
    main()
