"""
    Основные настройки окна
"""

import tkinter

app = tkinter.Tk()

# Размер окна при открытии
app.geometry('350x300')
# Минимальный размер окна
app.minsize(200,200)
# Заголовок
app.title('Заголовок окна')
# Иконка приложения
#app.iconbitmap('MyIcon.ico')

app.mainloop()
