sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
unique_list = []

for item in sample_list:
    if item not in unique_list:
        unique_list.append(item)

print("Unique List:", unique_list)
