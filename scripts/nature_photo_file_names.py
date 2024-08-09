import os
import yaml

site_dir = '/home/empathyforgiveness/max_website/max-website/'

# Directory containing images
image_dir = site_dir + 'assets/photography/nature'

# List to store image filenames
photos = []

# Loop through files in the directory
for filename in os.listdir(image_dir):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        photos.append(filename)

# Write to photos.yml
with open(site_dir + '_data/nature_photos.yml', 'w') as file:
    yaml.dump(photos, file, default_flow_style=False)
