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

        self.instruction = Label(self.rightframe, text="1. Select a zip file with the main.exe and all the dependencies\n directly in it\n"
                                                       "2. Select a name for your packet (Caps)\n"
                                                       "3. Write a infotext, developertext and select a image and a version"

                                 , justify=LEFT)
        self.instruction.pack(anchor=NW)

        label = ttk.LabelFrame(self.leftframe, text="Path to .zip", width=40)
        self.zip_select = ttk.Entry(label, width=40)
        self.zip_select.pack()
        label.pack(anchor=NW)

        label = ttk.LabelFrame(self.leftframe, text="Packet Name (Caps)")
        self.name_select = ttk.Entry(label, width=30)
        self.name_select.pack()
        label.pack(anchor=NW)

        label = ttk.LabelFrame(self.leftframe, text="Packet Info Text (optional)")
        self.info_select = Text(label, height=5, width=50)
        self.info_select.pack()
        label.pack(anchor=NW)

        label = ttk.LabelFrame(self.leftframe, text="Packet Developer (optional)")
        self.dev_select = ttk.Entry(label, width=30)
        self.dev_select.pack()
        label.pack(anchor=NW)

        label = ttk.LabelFrame(self.leftframe, text="Packet Version (optional)")
        self.version_select = ttk.Entry(label, width=30)
        self.version_select.pack()
        label.pack(anchor=NW)

        label = ttk.LabelFrame(self.leftframe, text="Path to .png (optional)", width=40)
        self.img_select = ttk.Entry(label, width=40)
        self.img_select.pack()
        label.pack(anchor=NW)

        applybtn = ttk.Button(self.leftframe, text="Create Package", command=self.create_pkg)
        applybtn.pack(anchor=NW, pady=(10, 0))

    def create_pkg(self):
        os.system(f"mkdir {DATAFOLDER2}Pack_out")
        os.system(f"rmdir /S /Q {DATAFOLDER2}Pack_out")
        os.system(f"mkdir {DATAFOLDER2}Pack_out")

        f = open(self.zip_select.get(), "rb")
        data = f.read()
        f.close()

        f = open(f"{DATAFOLDER}Pack_out/dist.zip", "wb")
        f.write(data)
        f.close()

        packname = self.name_select.get().upper()
        code = f'''from PACKET import *

PACKETNAME = "{packname}"

class {packname}(PACKET):
    def __init__(self):
        PACKET.__init__(self)
        self.packname = "{packname}"
        self.packinfo = "{self.info_select.get(1.0, END)}"
        self.packversion = {self.version_select.get()}

    def setup(self, args=None):
        {packname}.setup(self)
        self.download_dependency("dist.zip")
        self.unzip(DATAFOLDER2 + "EXTERNPACKAGES\\" + self.packname,"\\dist.zip")

    def run(self):
        os.system("cd " + DATAFOLDER + "EXTERNPACKAGES/" + self.packname + "/ & start main.exe")'''

        f = open(f"{DATAFOLDER}Pack_out/{packname}.py", "w")
        f.write(code)
        f.close()

        if self.dev_select.get() != "":
            f = open(f"{DATAFOLDER}Pack_out/1developer.py", "w")
            f.write(self.dev_select.get())
            f.close()

        if self.version_select.get() != "":
            f = open(f"{DATAFOLDER}Pack_out/1version.py", "w")
            f.write(self.version_select.get())
            f.close()

        if self.img_select.get() != "":
            f = open(self.zip_select.get(), "rb")
            data = f.read()
            f.close()

            f = open(f"{DATAFOLDER}Pack_out/1icon.png", "wb")
            f.write(data)
            f.close()

        os.system(f"start {DATAFOLDER2}Pack_out")