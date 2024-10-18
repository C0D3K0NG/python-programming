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
      file_name = str(input("Which password do you want to view: ")) + '.txt'
      files = [file.name for file in path.iterdir() if file.is_file()]
      for file in files:
        if file_name == file:
          with open(path / file_name, 'r') as f:
              print(f.read())
              return
      print("Wrong file name")
  def delete():
      files = [file.stem for file in path.iterdir() if file.is_file()]
      print("The files in this folder are: ")
      print("-----------------------------------------------")
      for file in files:
          print(file)
      print("-----------------------------------------------")
      del_file=str(input("What file You want to delete: "))+'.txt'
      files = [file.name for file in path.iterdir() if file.is_file()]
      for file in files:
        if del_file == file:
          pth=Path(path/del_file)
          pth.unlink()
          print(f"{del_file} has been deleted.")
          return
      print("No Such file is there to delete")
      

  while True:
    print("\n1.Add a password\n2.View a password\n3.Delete a password\n4.Exit")
    choice=int(input("Enter what You want to do: "))
    if choice==1:
      add()
    elif choice==2:
      view()
    elif choice==3:
      delete()
    elif choice==4:
      break
else:
  print("Password is invalid!")