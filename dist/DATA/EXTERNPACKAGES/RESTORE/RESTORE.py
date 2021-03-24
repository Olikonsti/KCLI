from PACKET import *

PACKETNAME = "RESTORE"



class RESTORE(PACKET):
    def __init__(self):
        PACKET.__init__(self)

        self.name = "RESTORE"
        self.info = "A KCLI Packet to uninstall all other packets"
        self.version = "v1.0"


    def run(self, args):
        if PACKET.run(self, args) == 0:
            pass
        else:
            return 0

        a = input("Are you sure you want to uninstall all installed packages? (Y, N)> ")
        if a == "Y":
            console.log("STARTING... This process can take a while")
            console.log("you need to uninstall RESTORE manually if you really want to!")
            for i in self.interpreter.ADDONS.copy():
                if i in ADDONS or i == "RESTORE":
                    pass
                else:
                    console.log("Starting restore to default of " + i)
                    self.interpreter.askCommand("uninstall " + i)