numbers=[5,7,3,9,0]

# Adding elements
numbers.append(60)          # Adds 60 to the end
numbers.insert(2, 25)       # Inserts 25 at index 2

# Removing elements
numbers.remove(25)          # Removes the first occurrence of 25
numbers.pop(3)              # Removes the element at index 3
numbers.clear()             # Clears the entire list

# Finding elements
numbers.index(40)           # Returns the index of the first occurrence of 40
numbers.count(10)           # Counts the occurrences of 10

# Sorting and reversing
numbers.sort()              # Sorts the list in ascending order
numbers.reverse()           # Reverses the order of the list

# Copying a list
new_list = numbers.copy()   # Creates a shallow copy of the list
