from tkinter import *
root=Tk()
def hello():
  print("Hello World!")
root.geometry("300x500")
root.minsize(300,500)
f1=Frame(root,bg="#66b3ff",borderwidth=8,relief=GROOVE,padx=10,pady=10)
f1.pack(anchor=NW)
b1=Button(f1,text="CLick",command=hello,padx=0,pady=0)
b1.pack()
root.mainloop()