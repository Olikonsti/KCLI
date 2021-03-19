from PACKET import *

class HELP(PACKET):
    def __init__(self):
        PACKET.__init__(self)

        self.info = "A Packet to tell you what packages you have imported"

    def run(self, args):

        if PACKET.run(self, args) == 0:
            pass
        else:
            return 0

        console.log("Packages:\n")
        for i in self.interpreter.ADDONS:
             console.log(i)
        console.log()
        console.log("type '<Packet> info' to see the packets info page")