import csv
import requests
import os

from time import sleep
from slugify import slugify

# downnload image function
def download_image_url(filename, image_url, output_directory):
    output_path = f"{output_directory}/{filename}.jpg"
    if not os.path.exists(output_path):
        print("path ok")
        try:
            r = requests.get(image_url)
            sleep(.2)
        except requests.exceptions.ConnectionError as e:
            print(e)

        if r.status_code == 200:
            print('Processing.. ', image_url)
            with open(output_path, 'wb') as f:
                f.write(r.content)

    else:
        print("exist")


# CSV file path
csv_file = 'data/sample.csv'

# column index title (to use for renaming)
title_column_index = 0

# column index image URLs
image_url_start_index = 2

# directory to save the downloaded images
output_directory = 'images'

# Read the CSV file
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    # Iterate over each row in the CSV file
    for row in reader:
        title = row[title_column_index]
        # Check if title is empty or contains invalid characters
        if not title or any(char in title for char in r'\/:*?"<>|'):
            print(f'Skipping invalid title: {title}')
            continue

        # Extract only the allowed characters for the filename
        title = ''.join(char for char in title if char.isalnum() or char in [' ', '_', '-'])

        for i in range(image_url_start_index, len(row)):
            image_url = row[i]
            if image_url:
                if i == 2:
                    filename = slugify(title)
                else:
                    filename = f"{slugify(title)}_{i - 1}"
                download_image_url(filename, image_url, output_directory)
            else:
                print("empty url")

