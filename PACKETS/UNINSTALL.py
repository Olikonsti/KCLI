from PACKET import *

class UNINSTALL(PACKET):
    def __init__(self):
        PACKET.__init__(self)

        self.packinfo = "A Packet to remove extern packets from the interpreter"

    def run(self):
        console.log(self.packinfo)

    def set(self, args):
        package = args[0].upper()
        console.log("starting deletion of " + args[0].upper())
        os.system('rmdir /S /Q ' + DATAFOLDER2 + "EXTERNPACKAGES\\" + args[0].upper())
        try:
            self.interpreter.ADDONS.remove(package)
        except Exception as e:
            console.log("[red]" + str(e))
        self.interpreter.askCommand("starttasks removeimport " + package)
        self.interpreter.askCommand("util unload " + args[0])
        console.log("finished!")