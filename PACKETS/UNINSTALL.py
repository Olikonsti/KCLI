from PACKET import *

class UNINSTALL(PACKET):
    def __init__(self):
        PACKET.__init__(self)

        self.info = "A Packet to remove extern packets from the interpreter"

    def run(self, args):

        if len(args) > 0 and PACKET.run(self, args) == 0:
            pass
        else:
            return 0

        package = args[0].upper()
        console.log("starting deletion of " + args[0].upper())
        os.system('rmdir /S ' + DATAFOLDER2 + "EXTERNPACKAGES\\" + args[0].upper())
        try:
            self.interpreter.ADDONS.remove(package)
        except Exception as e:
            console.log("[red]" + str(e))
        self.interpreter.askCommand("starttasks removeimport " + package)
        self.interpreter.askCommand("util unload " + args[0])
        console.log("finished!")