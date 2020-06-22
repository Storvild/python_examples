""" Пример использования переменной StringVar для поля entry """
import tkinter as tk
from tkinter import ttk

app = tk.Tk() 
app.title('Пример использования StringVar и entry')

entry_var = tk.StringVar()
entry = tk.Entry(app, width=30, textvariable=entry_var)
entry.grid(column=0, row=4)
entry_var.set('Текст') # Переменная и поле ввода entry_var теперь содержит текст "Текст"

# После нажатия на любую клавишу в поле ввода, в заголовке окна меняется текст
# Текст считывается из поля ввода с помощью переменной entry_var (entry_var.get())
entry.bind('<KeyRelease>', lambda event: app.title(entry_var.get())) 



app.mainloop()