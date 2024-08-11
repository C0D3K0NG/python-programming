a,b,c=map(int,input("Enter three numbers(divided by spaces): ").split())
if a==b or b==c or c==a:
  print("Two numbers are equal")
elif a==b and b==c:
  print("Three numbers are equal")

if a>=b and a>=c:
  print(f"The max of three terms is {a}")
elif b>=a and b>=c:
  print(f"The max of three terms is {b}")
elif c>=a and c>=b:
  print(f"The max of three terms is {c}")