n=int(input("Enter three digit number to reverse: "))
print(((n%10)*100)+(((n//10)%10)*10)+(n//100))