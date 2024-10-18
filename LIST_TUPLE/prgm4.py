# Write a Python program to take an input list and removes the element at index 4
# and add it to the 2nd position and also, at the end of the list.

input_list = [10, 20, 30, 40, 50, 60, 70]

element = input_list.pop(4)
input_list.insert(2, element)
input_list.append(element)

print(input_list)
