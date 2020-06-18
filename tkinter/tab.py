import tkinter as tk
from tkinter import ttk


app = tk.Tk() 

tab_parent = ttk.Notebook(app)
tab_parent.pack(expand=1, fill='both')

tab1 = ttk.Frame(tab_parent)
tab_parent.add(tab1, text='Tab One')
tab2 = ttk.Frame(tab_parent)
tab_parent.add(tab2, text='Tab Two')

label1 = tk.Label(tab1, text = "Первый таб")
label1.pack()

label2 = tk.Label(tab2, text = "Второй таб")
label2.pack()

app.mainloop()