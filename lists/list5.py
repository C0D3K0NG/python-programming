# Write a program using map ( ) function to create a list of squares of numbers in the
# range 1-10.


numbers=range(1,11)

squares=list(map(lambda x:x**2,numbers))
print(squares)