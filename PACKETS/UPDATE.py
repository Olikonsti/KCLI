from PACKET import *

class UPDATE(PACKET):
    def __init__(self):
        PACKET.__init__(self)

        self.info = "A Packet to update extern packets"

    def run(self, args):

        if len(args) > 0 and PACKET.run(self, args) == 0:
            pass
        else:
            return 0


        self.interpreter.askCommand("uninstall " + args[0])
        self.interpreter.askCommand("install " + args[0])