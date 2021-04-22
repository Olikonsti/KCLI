from PACKET import *

PACKETNAME = "GUI"



class GUI(PACKET):
    def __init__(self):
        PACKET.__init__(self)

        self.packname = "GUI"
        self.packinfo = """
A KCLI Program GUI

Commands:
    gui config <setting> <value>
        setting[
            theme: "dark", "light", "speed"
        ]
            
"""
        self.packversion = "1.44"

    def uninstall(self):
        PACKET.uninstall(self)
        self.interpreter.askCommand("STARTTASKS remove GUI")

    def setup(self, args=None):
        PACKET.setup(self)
        self.download_dependency("azurettk.zip")
        self.unzip(DATAFOLDER2 + "EXTERNPACKAGES\\" + self.packname,"\\azurettk.zip")
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
        self.download_dependency("Settings.py")

        self.interpreter.askCommand("STARTTASKS add GUI")

        os.system(f"cd {DATAFOLDER}/PROGRAMDATA & mkdir GUI")

        try:
            f = open(f"{DATAFOLDER}/PROGRAMDATA/GUI/theme.txt", "r")
            f.read()
            f.close()
            console.log("Settings were not reset. use 'gui reset' to reset the GUI settings to default")
        except:
            self.reset()


    def reset(self, args=None):
        console.log("Loading default settings...")
        with open(f"{DATAFOLDER}/PROGRAMDATA/GUI/theme.txt", "w") as f:
            f.write("modern-dark")

    def config(self, args):
        if args[0] == "theme":
            f = open(f"{DATAFOLDER}/PROGRAMDATA/GUI/theme.txt", "w")
            f.write(args[1])
            f.close()

    def run(self, theme="speed"):

        console.log("loading settings...")

        f = open(f"{DATAFOLDER}/PROGRAMDATA/GUI/theme.txt", "r")
        self.theme = f.read()
        f.close()

        console.log("loading external classes...")
        self.BUTTON = self.loadExternClass("BUTTON.py")
        self.INSTALLBUTTON = self.loadExternClass("INSTALLBUTTON.py")
        self.Loading_Page = self.loadExternClass("Loading_Page.py")
        self.About_Page = self.loadExternClass("About_Page.py")
        self.Pack_Page = self.loadExternClass("Pack_Page.py")
        self.Home_Page = self.loadExternClass("Home_Page.py")
        self.Manage_Packages_Page = self.loadExternClass("Manage_Packages_Page.py")
        self.VerticalScrolledFrame = self.loadExternClass("VerticalScrolledFrame.py")
        self.CreatePackage = self.loadExternClass("CreatePackage.py")
        self.Settings = self.loadExternClass("Settings.py")

        console.log("checking for updates...")

        if requests.get(SERVERURL + "/" + "GUI" + "/" + "1version.txt").status_code == 200:
            if float(self.packversion) < float(
                    requests.get(SERVERURL + "/" + "GUI"+ "/" + "1version.txt").text):
                console.log(f'\nA new Version of the KCLI Gui is available... ({self.packversion}, {requests.get(SERVERURL + "/" + "GUI"+ "/" + "1version.txt").text})\n')
                if console.input("[blue]Would you like to update (y/n)> ") == "y":
                    console.log(f"\n[green]Updating KCLI Gui to version [cyan]" + requests.get(SERVERURL + "/" + "GUI"+ "/" + "1version.txt").text + "[green] ... Please wait\n")
                    self.interpreter.askCommand("UPDATE get GUI")
                    self.interpreter.askCommand("UTIL unload GUI")
                    self.interpreter.askCommand("GUI")
                    return 0


        console.log("loading GUI")

        self.window = Tk()
        self.window.geometry("800x500")
        self.window.title("KCLI Gui interface")
        self.window.iconbitmap(DATAFOLDER + "EXTERNPACKAGES/" + self.packname + "/icon.ico")
        self.window.protocol("WM_DELETE_WINDOW", lambda: (self.interpreter.askCommand("UTIL unload GUI"), self.window.destroy()))

        self.style = ttk.Style(self.window)

        if self.theme == "win10":
            self.style.theme_use("vista")
        elif self.theme == "win95":
            self.style.theme_use("winnative")
        elif self.theme == "clam":
            self.style.theme_use("clam")
        elif self.theme == "alt":
            self.style.theme_use("alt")
        elif self.theme == "modern-dark":
            try:
                self.window.tk.call("source", f"{DATAFOLDER}EXTERNPACKAGES/GUI/azure-dark.tcl")
            except:
                pass
            self.style.theme_use("azure-dark")
        elif self.theme == "modern-light":
            try:
                self.window.tk.call("source", f"{DATAFOLDER}EXTERNPACKAGES/GUI/azure.tcl")
            except:
                pass
            self.style.theme_use("azure")

        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(anchor=NW, expand=True, fill=BOTH)

        self.aboutPage = self.About_Page(self.notebook, self)
        self.homePage = self.Home_Page(self.notebook, self)
        self.managePackagesPage = self.Manage_Packages_Page(self.notebook, self)
        self.createPackage = self.CreatePackage(self.notebook, self)
        self.settings = self.Settings(self.notebook, self)

        self.notebook.add(self.homePage, text="Home")
        self.notebook.add(self.managePackagesPage, text="Install Packages")
        self.notebook.add(self.settings, text="Settings")
        self.notebook.add(self.aboutPage, text="About")

        #self.notebook.add(self.createPackage, text="Create KCLI Package")

    def create_popup_frame(self):
        pass

    def create_tab(self, frame, text):
        self.notebook.add(frame, text=text)
        self.notebook.select(frame)

