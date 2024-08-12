def dec1():
  def greet(name):
    return f"Hello {name}!"
  def welcome(name):
    return f"{greet(name)}, Welcome to our platform!"

  name= input("Enter your name: ")
  print(welcome(name))

def dec2():
  def greet(name):
    return f"Hello {name}!"
  def welcome_fnc(func):
    def welcome(name):
      return f"{func(name)}, Welcome to our platform!"
    return welcome
  gettext=welcome_fnc(greet)
  name= input("Enter your name : ")
  print(gettext(name))

#implementation area
dec2()  