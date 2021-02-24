import tkinter
from tkinter import *
root=Tk()

l1=Label(root,text="Date")
l1.grid(row=0,column=0)
l2=Label(root,text="Study")
l2.grid(row=0,column=2)
l3=Label(root,text="exercise")
l3.grid(row=1,column=0)
l4=Label(root,text="Diet")
l4.grid(row=1,column=2)
l5=Label(root,text="Python")
l5.grid(row=2,column=0)

date_txt=StringVar()
e1=Entry(root,textvariable=date_txt)
e1.grid(row=0,column=1)

study_txt=StringVar()
e2=Entry(root,textvariable=study_txt)
e2.grid(row=0,column=3)

exer_txt=StringVar()
e3=Entry(root,textvariable=exer_txt)
e3.grid(row=1,column=1)

diet_txt=StringVar()
e4=Entry(root,textvariable=diet_txt)
e4.grid(row=1,column=3)

py_txt=StringVar()
e5=Entry(root,textvariable=py_txt)
e5.grid(row=2,column=1)





root.mainloop()