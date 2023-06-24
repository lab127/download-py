import csv
import re
import random

from datetime import datetime, timedelta
from slugify import slugify

def get_brand(title):
    if re.match(r'^(?=.*\bapple?\b).*$', title, re.I):
        brand = "apple"
    elif re.match(r'^(?=.*\bsamsung?\b).*$', title, re.I):
        brand = "samsung"
    else:
        brand = "android"
    
    return brand


# buat random date post
def generate_random_date(start_date, end_date):
    # Calculate the time range in seconds
    time_range = (end_date - start_date).total_seconds()

    # Generate a random number of seconds to add to the start date
    random_seconds = random.randint(0, int(time_range))

    # Calculate the random date
    random_date = start_date + timedelta(seconds=random_seconds)

    # Format the random date with timezone offset
    formatted_date = random_date.strftime("%Y-%m-%dT%H:%M:%S%z")

    return formatted_date


# Usage
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 6, 24)


# csv and txt path. gunakan
# gunakan `data = "."` jika folder sama dengan file .py
data_dir = "data"

# Read the combined list from the CSV file
pdata = []
with open(f"{data_dir}/output.sample.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        pdata.append(row)

# Create a text file for each row in the combined list
for row in pdata:
    title = re.sub('^[^a-zA-Z]', '', row[0])
    datepost = generate_random_date(start_date, end_date)
    tag = row[1]
    weight = row[2]
    info = row[3]
    price = "{:0,.2f}".format(float(row[4]))
    images = row[5:]
    brand = get_brand(title)

    # Create the filename based on the name
    filename = f'{slugify(title)}.md'

    # Prepare the content of the text file
    content = '''\
---
title: "{title}"
date: {datepost}+07:00
collections: ["{tag}", "{brand}"]
brands: "{brand}"
grams: "{weight}"
description : "{title}"
price: "{price}"

google_drive:
  enable: true
  pics:
'''.format(title=title, datepost=datepost, tag=tag, brand=brand, weight=weight, price=price)
    for img in images:
        content += f'  - url: {img}\n'

    content += '''
draft: false
---

{info}
'''.format(info=info)
    
    # random date buat nama
    dt = datetime.fromisoformat(datepost)
    formatted_date = dt.strftime("%Y-%m-%d")

    # Write the content to the text file
    with open(f'{data_dir}/products/{formatted_date}-{filename}', 'w', encoding="utf-8") as txt_file:
        txt_file.write(content)

print("Text files created successfully.")
