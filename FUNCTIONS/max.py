a,b,c=map(int,input("Enter three numbers(divided by spaces): ").split())
def max_value(a, b):
   return a if a>b else b
def input(a,b,c):
  return max_value(max_value(a,b),c)
print(input(a,b,c))