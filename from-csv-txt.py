import csv
import os


# csv and txt path. gunakan
# gunakan `data = "."` jika folder sama dengan file .py
data_dir = "data"

# Read the combined list from the CSV file
combined_list = []
with open(f"{data_dir}/output.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        combined_list.append(row)

# Create a text file for each row in the combined list
for row in combined_list:
    name = row[1]
    address = row[2]
    others = row[3:]

    # Create the filename based on the name
    filename = f'{name}.txt'

    # Prepare the content of the text file
    content = f'name: {name}\naddress: {address}\nothers:\n'
    for item in others:
        content += f'  - {item}\n'

    # Write the content to the text file
    with open(f'{data_dir}/{filename}', 'w') as txt_file:
        txt_file.write(content)

print("Text files created successfully.")
