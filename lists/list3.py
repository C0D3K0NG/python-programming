# Write a Python function to sum all the numbers in a list.
# Sample List: (8, 2, 3, 0, 7)
# Expected Output: 20

listn=[8,2,3,0,7]
sum=0
for x in range(0,len(listn)):
    sum+=listn[x]
print(sum)