# Write a Python program that has a list of both positive and negative numbers. Create
# another list using filter ( ) that has only positive values.

list1=[-1,4,7,-9,8,-3,-2,9,-5]

positive_list=list(filter(lambda x:x>0,list1))
print(positive_list)