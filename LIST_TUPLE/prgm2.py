# Write a Python program that creates a list of 10 random integers. Then create two lists-
# Odd list and Even List that has all odd and even values in the list respectively.

import random

random_list = [random.randint(1, 100) for _ in range(10)]
odd_list = [num for num in random_list if num % 2 != 0]
even_list = [num for num in random_list if num % 2 == 0]

print("Random List:", random_list)
print("Odd List:", odd_list)
print("Even List:", even_list)
