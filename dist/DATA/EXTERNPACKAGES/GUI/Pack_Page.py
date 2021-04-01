from tkinter import *
import tkinter.ttk as ttk
from GLOBAL import *

class mainclass(Frame):
    def __init__(self, parent, packet_onTop, packet):
        Frame.__init__(self, parent)

        self.packet = packet
        self.packet_onTop = packet_onTop
        self.pack(expand=True, fill=BOTH)

        self.navBar = Frame(self, height=5)
        self.navBar.pack(fill=X)

        ttk.Separator(self.navBar).pack(fill=X, side=BOTTOM)

        self.back_button = ttk.Button(self.navBar, text="<", width=3, command=self.exit_window)
        self.back_button.pack(side=LEFT)
        self.packLabel = Label(self.navBar, text=packet)
        self.packLabel.pack(side=LEFT)

        self.scrollregion = self.packet_onTop.VerticalScrolledFrame(self)
        self.scrollregion.pack(expand=TRUE, fill=BOTH, side=BOTTOM)



        self.topframe = Frame(self.scrollregion.interior, height=200)
        self.topframe.pack(side=TOP, fill=X, expand=True, anchor=NW)
        self.bottomframe = ttk.LabelFrame(self.scrollregion, text="KCLI Gui")
        self.bottomframe.pack(side=BOTTOM)

        self.packImageContainer = Canvas(self.topframe, width=200, height=200, bg="blue", highlightthickness=0)
        self.packImageContainer.pack(side=LEFT, pady=10, padx=10)

        self.actionsContainer = Frame(self.topframe, width=70, height=40, bg="red")
        self.actionsContainer.pack(side=LEFT, anchor=S, pady=20)

        self.properties = Frame(self.topframe, bg="green")
        self.properties.pack(side=RIGHT, fill=BOTH, expand=True, pady=10, padx=10)

        # actions
        self.uninstall_button = ttk.Button(self.actionsContainer, text="Uninstall", command=self.uninstall_app)
        self.uninstall_button.pack()

    def exit_window(self):
        self.destroy()
        self.packet_onTop.notebook.pack(
            expand=True, fill=BOTH)

    def uninstall_app(self):
        a = threading.Thread(target=lambda: self.packet_onTop.interpreter.askCommand("UNINSTALL set " + self.packet))
        a.start()
        self.exit_window()