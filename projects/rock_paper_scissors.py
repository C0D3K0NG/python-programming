import random
#functions
def roll():
  return (random.randint(0,2))
turns_real=['Rock','Paper','Scissors']
def user_input():
  while True:
    try:
      user_turn = int(input("\nEnter ur turn: "))
      if 1 <= user_turn <= 3:
        return user_turn
      else:
        print("Enter between 1 and 3\n1.ROCK  2.PAPER  3.SCISSORS")
    except ValueError:
      print("Wrong input, try again")

def turns_input():
  while True:
    n= input("\nEnter the no. of turns: ").strip()
    if n.isdigit():
      n = int(n)
      return n
    print("Wrong input,try again")
score_human=score_com=0


#intro
name=input("Enter your name: ")

print("|------------------------------|")
print("|Welcome to Rock,paper,Scissors|")
print("|------------------------------|")
print()
print("======================================================================")
print(f"Hello {name},lets go through the rules and guidelines first.")
print("======================================================================")
print("Rules for playing this game")
print("Press appropriate buttons for choosing between turns")
print("1.ROCK  2.PAPER  3.SCISSORS")
print("U are playing against the bot")
print("U can call how many times u want to play")
print("If the bot scores more than you then you will lose")
print("Please dont throw this console on losing")


#main game
turns=turns_input()
print(f"The match will be played for {turns} turns")
for i in range(1,turns+1):
  cc=roll()                 #computer choice of rock,paper,scissors
  print(f"Turn no.{i}||1.ROCK  2.PAPER  3.SCISSORS")
  pc=user_input()-1          #player choice of rock,paper,scissors
  print("---------------------------------------------------------")
  print(f"The Player chose {turns_real[pc]} and computer chose {turns_real[cc]}")
  if cc==0:
    if pc==0:
      print("Its a draw")
    elif pc==1:
      print(f"{name} got {score_human+1} points")
      score_human+=1
    else:
      print(f"Bot got {score_com+1} points")
      score_com+=1
  elif cc==1:
    if pc==0:
      print(f"Bot got {score_com+1} points")
      score_com+=1
    elif pc==1:
      print("Its a draw")
    else:
      print(f"{name} got {score_human+1} points")
      score_human+=1
  else:
    if pc==0:
      print(f"{name} got {score_human+1} points")
      score_human+=1
    elif pc==1:
      print(f"Bot got {score_com+1} points")
      score_com+=1
    else:
      print("Its a draw")
  print("---------------------------------------------------------")
      
if(score_com>score_human):
    print(f"\nBot won against you in {score_com-score_human} points")
elif(score_human>score_com):
    print(f"\n{name} won against bot in {score_human-score_com} points")
else:
    print("The game is a draw")