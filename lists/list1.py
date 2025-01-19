#Write a Python function that takes a list and returns a new list with unique elements of
# the first list.
# Sample List: [1,2,3,3,3,3,4,5]
# Unique List: [1, 2, 3, 4, 5]



Sample_List=[1,2,3,3,3,3,4,5]
Unique_List=list(set(Sample_List))

print("Unique list: ",Unique_List)



sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
unique_list = []

for item in sample_list:
    if item not in unique_list:
        unique_list.append(item)

print("Unique List:", unique_list)
