import tkinter as tk
from tkinter import ttk

app = tk.Tk() 

def rb_click():
    print()

country = tk.IntVar()
rb1 = tk.Radiobutton(app, text='Russia', value=1, variable=country, padx=15, pady=10, command=rb_click)
rb1.grid(row=1, column=0, sticky=tk.W)

rb2 = tk.Radiobutton(app, text='USA', value=2, variable=country, padx=15, pady=10)
rb2.grid(row=2, column=0, sticky=tk.W)


app.mainloop()