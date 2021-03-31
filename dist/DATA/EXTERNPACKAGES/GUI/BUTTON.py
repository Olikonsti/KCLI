import tkinter.ttk as ttk
from tkinter import *

class mainclass(ttk.Button):
    def __init__(self, packet, parent, item):
        self.item = item
        self.packet = packet
        ttk.Button.__init__(self, parent)
        self.config(command=self.click, text=self.item)

    def click(self):
        self.packet.interpreter.askCommand(self.item)