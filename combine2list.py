import csv

first_list = [[1, "jane"], [2, "adam"], [3, "john"]]
second_list = [["jane", "montana"], ["jane", "anime"], ["jane", "high school"], ["adam", "london"],["adam","netflix"],["john", "new york"],["john", "skate"],["john", "high school"]]

combined_list = []

for sublist in first_list:
    combined_sublist = sublist.copy()
    matching_elements = [element[1] for element in second_list if element[0] == sublist[1]]
    combined_sublist.extend(matching_elements)
    combined_list.append(combined_sublist)

# Write the combined list to a CSV file
with open('data/output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(combined_list)

print("Output saved to output.csv")
