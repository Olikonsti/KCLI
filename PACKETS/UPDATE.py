from PACKET import *

class UPDATE(PACKET):
    def __init__(self):
        PACKET.__init__(self)

        self.packinfo = "A Packet to update extern packets"

    def run(self):
        console.log(self.packinfo)

    def get(self, args):
        self.interpreter.askCommand("uninstall set " + args[0])
        self.interpreter.askCommand("install get " + args[0])