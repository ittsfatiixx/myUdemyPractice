import tkinter
from tkinter import END,ttk


def convert_to():
       metric_values ={
              'femto':10**-15,
              'pico':10**-12,
              'nano':10**-9,
              'micro':10**-6,
              'milli':10**-3,
              'centi':10**-2,
              'deci':10**-1,
              'base value':10**0,
              'deca':10**1,
              'hecto':10**2,
              'kilo':10**3,
              'mega':10**6,
              'giga':10**9,
              'tera':10**12,
              'peta':10**15}
       op_entry .delete (0,END)
       base_val=float(ip_entry .get ())*metric_values[from_list .get ()]
       ans=base_val/metric_values[to_list .get ()]
       op_entry .insert (0,ans)

#defne root window
root=tkinter .Tk()
root.config (bg='brown')
root.iconbitmap('ruler.ico')
root.title ('Metric converter')

#def widgets
ip_entry=tkinter.Entry()
ip_entry .insert(0,'Enter value to convert')
op_entry=tkinter.Entry ()
eq_label=tkinter.Label (text='=',bg='brown')
ip_entry.grid(row=0,column=0,padx=5,pady=5)
eq_label .grid (row=0,column=1,padx=5,pady=5)
op_entry .grid (row=0,column=2,padx=5,pady=5)

unit_lst=['femto' , 'pico' , 'nano', 'micro', 'milli', 'centi', 'deci', 'base value', 'deca', 'hecto', 'kilo', 'mega', 'giga', 'tera', 'peta']


from_list=ttk.Combobox(root,value=unit_lst )
from_list.set ('base value')
to_list=ttk.Combobox(root,value=unit_lst )
to_list .set ('base value')

from_list .grid(row=1,column=0,padx=5,pady=5)
tkinter.Label(root,text='To',bg='brown') .grid(row=1,column=1,padx=5,pady=5)
to_list .grid(row=1,column=2,padx=5,pady=5)

convert_btn=tkinter.Button (root,bg='grey',text='Convert',command=convert_to)
convert_btn .grid(row=2,column=0,columnspan=3)

#def methods

root.mainloop ()
