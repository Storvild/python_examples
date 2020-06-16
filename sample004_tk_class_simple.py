"""
    Простая программа с пустым окном основанная на классе Tk
"""

import tkinter


class MainTk(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)


if __name__ == '__main__':
    app = MainTk()
    app.mainloop()
