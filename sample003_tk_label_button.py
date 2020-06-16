"""
    Текст и Кнопка которая меняет текст
"""
import tkinter

app = tkinter.Tk()

label = tkinter.Label(app, text='Текст')
label.pack()


def button_click():
    current_text = label['text']
    label.config(text=current_text + '!')


button = tkinter.Button(app, text='Кнопка', command=button_click)
button.pack()

app.mainloop()
