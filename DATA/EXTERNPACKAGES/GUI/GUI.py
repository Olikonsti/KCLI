from PACKET import *

PACKETNAME = "GUI"

class GUI(PACKET):
    def __init__(self):
        PACKET.__init__(self)

        self.packname = "GUI"
        self.packinfo = "A KCLI Program starter GUI"



        global SIDEPANEL

        class SIDEPANEL(Frame):
            def __init__(self, parent):
                Frame.__init__(self, parent)
                self.pack(side=RIGHT)



    def setup(self, args=None):
        self.download_dependency("BUTTON.py")

    def run(self):

        BUTTON = self.loadExternClass("BUTTON.py")

        self.window = Tk()
        self.window.geometry("800x500")

        self.sidepanel = SIDEPANEL(self.window)
        for i in self.interpreter.ADDONS:
            if i in ADDONS:
                pass
            else:
                b = BUTTON(self, self.sidepanel, i)
                b.pack()

                print(i)