from tkinter import *
import tkinter.ttk as ttk
from GLOBAL import *

class mainclass(Frame):
    def __init__(self, parent, packet):
        Frame.__init__(self, parent)
        self.pack(expand=True, fill=BOTH)


        Label(self, text="Loading...").pack(expand=True)