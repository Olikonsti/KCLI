from PACKET import *

class IMPORT(PACKET):
    def __init__(self):
        PACKET.__init__(self)

        self.packinfo = "A Packet to import extern packets into the interpreter"

    def run(self):
        console.log(self.packinfo)

    def set(self, args):
        try:
            f = open(args[0].upper()+".py", "r")
            code = f.read()
            f.close()
        except Exception as e:
            console.log("[red]Error opening file " + str(e))
        try:
            exec("global PACKETNAME; " + code)
            self.interpreter.ADDONS.append(PACKETNAME)
        except Exception as e:
            console.log(f"[red]Packet import error STAGE1:\n{e}")
        try:
            error = self.interpreter.execGlobal(f"global {PACKETNAME}; " + code)
            if error != False:
                console.log("IMPORT ERROR: " + str(error))
        except Exception as e:
            console.log(f"[red]Packet import error STAGE2:\n{e}")