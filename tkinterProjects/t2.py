from tkinter import *
root=Tk()
root.geometry("500x300")
root.maxsize(2000,300)
root.minsize(300,300)
tex=Label(text="READY",bg="black",fg="red",font="comicsansms 30 bold",borderwidth=8, relief=GROOVE)
tex.pack(side=BOTTOM,fill=X,padx=10,pady=10)
root.mainloop()