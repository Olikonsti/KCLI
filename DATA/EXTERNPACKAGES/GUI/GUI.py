from PACKET import *

PACKETNAME = "GUI"

class GUI(PACKET):
    def __init__(self):
        PACKET.__init__(self)

        self.packname = "GUI"
        self.packinfo = "A KCLI Program GUI"
        self.packversion = "v0.3"

    def setup(self, args=None):
        self.download_dependency("icon.ico")
        self.download_dependency("BUTTON.py")
        self.download_dependency("About_Page.py")
        self.download_dependency("Home_Page.py")
        self.download_dependency("Manage_Packages_Page.py")
        self.download_dependency("VerticalScrolledFrame.py")

    def run(self):

        for i in range(100):
            self.interpreter.ADDONS.append(str(i))


        self.BUTTON = self.loadExternClass("BUTTON.py")
        self.About_Page = self.loadExternClass("About_Page.py")
        self.Home_Page = self.loadExternClass("Home_Page.py")
        self.Manage_Packages_Page = self.loadExternClass("Manage_Packages_Page.py")
        self.VerticalScrolledFrame = self.loadExternClass("VerticalScrolledFrame.py")

        self.window = Tk()
        self.window.geometry("800x500")
        self.window.title("KCLI Gui interface")
        self.window.iconbitmap(DATAFOLDER + "EXTERNPACKAGES/" + self.packname + "/icon.ico")

        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(anchor=NW, expand=True, fill=BOTH)

        self.aboutPage = self.About_Page(self.notebook, self)
        self.homePage = self.Home_Page(self.notebook, self)
        self.managePackagesPage = self.Manage_Packages_Page(self.notebook, self)

        self.notebook.add(self.homePage, text="Home")
        self.notebook.add(self.managePackagesPage, text="Manage Packages")
        self.notebook.add(self.aboutPage, text="About")


