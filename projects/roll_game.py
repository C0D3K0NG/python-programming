import random

def roll():
  min=1
  max=6
  return random.randint(min,max)
total=0
while True:
  print("\n\n1.Roll the dice\n2.Know the current score\n3.Exit the game")
  choice=int(input("Enter what You want to do: "))
  
  if choice==1:
    print("\nRolling the dice...")
    value=roll()
    print(f"u got {value}")
    total+=value
    if(value==1):
      print("u lose the game:( try again")
      total=0
    if total>=50:
      print("you won the game:)")
      total=0
  elif choice==2:
    print(f"The total score u got until now is {total}")
  elif choice==3:
    break
  
    
    