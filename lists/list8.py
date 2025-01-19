# Write a Python program to take an input list and removes the element at index 4
# and add it to the 2nd position and also, at the end of the list.


input_list = input("Enter elements separated by spaces: ").split()
input_list = [int(x) for x in input_list]

print("Original List:", input_list)

element = input_list.pop(4)


input_list.insert(1, element)
input_list.append(element)

print("Modified List:", input_list)
