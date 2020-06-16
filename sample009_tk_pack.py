"""
    Выход по Esc или средней кнопке мыши
"""

import tkinter as tk
from tkinter import ttk

class MainTk(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        frame1 = ttk.LabelFrame(self, text='pack()', width=200, height=50)
        frame1.pack(fill=tk.X)

        frame11 = tk.Label(frame1, text='1', width='5', height='2', background='#AAA')
        frame11.pack()
        frame12 = tk.Label(frame1, text='2', width='5', height='2', background='#999')
        frame12.pack()
        frame13 = tk.Label(frame1, text='3', width='5', height='2', background='#777')
        frame13.pack()

        frame2 = ttk.LabelFrame(self, text='pack(side=RIGHT)', width=200, height=50)
        frame2.pack(fill=tk.X)

        frame21 = tk.Frame(frame2, width=50, height=50, background='#AAA')
        frame21.pack(side=tk.RIGHT)
        frame22 = tk.Frame(frame2, width=50, height=50, background='#999')
        frame22.pack(side=tk.RIGHT)
        frame23 = tk.Frame(frame2, width=50, height=50, background='#777')
        frame23.pack(side=tk.RIGHT)

if __name__ == '__main__':
    app = MainTk()
    app.mainloop()
