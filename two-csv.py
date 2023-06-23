import csv
import re

from slugify import slugify

data_dir =  "data"

first_list = []
# list judul
with open(f"{data_dir}/media1.sample.csv", "r") as f_file:
    fc_reader = csv.reader(f_file)
    for fc_row in fc_reader:
        first_list.append(fc_row)

second_list = []
# list gambar dari google drive berserta id ya
with open(f"{data_dir}/media2.sample.csv", "r") as sc_file:
    sc_reader = csv.reader(sc_file)
    for sc_row in sc_reader:
        second_list.append(sc_row)


combined_list = []

for sublist in first_list:

    matching_elements = []
    for element in second_list:
        title = sublist[0]
        filename = re.sub(r"_[^.]+", "", element[0]).split(".")[0]
        if slugify(title) == filename:
            matching_elements.append(element[1])

    sublist.extend(matching_elements)
    combined_list.append(sublist)

with open(f'{data_dir}/media.output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(combined_list)

print("Output saved to media.output.csv")
