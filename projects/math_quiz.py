import random 
import time
import mysql.connector
def connect_database():
  try:
    connect=mysql.connector.connect(host='localhost',user='root',password='7896',database='mathquiz_record')
    mycursor=connect.mycursor()
  except:
    print("Database error")
  mycursor.execute('use mathquiz_record')
  mycursor.execute('create table leaderboard(id int auto_increment primary key not null,name varchar(30) not null,)')
  
  

noOfTurns=10
def game(min,max):
  operators=["+","-","//","*"]
  leftNo=random.randint(min,max)
  rightNo=random.randint(min,max)
  middle=random.choice(operators)
  expr=str(leftNo) +" " + middle + " " + str(rightNo)
  answer=eval(expr)
  return expr,answer
wrong=0
choice=int(input("This is a fun math guessing game\nPress select the difficulty\n1.Easy\n2.Medium\n3.Hard\nSelect your Choice: "))
if(choice==1):
  min,max=1,15
elif(choice==2):
  min,max=10,25
elif(choice==3):
  min,max=30,50
else:
  print("Wrong Choice")
  exit(0)
def main():
  start= time.time()
  print("---------------------------------------------")
  for i in range(noOfTurns):
    expr,ans=game(min,max)
    while True:
      guess=input(f"Question no #{i+1}: {expr} = ")
      if guess == str(ans):
        break
      else:
        wrong+=1
        print("Wrong answer")
  print("---------------------------------------------")  
  end=time.time()
  totaltime=round(end-start,1)
  print(f"You completed the game in {totaltime} secs")
  if wrong!=0:
    print(f"You did {wrong} wrong attempts")
  print("---------------------------------------------") 