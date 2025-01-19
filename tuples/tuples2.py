# Write a Python program to swap two values using the tuple assignment.


value1 = input("Enter the first value: ")
value2 = input("Enter the second value: ")

print("\nBefore swapping:")
print(f"First value: {value1}")
print(f"Second value: {value2}")

value1, value2 = value2, value1


print("\nAfter swapping:")
print(f"First value: {value1}")
print(f"Second value: {value2}")
