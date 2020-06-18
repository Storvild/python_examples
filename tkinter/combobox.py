import tkinter as tk
from tkinter import ttk
from pprint import pprint

def callbackFunc(event):
     labelTop.config(text='Вы выбрали {} ({})'.format(comboExample.get(), comboExample.current()))
     
app = tk.Tk() 

labelTop = tk.Label(app, text = "Выберите месяц")
labelTop.pack()

# ------------- ComboBox -----------
month_list = ["Январь", "Февраль", "Март", "Апрель"]
comboExample = ttk.Combobox(app, values=month_list, state="readonly")
comboExample.pack()
# По умолчанию выбераем Февраль
comboExample.current(1)

# Событие на выбор элемента combobox
comboExample.bind("<<ComboboxSelected>>", callbackFunc)


app.mainloop()