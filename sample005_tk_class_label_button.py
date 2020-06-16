"""
    Текст, Кнопка, Обработка нажатия на кнопку
"""
import tkinter


class MainTk(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        self.label = tkinter.Label(self, text='Текст')
        self.label.pack()

        self.button = tkinter.Button(self, text='Кнопка', command=self.button_click)
        self.button.pack()

    def button_click(self):
        current_text = self.label['text']
        self.label.config(text=current_text + '!')


if __name__ == '__main__':
    app = MainTk()
    app.mainloop()
