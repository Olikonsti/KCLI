from PACKET import *

PACKETNAME = "GUI"



class GUI(PACKET):
    def __init__(self):
        PACKET.__init__(self)

        self.packname = "GUI"
        self.packinfo = "A KCLI Program GUI"
        self.packversion = "1.34"

    def uninstall(self):
        PACKET.uninstall(self)
        self.interpreter.askCommand("STARTTASKS remove GUI")

    def setup(self, args=None):
        PACKET.setup(self)
        self.download_dependency("icon.ico")
        self.download_dependency("BUTTON.py")
        self.download_dependency("INSTALLBUTTON.py")
        self.download_dependency("About_Page.py")
        self.download_dependency("Home_Page.py")
        self.download_dependency("Manage_Packages_Page.py")
        self.download_dependency("Pack_Page.py")
        self.download_dependency("Loading_Page.py")
        self.download_dependency("VerticalScrolledFrame.py")
        self.download_dependency("CreatePackage.py")

        self.interpreter.askCommand("STARTTASKS add GUI")

    def run(self):

        self.BUTTON = self.loadExternClass("BUTTON.py")
        self.INSTALLBUTTON = self.loadExternClass("INSTALLBUTTON.py")
        self.Loading_Page = self.loadExternClass("Loading_Page.py")
        self.About_Page = self.loadExternClass("About_Page.py")
        self.Pack_Page = self.loadExternClass("Pack_Page.py")
        self.Home_Page = self.loadExternClass("Home_Page.py")
        self.Manage_Packages_Page = self.loadExternClass("Manage_Packages_Page.py")
        self.VerticalScrolledFrame = self.loadExternClass("VerticalScrolledFrame.py")
        self.CreatePackage = self.loadExternClass("CreatePackage.py")

        if requests.get(SERVERURL + "/" + "GUI" + "/" + "1version.txt").status_code == 200:
            if float(self.packversion) < float(
                    requests.get(SERVERURL + "/" + "GUI"+ "/" + "1version.txt").text):
                console.log("\nA new Version of the KCLI Gui is available...")
                console.log(f"\n[green]Updating KCLI Gui to version [cyan]" + requests.get(SERVERURL + "/" + "GUI"+ "/" + "1version.txt").text + "[green] ... Please wait\n")
                self.interpreter.askCommand("UPDATE get GUI")
                self.interpreter.askCommand("UTIL unload GUI")
                self.interpreter.askCommand("GUI")
                return 0

        self.window = Tk()
        self.window.geometry("800x500")
        self.window.title("KCLI Gui interface")
        self.window.iconbitmap(DATAFOLDER + "EXTERNPACKAGES/" + self.packname + "/icon.ico")

        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(anchor=NW, expand=True, fill=BOTH)

        self.aboutPage = self.About_Page(self.notebook, self)
        self.homePage = self.Home_Page(self.notebook, self)
        self.managePackagesPage = self.Manage_Packages_Page(self.notebook, self)
        self.createPackage = self.CreatePackage(self.notebook, self)

        self.notebook.add(self.homePage, text="Home")
        self.notebook.add(self.managePackagesPage, text="Install Packages")
        self.notebook.add(self.aboutPage, text="About")
        #self.notebook.add(self.createPackage, text="Create KCLI Package")

    def create_popup_frame(self):
        pass

    def create_tab(self, frame, text):
        self.notebook.add(frame, text=text)
        self.notebook.select(frame)

