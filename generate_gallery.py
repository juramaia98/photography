#!/usr/bin/env python3
"""
Automatically generates gallery.json from images in a folder.
Run this script whenever you add new images to your gallery.
"""

import os
import json
from PIL import Image

# Configuration
IMAGES_FOLDER = 'images'
OUTPUT_FILE = 'gallery.json'
SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}

def is_portrait(image_path):
    """Check if an image is portrait orientation."""
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return height > width
    except Exception as e:
        print(f"Warning: Could not read dimensions for {image_path}: {e}")
        return False

def generate_gallery_json():
    """Generate gallery.json from images in the specified folder."""
    
    if not os.path.exists(IMAGES_FOLDER):
        print(f"Error: {IMAGES_FOLDER} folder not found!")
        print(f"Please create the folder and add your images.")
        return
    
    images = []
    
    # Get all image files from the folder
    files = sorted(os.listdir(IMAGES_FOLDER))
    
    for filename in files:
        # Check if file has a supported image extension
        ext = os.path.splitext(filename)[1].lower()
        if ext not in SUPPORTED_FORMATS:
            continue
        
        image_path = os.path.join(IMAGES_FOLDER, filename)
        
        # Skip if not a file
        if not os.path.isfile(image_path):
            continue
        
        # Determine if image is portrait
        is_portrait_img = is_portrait(image_path)
        
        # Create image entry
        image_entry = {
            "filename": filename,
            "alt": os.path.splitext(filename)[0].replace('-', ' ').replace('_', ' '),
            "portrait": is_portrait_img
        }
        
        images.append(image_entry)
        print(f"Added: {filename} ({'portrait' if is_portrait_img else 'landscape'})")
    
    if not images:
        print(f"No images found in {IMAGES_FOLDER} folder!")
        return
    
    # Create gallery data
    gallery_data = {
        "images": images
    }
    
    # Write to JSON file
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(gallery_data, f, indent=2)
    
    print(f"\n✓ Generated {OUTPUT_FILE} with {len(images)} images!")
    print(f"Commit and push to update your gallery.")

if __name__ == "__main__":
    generate_gallery_json()