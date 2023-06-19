import csv
import requests
import os

from time import sleep
from slugify import slugify

from multiprocessing import Pool, cpu_count

# downnload image function
def download_image_url(uri):
    image_url = uri[1]
    output_path = uri[0]
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


# function to get list url from csvs, default directory "images"
def get_filename_url(csv_file, output_directory="images"):

    # column index title (to use for renaming)
    title_column_index = 0

    # column index image URLs
    image_url_start_index = 2

    listurl = []

    # Read the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)

        # Iterate over each row in the CSV file
        for row in reader:
            title = row[title_column_index]
            # Check if title is empty or contains invalid characters
            if not title or any(char in title for char in r'\/:*?"<>|'):
                print(f'Skipping invalid title: {title}')
                continue

            # Extract only the allowed characters for the filename
            title = ''.join(char for char in title if char.isalnum() or char in [' ', '_', '-'])

            # loop for images each row
            for i in range(image_url_start_index, len(row)):
                image_url = row[i]

                # check if value not empty
                if image_url:
                    if i == 2:
                        filename = slugify(title)
                    else:
                        filename = f"{slugify(title)}_{i - 1}"
                    output_path = f"{output_directory}/{filename}.jpg"
                    
                    # append all for return value
                    listurl.append([output_path, image_url])
                else:
                    print("empty url")

    return listurl


if __name__ == '__main__':
    # CSV file path
    csv_file = 'data/sample.csv'
    uri = get_filename_url(csv_file)

    # for multiprocessing
    pool = Pool(cpu_count() * 2)
    pool.map(download_image_url, uri)
