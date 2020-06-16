import tkinter as tk
from tkinter import ttk


class MainTk(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.labelframe1 = ttk.LabelFrame(self, text='Группа1')
        self.labelframe1.pack(padx=10, pady=10)

        self.button1 = tk.Button(self.labelframe1, text='Кнопка')
        self.button1.pack(padx=10, pady=10)

        self.labelframe2 = ttk.LabelFrame(self, text='Группа2')
        self.labelframe2.pack(padx=10, pady=10, fill='both')

        self.button2 = tk.Button(self.labelframe2, text='Кнопка')
        self.button2.pack(padx=10, pady=10, side=tk.RIGHT)

        self.labelframe3 = ttk.LabelFrame(self, text='Группа3')
        self.labelframe3.pack(padx=10, pady=10, fill='both', expand=1)

        self.button3 = tk.Button(self.labelframe3, text='Кнопка', background='#555', foreground='#eee', font=15)
        self.button3.pack(padx=10, pady=10)

        self.labelframe4 = ttk.LabelFrame(self, text='Группа4')
        self.labelframe4.pack(padx=10, pady=10, fill='both')

        self.button4 = tk.Button(self.labelframe4, text='Кнопка')
        self.button4.pack(padx=10, pady=10, fill=tk.X)


if __name__ == '__main__':
    app = MainTk()
    app.mainloop()
