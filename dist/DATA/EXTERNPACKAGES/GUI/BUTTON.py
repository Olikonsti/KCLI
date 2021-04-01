import tkinter.ttk as ttk
from tkinter import *

class mainclass(Frame):
    def __init__(self, packet, parent, item):
        self.item = item
        self.packet = packet
        Frame.__init__(self, parent)

        self.button = ttk.Button(self)
        self.button.config(command=self.click, text=self.item)
        self.button.pack(fill=X, side=LEFT, expand=True)

        self.openPageButton = ttk.Button(self, text="...", width=3, command=self.open_PackPage)
        self.openPageButton.pack(side=LEFT)

    def open_PackPage(self):
        self.packet.notebook.pack_forget()
        self.packet.Pack_Page(self.packet.window, self.packet, self.item)

    def click(self, event=None):
        self.packet.interpreter.askCommand(self.item)