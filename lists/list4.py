# Write a Python program that creates a list of 10 random integers. Then create two lists-
# Odd list and Even List that has all odd and even values in the list respectively.

import random
random_list=[]
even_list=[]
odd_list=[]

for i in range(0,10):
    random_list.append(random.randint(0,100))

print("Random list:",random_list)

for i in random_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("Odd list",odd_list)
print("even list",even_list)