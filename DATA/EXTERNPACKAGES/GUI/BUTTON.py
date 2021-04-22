import tkinter.ttk as ttk
from tkinter import *
from GLOBAL import *

class mainclass(ttk.Frame):
    def __init__(self, packet, parent, item):
        self.item = item
        self.packet = packet
        self.item_instance = None
        ttk.Frame.__init__(self, parent)

        self.iconCanvas = Canvas(self, width=37, height=22, highlightthickness=0)
        self.iconCanvas.pack(side=LEFT)


        try:
            self.item_instance = self.packet.interpreter.loadedPackages[self.item]
        except:
            self.packet.interpreter.initializePacket(self.item)
        self.item_instance = self.packet.interpreter.loadedPackages[self.item]

        if requests.get(SERVERURL + "/" + item + "/" + "1version.txt").status_code == 200:
            if float(self.item_instance.packversion) < float(
                    requests.get(SERVERURL + "/" + self.item + "/" + "1version.txt").text):
                self.iconCanvas.create_oval(25, 8, 32, 16, fill="#0097cf", outline="")

        try:
            self.icon = Image.open(DATAFOLDER + "EXTERNPACKAGES/" + item + "/1icon.png").convert("RGBA")
            self.icon = self.icon.resize((22, 22), Image.BOX)
            self.image = ImageTk.PhotoImage(self.icon)
            self.iconCanvas.create_image(11, 11, image=self.image)
        except:
            pass


        self.button = ttk.Button(self)
        self.button.config(command=self.click, text=self.item)
        self.button.pack(fill=X, side=LEFT, expand=True, padx=2)

        if item == "GUI":
            self.button.config(command=lambda: console.log("An Error Accoured: HANDLE CANCELLED"))

        self.openPageButton = ttk.Button(self, text="...", width=3, command=self.open_PackPage)
        self.openPageButton.pack(side=LEFT)

    def open_PackPage(self):
        self.packet.notebook.pack_forget()
        self.packet.Pack_Page(self.packet.window, self.packet, self.item)

    def click(self, event=None):
        self.packet.interpreter.askCommand(self.item)