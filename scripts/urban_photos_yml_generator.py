import os
import yaml

site_dir = '/home/empathyforgiveness/max_website/max-website/'

# Directory containing images
image_dir = site_dir + 'assets/photography/urban'

# List to store image filenames
urban_photos = []

# Loop through files in the directory
for filename in os.listdir(image_dir):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        urban_photos.append(filename)

# Write to photos.yml
with open(site_dir + '_data/urban_photos.yml', 'w') as file:
    yaml.dump(urban_photos, file, default_flow_style=False)
