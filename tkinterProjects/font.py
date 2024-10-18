from tkinter import *

root=Tk()
fonts=['MS Serif','MS Sans Serif','Small Fonts','Bell Gothic Std Black','Bell Gothic Std Light','Eccentric Std','Stencil Std','Tekton Pro','Tekton Pro Cond','Tekton Pro Ext','Trajan Pro','Rosewood Std Regular','Prestige Elite Std','Poplar Std','Orator Std','Minion Pro Cond','Mesquite Std','Lithos Pro Regular','Kozuka Mincho Pro H']
for fontg in fonts:
  text=Label(root,text=fontg,font=(fontg,22,'bold')).pack()
root.mainloop()