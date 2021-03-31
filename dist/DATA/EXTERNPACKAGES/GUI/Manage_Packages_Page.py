from tkinter import *
import tkinter.ttk as ttk

class mainclass(Frame):
    def __init__(self, notebook, packet):
        Frame.__init__(self, notebook)
        self.config()

        self.inner = packet.VerticalScrolledFrame(self)
        self.inner.pack(side=BOTTOM, fill=BOTH, expand=TRUE)

        Label(self.inner.interior, text="Packages!").pack()
        for i in packet.interpreter.ADDONS:
            for j in packet.interpreter.loadedPackages:
                if i == j:
                    item = packet.interpreter.loadedPackages[i]
                    Label(self.inner.interior, text=i + " - " + str(item.packinfo) + "\n\n", justify=LEFT).pack(anchor=NW)
