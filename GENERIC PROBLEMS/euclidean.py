x1,x2,x3=map(float,input("Enter coordinates of x: ").split())
y1,y2,y3=map(float,input("Enter coordinates of y: ").split())
result=pow((pow(x1-y1,2)+pow(x2-y2,2)+pow(x3-y3,2)),0.5)
print(f"The result is {result:.2f}")