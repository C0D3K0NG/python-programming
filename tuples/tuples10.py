# Write a Python program to replace the last value of tuples in a list with 100.
# Sample list: [(10,20,40), (40,50,60), (70,80,90)]
# Expected Output: [(10,20,100), (40,50,100), (70,80,100)]


sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

updated_list = [t[:-1] + (100,) for t in sample_list]
print(updated_list)
