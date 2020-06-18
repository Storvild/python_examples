import tkinter as tk
from tkinter import ttk

app = tk.Tk() 
app.title('Пример компонент tk')

entry = tk.Entry(app, width=30)
entry.grid(column=0, row=4)
entry.insert(1, 'Мой текст')

app.mainloop()