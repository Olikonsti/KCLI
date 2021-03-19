from PACKET import *

class INSTALL(PACKET):
    def __init__(self):
        PACKET.__init__(self)

        self.info = "A Packet to install extern packets into the interpreter\n" \
                    "'list'"

        self.installing = True

    def runanimation(self):
        print("/\r", end="\r")
        time.sleep(0.1)
        print("-\r", end="\r")
        time.sleep(0.1)
        print("\\\r", end="\r")
        time.sleep(0.1)
        print("-\r", end="\r")

    def animationloop(self):
        while self.installing:
            self.runanimation()

    def run(self, args):

        if len(args) > 0 and PACKET.run(self, args) == 0:
            pass
        else:
            return 0

        if args[0].upper() == "LIST":
            os.system("start " + SERVERURL)
            return 0

        if args[0].upper() not in self.interpreter.ADDONS:
            pass
        else:
            console.log("[red]Packet is already installed!")
            return 0
        if requests.get(SERVERURL + args[0].upper() + "/" + args[0].upper() + ".py").status_code == 200:
            package = args[0].upper()
            console.log("starting installation of " + args[0].upper())
            os.system("cd " + DATAFOLDER + "EXTERNPACKAGES/ & mkdir " + package)
            f = open(DATAFOLDER + "EXTERNPACKAGES/" + args[0].upper() + "/" + package + ".py", "a")
            f.close()
            f = open(DATAFOLDER + "EXTERNPACKAGES/" + args[0].upper() + "/" + package + ".py", "w")
            f.write(requests.get(SERVERURL + args[0].upper() + "/" + args[0].upper() + ".py").text)
            f.close()


            self.interpreter.askCommand("import " + DATAFOLDER + "EXTERNPACKAGES/" + package + "/" + package)
            self.interpreter.askCommand("starttasks addimport " + package)
            console.log("starting setup...")
            console.log("[yellow]The installation can take a while...\n\n")
            threading.Thread(target=self.animationloop).start()
            self.interpreter.askCommand(package + " setup")
            self.installing = False
            print()
            time.sleep(0.6)
            console.log("finished!")

        else:
            console.log("[red]Packet not fond on the server " + SERVERURL)