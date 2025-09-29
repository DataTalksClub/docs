import os
import csv
import re
from urllib.parse import urlparse, parse_qs

# Function to extract YouTube video ID from URL
def extract_video_id(url):
    parsed_url = urlparse(url)
    if parsed_url.netloc == 'www.youtube.com' or parsed_url.netloc == 'youtube.com':
        if parsed_url.path == '/watch':
            return parse_qs(parsed_url.query)['v'][0]
        elif 'embed' in parsed_url.path:
            return parsed_url.path.split('/')[-1]
    elif parsed_url.netloc == 'youtu.be':
        return parsed_url.path[1:]
    return None

# Function to create folder if it doesn't exist
def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")

# Function to format the title from filename
def format_title(filename):
    # Remove file extension
    name = os.path.splitext(filename)[0]
    # Extract the number prefix if it exists
    num_prefix = re.search(r'^(\d+)-', name)
    prefix = ""
    if num_prefix:
        prefix = f"{num_prefix.group(1)}. "
        # Remove leading numbers and hyphens (like 01-)
        name = re.sub(r'^\d+-', '', name)
    # Replace hyphens with spaces
    name = name.replace('-', ' ')
    # Capitalize words
    return prefix + ' '.join(word.capitalize() for word in name.split())

# Function to format module name
def format_module_name(folder):
    # Remove leading numbers (like 01)
    module_num = re.search(r'^(\d+)', folder)
    if module_num:
        module_number = module_num.group(1)
        # Remove the hyphen if it exists
        module_name = re.sub(r'^\d+-', '', folder)
        # Replace hyphens with spaces
        module_name = module_name.replace('-', ' ')
        # Capitalize words
        module_name = ' '.join(word.capitalize() for word in module_name.split())
        return f"Module {module_number}: {module_name}"
    else:
        # If no leading number, just capitalize
        return ' '.join(word.capitalize() for word in folder.replace('-', ' ').split())

# Function to create index.md file for a module
def create_index_file(module_folder, module_name):
    index_path = os.path.join(module_folder, 'index.md')
    # Extract module number for nav_order
    module_num = re.search(r'Module (\d+)', module_name)
    nav_order = int(module_num.group(1)) if module_num else 1
    
    with open(index_path, 'w') as f:
        f.write(f"""---
title: "{module_name}"
nav_order: {nav_order}
has_children: true
---

# {module_name}

This module covers the following topics:

""")
    print(f"Created index file: {index_path}")

# Function to create markdown file for a video
def create_md_file(module_folder, filename, video_url, module_name, order):
    md_path = os.path.join(module_folder, filename)
    title = format_title(filename)
    video_id = extract_video_id(video_url)
    
    # Extract file number for nav_order if it exists
    file_num = re.search(r'^(\d+)', os.path.splitext(filename)[0])
    nav_order = int(file_num.group(1)) if file_num else order
    
    with open(md_path, 'w') as f:
        f.write(f"""---
title: "{title}"
parent: "{module_name}"
nav_order: {nav_order}
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
""")
    print(f"Created markdown file: {md_path}")

# Main function
def main():
    base_dir = 'docs/machine-learning-zoomcamp'
    csv_file = 'youtube_links.csv'
    
    # Read CSV file
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        
        # Group by folder
        folder_files = {}
        for row in reader:
            folder, filename, video_url = row
            if folder not in folder_files:
                folder_files[folder] = []
            folder_files[folder].append((filename, video_url))
    
    # Create folders and files
    for folder, files in folder_files.items():
        module_name = format_module_name(folder)
        module_folder = os.path.join(base_dir, folder)
        
        # Create module folder
        create_folder_if_not_exists(module_folder)
        
        # Create index.md for the module
        create_index_file(module_folder, module_name)
        
        # Create markdown files for each video
        for i, (filename, video_url) in enumerate(files):
            create_md_file(module_folder, filename, video_url, module_name, i + 1)

if __name__ == "__main__":
    main()
