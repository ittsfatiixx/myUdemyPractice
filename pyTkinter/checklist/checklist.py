import tkinter
root = tkinter.Tk()

root.geometry('400x400')
root.resizable(0,0)
root_color='#79d2a6'
btn_color='#26734d'
my_font=('Times New Roman ',14)
root.iconbitmap('checklst.ico')

ip_frame=tkinter.Frame(root,bg=root_color)
op_frame=tkinter.Frame(root,bg=root_color)
btnFrame=tkinter.Frame(root)

ip_frame.pack()
op_frame.pack()
btnFrame.pack()
#ip frame widgets
add_txt=tkinter.Entry(ip_frame,width=35,border=6)
add_btn=tkinter.Button(ip_frame,width=10,text='Add item',fg='white',bg=btn_color)
add_txt.grid(row=0,column=0)
add_btn.grid(row=0,column=1)

#op frame 
mylist=tkinter.Listbox(op_frame,width=50,height=10)
mylist.grid(row=0,column=0,pady=10)

#btn frame
removeBtn=tkinter.Button(btnFrame,text='Remove Item')
clrList=tkinter.Button(btnFrame,text='CLear List')
save=tkinter.Button(btnFrame,text='Save list')
quit=tkinter.Button(btnFrame,text="Quit")

removeBtn.grid(row=0,column=0)
clrList.grid(row=0,column=1)
save.grid(row=0,column=2)
quit.grid(row=0,column=3)

root.config(bg=root_color)
root.mainloop()


