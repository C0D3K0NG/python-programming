n=(int(input("Enter a number to check it is armstrong or not: ")))
p=q=n
count=sum=0
while(p>0):
  count+=1
  p=p//10
while(q>0):
  sum+=(q%10)**count
  q=q//10
if(sum==n):
  print("It is an armstrong number")
else:
  print("It is not an armstrong number") 
  