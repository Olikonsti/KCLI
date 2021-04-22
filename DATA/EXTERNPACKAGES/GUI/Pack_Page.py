from tkinter import *
import tkinter.ttk as ttk
from GLOBAL import *
from PIL import Image
from PIL import ImageTk

class mainclass(ttk.Frame):
    def __init__(self, parent, packet_onTop, packet, mode="installed", packmgr=None):
        ttk.Frame.__init__(self, parent)

        self.packet = packet
        self.packet_onTop = packet_onTop
        self.pack(expand=True, fill=BOTH)
        self.packmgr = packmgr

        self.navBar = ttk.Frame(self, height=5)
        self.navBar.pack(fill=X)

        ttk.Separator(self.navBar).pack(fill=X, side=BOTTOM)

        self.back_button = ttk.Button(self.navBar, text="<", width=3, command=self.exit_window)
        self.back_button.pack(side=LEFT)
        self.packLabel = ttk.Label(self.navBar, text=packet)
        self.packLabel.pack(side=LEFT)

        self.scrollregion = self.packet_onTop.VerticalScrolledFrame(self)
        self.scrollregion.pack(expand=TRUE, fill=BOTH, side=BOTTOM)



        self.topframe = ttk.Frame(self.scrollregion.interior, height=200)
        self.topframe.pack(side=TOP, fill=X, expand=True, anchor=NW)
        self.bottomframe = ttk.LabelFrame(self.scrollregion.interior, text="Packet info")
        self.bottomframe.pack(side=TOP, fill=BOTH, expand=True, anchor=NW, padx=10, pady=10)

        self.packImageContainer = Canvas(self.topframe, width=202, height=202, bg="grey", highlightthickness=1)
        self.packImageContainer.pack(side=LEFT, pady=10, padx=10)

        self.actionsContainer = ttk.Frame(self.topframe, width=70, height=40)
        self.actionsContainer.pack(side=LEFT, anchor=S, pady=20)

        self.properties = ttk.Frame(self.topframe)
        self.properties.pack(side=RIGHT, expand=True, pady=30, padx=30)

        # properties
        if mode != "INSTALL":
            self.packet_onTop.interpreter.initializePacket(packet)
        if requests.get(SERVERURL + "/" + packet + "/" + "1version.txt").status_code == 200:
            ttk.Label(self.properties, text="Newest Version            " + requests.get(
                SERVERURL + "/" + packet + "/" + "1version.txt").text).pack(anchor=NW)
        if mode != "INSTALL":
            ttk.Label(self.properties, text="Installed Version          " + str(self.packet_onTop.interpreter.loadedPackages[
                packet].packversion)).pack(anchor=NW)

        if requests.get(SERVERURL + "/" + packet + "/" + "1developer.txt").status_code == 200:
            ttk.Label(self.properties, text="Developer:                    " + requests.get(
                SERVERURL + "/" + packet + "/" + "1developer.txt").text).pack(anchor=NW)



        # actions
        if mode != "INSTALL":
            if self.packet != "GUI":
                self.start_button = ttk.Button(self.actionsContainer, text="Start",
                                               command=lambda: self.packet_onTop.interpreter.askCommand(self.packet))
                self.start_button.pack(pady=1)
            self.runWithArgsFrame = ttk.Frame(self.actionsContainer)
            self.runWithArgsFrame.pack(pady=1)

            self.runWithArgsbtn = ttk.Button(self.runWithArgsFrame, text=">", width=3, command=lambda: self.packet_onTop.interpreter.askCommand(self.packet + " " + self.runWithArgsentry.get()))
            self.runWithArgsbtn.pack(side=RIGHT)
            self.runWithArgsentry = ttk.Entry(self.runWithArgsFrame, width=10)
            self.runWithArgsentry.pack(side=LEFT)
            if requests.get(SERVERURL + "/" + packet + "/" + "1version.txt").status_code == 200:
                if float(self.packet_onTop.interpreter.loadedPackages[packet].packversion) < float(
                        requests.get(SERVERURL + "/" + packet + "/" + "1version.txt").text):
                    self.update_button = ttk.Button(self.actionsContainer, text="Update", command=self.update_app)
                    self.update_button.pack(pady=1)

            self.uninstall_button = ttk.Button(self.actionsContainer, text="Uninstall", command=self.uninstall_app)
            self.uninstall_button.pack(pady=1)
        else:
            self.install_button = ttk.Button(self.actionsContainer, text="Install", command=lambda: (self.destroy(), self.packmgr.install(packet)))
            self.install_button.pack(pady=1)




        # icon_loading
        try:
            if mode != "INSTALL":
                self.icon = Image.open(DATAFOLDER + "EXTERNPACKAGES/" + self.packet + "/1icon.png").convert("RGBA")
                self.icon = self.icon.resize((200, 200), Image.BOX)
                self.image = ImageTk.PhotoImage(self.icon)
                self.packImageContainer.create_image(102, 102, image=self.image)
            else:
                r = requests.get(str(SERVERURL) + "/" + str(self.packet) + "/" + "1icon.png")
                with open(str(DATAFOLDER) + "/TEMP/" + "1icon.png", 'wb') as pypdf:
                    pypdf.write(r.content)
                self.icon = Image.open(DATAFOLDER + "TEMP/" + "1icon.png").convert("RGBA")
                self.icon = self.icon.resize((200, 200), Image.BOX)
                self.image = ImageTk.PhotoImage(self.icon)
                self.packImageContainer.create_image(102, 102, image=self.image)
        except:
            pass

        # packInfo
        if requests.get(SERVERURL + "/" + packet + "/" + "1info.txt").status_code == 200:
            self.infoLabel = Label(self.bottomframe, text=requests.get(SERVERURL + "/" + packet + "/" + "1info.txt").text, justify=LEFT)
            self.infoLabel.pack(anchor=NW, padx=10, pady=10)

    def exit_window(self):
        self.destroy()
        self.packet_onTop.notebook.pack(
            expand=True, fill=BOTH)

    def uninstall_app(self):
        response = messagebox.askquestion(title="Deletion Warning", message=f"Are you sure, that you want to delete {self.packet}?")
        if response == "yes":
            a = threading.Thread(target=lambda: self.packet_onTop.interpreter.askCommand("UNINSTALL set " + self.packet))
            a.start()
            self.exit_window()

    def launch_loading_screen(self, thread):
        self.pack_forget()
        loading_page = self.packet_onTop.Loading_Page(self.packet_onTop.window, self.packet_onTop)
        while thread.is_alive():
            self.packet_onTop.window.update()
        loading_page.destroy()
        self.exit_window()

    def update_app(self):
        response = messagebox.askquestion(title="Update Warning",
                                          message=f"Are you sure? Data of the packet {self.packet} might get lost!")
        if response == "yes":

            a = threading.Thread(target=lambda: self.packet_onTop.interpreter.askCommand("UPDATE get " + self.packet))
            a.start()
            self.launch_loading_screen(a)