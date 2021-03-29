from PACKET import *

class UTIL(PACKET):
    def __init__(self):
        PACKET.__init__(self)

        self.packinfo = "A KCLI Utility Packet\n" \
                    "Commands:\n\n" \
                    "'exit'\n" \
                    "'clear'\n" \
                    "'loaded'\n" \
                    "'loadas <listname> <packet>'\n" \
                    "'unload <listname>'\n"

    def run(self):
        console.log(self.packinfo)

    def exit(self, args):
        console.log("exiting...BYE!")
        self.interpreter.running = False

    def clear(self, args):
        os.system('cls||clear')

    def loaded(self, args):
        console.log(self.interpreter.loadedPackages)

    def unload(self, args):
        try:
            del self.interpreter.loadedPackages[args[0].upper()]
            console.log(f"sucessfully unloaded module '{args[0].upper()}'")
        except:
            console.log("[red] this module is not loaded!")

    def loadas(self, args):
        self.interpreter.utilLoadPackage(args)