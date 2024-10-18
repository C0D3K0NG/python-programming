from tkinter import *
root=Tk()
root.geometry("300x500")
root.minsize(100,100)
f1= Frame(root,bg="#66b3ff",relief=SUNKEN,borderwidth=5)
f1.pack(side=LEFT,fill=Y)
tex=Label(f1,text="Hello",bg="#66b3ff",fg="white",font="comicsans 20 bold",padx=60,pady=60)
tex.pack(anchor=E,side=RIGHT) #This make the text in center idk how

root.mainloop()