import tkinter as tk
#contructor Frame#
class Frame(tk.Frame):
    def __init__(self, ventanaHistoriaM):
        super().__init__(ventanaHistoriaM, width=1200, height=620)
        self.ventanaHistoriaM = ventanaHistoriaM
        self.pack()
        self.config(bg='#CDD8FF')