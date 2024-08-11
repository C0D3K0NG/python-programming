# Define the list correctly
my_list = [4, 6, 7, 2, 8, 9]

# Take input from the user
a = int(input("Enter a number to search: "))

# Check if the number exists in the list
if a in my_list:
    print("Search found")
else:
    print("Search not found")
