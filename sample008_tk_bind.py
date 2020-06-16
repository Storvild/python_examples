"""
    Выход по Esc или средней кнопке мыши
"""

import tkinter


class MainTk(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        self.bind('<Button-2>', lambda event: exit())  # Выход по средней кнопки мыши
        self.bind('<Escape>', lambda event: exit())  # Выход по Esc


if __name__ == '__main__':
    app = MainTk()
    app.mainloop()
