import tkinter as tk
from tkinter import ttk


app = tk.Tk() 

# ---------------- Text
textedit_var=tk.StringVar()
textedit = tk.Text(app, width=25, height=5, bg="lightgray", fg='black', wrap=tk.WORD) #bg="darkgreen"  state='disabled'
textedit.pack() 
textedit.insert(tk.END, 'Текст вставленный в TextBox')

# Выделение текста
textedit.tag_add("here", "1.0", "1.4")
textedit.tag_add("start", "1.8", "1.13")
textedit.tag_config("here", background = "yellow", foreground = "blue")
textedit.tag_config("start", background = "black", foreground = "green")

print(textedit.get('1.0', 'end'))

app.mainloop()