import random

def bal():
  min=1
  max=6
  return random.randint(min,max)
def toss():
  return random.randint(0,1)
def game():
  score=over=0
  while True:
    if over==6:
      print(f"The total runs uptil now:{score}")
      over=0
    bat=input("Take Strike: ")
    if bat.isdigit():
      bat=int(bat)
      if not 1<=bat<=6:
        print("Strike between 1 to 6")
        continue
      ball=bal()
      if ball!=bat:
        score+=bat
        over+=1
        continue
      else:
        print(f"{ball} is thrown to u")
        break
    else:
      print("Strike between 1 to 6")
      continue
  return score
def game2(num):
  score=over=0
  while True:
    if score>num:
      break
    if over==6:
      print(f"The total runs uptil now:{score}")
      over=0
    bat=input("Take Strike: ")
    if bat.isdigit():
      bat=int(bat)
      if not 1<=bat<=6:
        print("Strike between 1 to 6")
        continue
      ball=bal()
      if ball!=bat:
        score+=bat
        continue
      else:
        print(f"{ball} is thrown to u")
        break
    else:
      print("Strike between 1 to 6")
      continue
  return score 

print("|-----------------------|")  
print("|WELCOME TO HAND CRICKET|")
print("|-----------------------|")
print("It is a match for two players so please mention your Names")
player1=input("Player 1: ")
player2=input("Player 2: ")
run1=run2=0

print("Lets toss:-")

if toss():
    print(f"------------------------------------------")
    print(f"{player1} won the toss")
    print(f"------------------------------------------")
    while True:
      choice=input(f"Select {"bat"} or {"ball"}: ")
      if(choice=="bat"):
        print(f"------------------------------------------")
        print(f"{player1} start batting:-")
        print(f"------------------------------------------")
        run1=game()
        print(f"The total score by {player1} is {run1},{player2} need {run1+1} needs to win")
        print(f"------------------------------------------")
        print(f"{player2} will bat now")
        print(f"------------------------------------------")
        run2=game2(run1)
        break
      elif(choice=="ball"):
        print(f"------------------------------------------")
        print(f"{player2} start batting:-")
        print(f"------------------------------------------")
        run2=game()
        print(f"The total score by {player2} is {run2},{player1} need {run2+1} needs to win")
        print(f"------------------------------------------")
        print(f"{player1} will bat now")
        print(f"------------------------------------------")
        run1=game2(run2)
        break
      else:
        print(f"Please select {"bat"} or {"ball"}")
        continue
else:
    print(f"------------------------------------------")
    print(f"{player2} won the toss ")
    print(f"------------------------------------------")
    while True:
      choice=input(f"Select {"bat"} or {"ball"}: ")
      if(choice=="bat"):
        print(f"------------------------------------------")
        print(f"{player2} start batting:-")
        print(f"------------------------------------------")
        run2=game()
        print(f"The total score by {player2} is {run2},{player1} need {run2+1} needs to win")
        print(f"------------------------------------------")
        print(f"{player1} will bat now")
        print(f"------------------------------------------")
        run1=game2(run2)
        break
      elif(choice=="ball"):
        print(f"------------------------------------------")
        print(f"{player1} start batting:-")
        print(f"------------------------------------------")
        run1=game()
        print(f"The total score by {player1} is {run1},{player2} need {run1+1} needs to win")
        print(f"------------------------------------------")
        print(f"{player2} will bat now")
        print(f"------------------------------------------")
        run2=game2(run1)
        break
      else:
        print(f"Please select {"bat"} or {"ball"}")
        continue
if run1>run2:
  print(f"{player1} won the game by {run1-run2}")
elif run1<run2:
  print(f"{player2} won the game by {run2-run1}")
else:
  print(f"Its a tie")

  
    
    