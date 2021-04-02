from tkinter import *
import tkinter.ttk as ttk
from GLOBAL import *
from PIL import Image
from PIL import ImageTk

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

        self.properties = Frame(self.topframe)
        self.properties.pack(side=RIGHT, fill=BOTH, expand=True, pady=30, padx=30)

        # properties
        self.packet_onTop.interpreter.initializePacket(packet)
        if requests.get(SERVERURL + "/" + packet + "/" + "1version.txt").status_code == 200:
            Label(self.properties, text="Newest Version            " + requests.get(
                SERVERURL + "/" + packet + "/" + "1version.txt").text).pack(anchor=NW)
        Label(self.properties, text="Installed Version          " + self.packet_onTop.interpreter.loadedPackages[
            packet].packversion).pack(anchor=NW)

        if requests.get(SERVERURL + "/" + packet + "/" + "1developer.txt").status_code == 200:
            Label(self.properties, text="Developer:                    " + requests.get(
                SERVERURL + "/" + packet + "/" + "1developer.txt").text).pack(anchor=NW)



        # actions
        if self.packet != "GUI":
            self.start_button = ttk.Button(self.actionsContainer, text="Start", command=lambda: self.packet_onTop.interpreter.askCommand(self.packet))
            self.start_button.pack()
        if requests.get(SERVERURL + "/" + packet + "/" + "1version.txt").status_code == 200:
            if float(self.packet_onTop.interpreter.loadedPackages[packet].packversion) < float(requests.get(SERVERURL + "/" + packet + "/" + "1version.txt").text):
                self.update_button = ttk.Button(self.actionsContainer, text="Update", command=self.update_app)
                self.update_button.pack()



        self.uninstall_button = ttk.Button(self.actionsContainer, text="Uninstall", command=self.uninstall_app)
        self.uninstall_button.pack()




        # icon_loading
        self.icon = Image.open(DATAFOLDER + "EXTERNPACKAGES/" + self.packet + "/1icon.png").convert("RGBA")
        self.icon = self.icon.resize((200, 200), Image.BOX)
        self.image = ImageTk.PhotoImage(self.icon)
        self.packImageContainer.create_image(100, 100, image=self.image)

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