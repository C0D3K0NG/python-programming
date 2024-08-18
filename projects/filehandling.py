from pathlib import Path
#set path
path = Path('c:/Users/rajde/Documents/Password')
master_pass=input("Enter the master password: ")
if master_pass=="7896":
  
  def add():
    file_name=str(input("What is the password for: "))+'.txt'
    with open(path/file_name,'w') as f:
      f.write(input("Enter the password: "))

  def view():
      files = [file.stem for file in path.iterdir() if file.is_file()]
      print("The files in this folder are: ")
      print("-----------------------------------------------")
      for file in files:
          print(file)
      print("-----------------------------------------------")
      choice=input()
      file_name = str(input("Which password do you want to view: ")) + '.txt'
      for file in files:
        if file_name == file:
          with open(path / file_name, 'r') as f:
              print(f.read())
              return
      print("Wrong file name")

      

  while True:
    print("\n1.Add a password\n2.View a password\n3.Exit")
    choice=int(input("Enter what You want to do: "))
    if choice==1:
      add()
    elif choice==2:
      view()
    elif choice==3:
      break
else:
  print("Password is invalid!")