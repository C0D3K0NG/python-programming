#string input version 1
def strinp1():
  fruits=[]
  print("Enter Fruits or 'done' to exit: ")
  while True:
    fruit=input()
    if fruit=='done':
      break
    fruits.append(fruit)
    
  for fruit in fruits:
      print(fruit)
#string input version 2
def strinp2():
  def pri(fruits): 
    print("\nThe fruits are:-") 
    for fruit in fruits:
      print(fruit)
  fru = []
  print("Enter Fruits or press enter to exit: ")
  while True:
    fruit = input()
    if fruit == '':
        break
    fru.append(fruit.upper())
  pri(fru)
#string input version 3
def strinp3():
  def pri(*fruits,sep=' '): 
    print("\nThe fruits are:-") 
    print(sep.join(fruits))
  fru = []
  print("Enter Fruits or press enter to exit: ")
  while True:
      fruit = input()
      if fruit == '':
          break
      fru.append(fruit.upper())
  pri(*fru)
#string input version 4
def strinp4():
  def pri(*fruits): 
    print("\nThe fruits are:-") 
    for fruit in fruits:
      print(fruit.upper())

  fru=[]
  fru=map(str,input("Enter the fruits divided by spaces: ").split())
  pri(*fru)





#implementation space