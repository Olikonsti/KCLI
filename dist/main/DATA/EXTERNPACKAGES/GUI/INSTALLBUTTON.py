import tkinter.ttk as ttk
from tkinter import *

class mainclass(Frame):
    def __init__(self, packet, parent, item, install_mng):
        self.item = item
        self.packet = packet
        self.parent = parent
        self.install_mng = install_mng
        Frame.__init__(self, parent)

        self.button = ttk.Button(self, width=30)
        self.button.config(command=self.click, text=self.item)
        self.button.pack(fill=X, side=LEFT, expand=True)


    def click(self, event=None):
        #self.install_mng.install(self.item)
        self.packet.notebook.pack_forget()
        self.packet.Pack_Page(self.packet.window, self.packet, self.item, mode="INSTALL", packmgr=self.install_mng)