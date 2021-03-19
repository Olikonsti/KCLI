from PACKET import *

class UTIL(PACKET):
    def __init__(self):
        PACKET.__init__(self)

        self.info = "A KCLI Utility Packet\n" \
                    "Commands:\n\n" \
                    "'exit'\n" \
                    "'clear'\n" \
                    "'loaded'\n" \
                    "'loadas <listname> <packet>'\n" \
                    "'unload <listname>'\n"

    def run(self, args):
        if len(args) > 0 and PACKET.run(self, args) == 0:
            pass
        else:
            return 0

        if args[0].upper() == "EXIT":
            console.log("exiting...BYE!")
            self.interpreter.running = False
        elif args[0].upper() == "CLEAR":
            os.system('cls||clear')
        elif args[0].upper() == "LOADED":
            console.log(self.interpreter.loadedPackages)
        elif args[0].upper() == "UNLOAD":
            try:
                del self.interpreter.loadedPackages[args[1].upper()]
                console.log(f"sucessfully unloaded module '{args[1].upper()}'")
            except:
                console.log("[red] this module is not loaded!")
        elif args[0].upper() == "LOADAS" and len(args) == 3:
            self.interpreter.utilLoadPackage(args)



        else:
            console.log("[red] unknown UTIL command")