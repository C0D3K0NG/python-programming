# Write a Python program to check if all items of Tuple are the same or not.

tuple1=(1,1,1,1,1,1,1,1,1)
if len(tuple1)==tuple1.count(tuple1[0]):
    print("All items are same")
else:
    print("All item are not same")