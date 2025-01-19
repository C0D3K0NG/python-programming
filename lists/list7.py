# Write a Python function to multiply all the numbers in a list.
# Sample List: [8, 2, 3, -1, 7]
# Expected Output: -336

listn=[8,2,3,-1,7]
result=1
for x in range(0,len(listn)):
    result*=listn[x]
print(result)