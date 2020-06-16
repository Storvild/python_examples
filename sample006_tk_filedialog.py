"""
    Файловый диалог
"""
import tkinter
from tkinter import filedialog


class MainTk(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        self.label = tkinter.Label(self, text='Текст')
        self.label.pack()

        self.button = tkinter.Button(self, text='Кнопка', command=self.fileDialog)
        self.button.pack()

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Выберите файл...",
                                                   filetype=(("txt files", "*.txt"), ("all files", "*.*")))
        self.label.configure(text=self.filename)


if __name__ == '__main__':
    app = MainTk()
    app.mainloop()
