from tkinter import *
import tkinter.ttk as ttk
from GLOBAL import *

class mainclass(ttk.Frame):
    def __init__(self, notebook, packet):
        ttk.Frame.__init__(self, notebook)
        self.packet = packet

        class AttributeSelectBox(ttk.LabelFrame):
            def __init__(self, parent, text, values):
                super().__init__(parent)
                self.var = StringVar()
                self.config(text=text)
                self.inner = ttk.Combobox(self, textvariable=self.var, state="readonly", values=values)
                self.inner.pack()

        self.theme_select = AttributeSelectBox(self, "Gui Theme", ["win10", "modern-dark", "modern-light", "clam", "alt", "win95",])
        try:
            self.theme_select.inner.current(["win10", "modern-dark", "modern-light", "clam", "alt", "win95",].index(packet.theme))
        except Exception as e:
            console.log(e)
        self.theme_select.pack(anchor=NW)


        self.apply_button = ttk.Button(self, text="Apply", command=self.apply)
        self.apply_button.pack(anchor=SE)

    def apply(self):
        console.log("Applying...")
        # Theme
        with open(f"{DATAFOLDER}/PROGRAMDATA/GUI/theme.txt", "w") as f:
            f.write(self.theme_select.var.get())


        # restarting
        self.packet.window.destroy()
        self.packet.interpreter.askCommand("util unload GUI")
        self.packet.interpreter.askCommand("GUI")
        del self
        return 0
