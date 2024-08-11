a,b,c=map(int,input("Enter a,b,c seperated by spaces: ").split())
d=b*b-4*a*c
s=d**0.5
if(a==0):
  print("Equation not applicable")
elif(d==0):
  print(f"Roots are real and equal, the root is: {-b/2*a}")
elif(d>0):
  print(f"Roots are real and distinct,the roots are: {(-b+s)/2*a},{(-b-s)/2*a}")
else:
  print("Roots are imaginary")