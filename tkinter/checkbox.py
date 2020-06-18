import tkinter as tk
from tkinter import ttk
from pprint import pprint

app = tk.Tk() 

# ------------ Label ---------
label1Top = tk.Label(app, text = "Нажми на Checkbox")
label1Top.pack()

def checkbutton_check():
    print('checkbox', var1.get())
    label1Top.config(text=var1.get())

# ---------- CheckBox ------------
var1 = tk.BooleanVar()
chb1 = tk.Checkbutton(app, text='Python', variable=var1, onvalue=True, offvalue=False, command=checkbutton_check)
chb1.pack()


app.mainloop()