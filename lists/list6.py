# Write a Python program to generate number of terms in the Fibonacci sequence and
# store it in the list. Then find the sum of the even-valued terms.

terms=int(input("How many terms should be generated: "))

fibonacci_list=[]
a=0
b=1
for i in range(0,terms):
    fibonacci_list.append(a)
    a,b=b,a+b
print(fibonacci_list)

evensum=sum(x for x in fibonacci_list if x%2==0)
print("Even sum is: ",evensum)