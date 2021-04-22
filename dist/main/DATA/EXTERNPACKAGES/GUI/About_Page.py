from tkinter import *
import tkinter.ttk as ttk
from GLOBAL import *

class mainclass(Frame):
    def __init__(self, notebook, packet):
        Frame.__init__(self, notebook)
        self.config()

        self.leftframe = ttk.LabelFrame(self, text="KCLI Kernel")
        self.leftframe.pack(side=LEFT, expand=True, fill=BOTH)
        self.rightframe = ttk.LabelFrame(self, text="KCLI Gui")
        self.rightframe.pack(side=RIGHT, expand=True, fill=BOTH)

        self.KCLI_Label = Label(self.leftframe, justify=LEFT, text="A Command Line interface for downloading\n"
                                                                   "and using of programs and packages that are based on python\n\n"
                                                                   f"Version: {VERSION}\n"
                                                                   f"Based on Python {PYTHONVERSION}\n"
                                                                   f"Developer: Konstantin Ehmann\n")

        self.KCLI_Label.pack(anchor=NW)

        self.KCLIgui_Label = Label(self.rightframe, justify=LEFT, text="A Grafical User interface for the KCLI Kernel\n\n"
                                                                        f"Version: {packet.packversion}\n"
                                                                        f"Developer: Konstantin Ehmann\n")

        self.KCLIgui_Label.pack(anchor=NW)

        ttk.Button(self.leftframe, text="Creator Website", command=lambda: os.system("start http://ksite.ddns.net")).pack(anchor=NW)
        ttk.Button(self.leftframe, text="Creator Github",
                   command=lambda: os.system("start https://github.com/Olikonsti")).pack(anchor=NW)
        ttk.Button(self.leftframe, text="KCLI Github",
                   command=lambda: os.system("start https://github.com/Olikonsti/KCLI")).pack(anchor=NW)
