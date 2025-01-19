# Write a Python program that has a list of numbers (both positive as well as
# negative). Make a new tuple that has only positive values from this list.
# Given list of numbers: 


tuple1=(-10, 1, 2, -9, 3, 4, -8, 5, 6)
positive_tuple=tuple(filter(lambda x:x>0,tuple1))
print(positive_tuple)
