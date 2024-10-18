import time
input_time=int(input("Enter time in seconds: "))

for i in range(input_time,0,-1):
  if(i>59): 
    print(f"{i//60}m:",end="")
    
  if(i%60==0):
    print(f"00s")
    time.sleep(1)
    continue
  if(i>59):
    print(f"{i%60}s")
  else:
    print(f"{i}s")
  time.sleep(1)
