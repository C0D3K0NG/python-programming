from tkinter import *
from pathlib import Path
root=Tk()
path= Path("C:/Users/rajde/Documents/GitHub/PYTHON LANGUAGE/tkinterProjects/data.txt")
root.geometry("500x300")
root.minsize(500,300)

def data():
  with open(path,'a') as f:
      f.write(f"\nName= {namevalue.get()} Year = {yearvalue.get()} Sem = {semvalue.get()} Roll= {rollvalue.get()}")


welcome=Label(root,text="Welcome to Tkinter",font="comicsans 30 bold",fg="black").grid(row=0,column=3)

name=Label(root,text="Name",fg="black",font="comicsans 15 bold",padx=10).grid(row=1,column=2)
year=Label(root,text="Year",fg="black",font="comicsans 15 bold",padx=10).grid(row=2,column=2)
roll=Label(root,text="Roll",fg="black",font="comicsans 15 bold",padx=10).grid(row=3,column=2)
sem=Label(root,text="Sem",fg="black",font="comicsans 15 bold",padx=10).grid(row=4,column=2)

namevalue=StringVar()
yearvalue=IntVar()
rollvalue=IntVar()
semvalue=IntVar()

name_input=Entry(root,textvariable=namevalue).grid(row=1,column=3)
year_input=Entry(root,textvariable=yearvalue).grid(row=2,column=3)
roll_input=Entry(root,textvariable=rollvalue).grid(row=3,column=3)
sem_input=Entry(root,textvariable=semvalue).grid(row=4,column=3)

submit=Button(root,text="Submit",fg="black",font="comicsans 10 bold",command=data).grid(row=5,column=2)
root.mainloop()