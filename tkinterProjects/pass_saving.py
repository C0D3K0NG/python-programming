from tkinter import *
from pathlib import Path
root=Tk()
path = Path('c:/Users/rajde/Documents/Password')
def add():
    file_name=str(uservalue.get())+'.txt'
    with open(path/file_name,'w') as f:
      f.write(passvalue.get())
    print(f"Account {uservalue.get()} is saved with password {passvalue.get()}")
      
root.geometry("400x200")
root.minsize(400,200)
root.title("Password Keeper")
user=Label(text="Username").grid(row=0,column=0)
password=Label(text="Password").grid(row=1,column=0)
uservalue=StringVar()
passvalue=StringVar()
user_input=Entry(root,textvariable=uservalue).grid(row=0,column=1)
pass_input=Entry(root,textvariable=passvalue).grid(row=1,column=1)
Button(text="Submit", command=add).grid()
root.mainloop()