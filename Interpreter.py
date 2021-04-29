from PACKETS.HELP import *
from PACKETS.STARTTASKS import *
from PACKETS.IMPORT import *
from PACKETS.INSTALL import *
from PACKETS.UNINSTALL import *
from PACKETS.UPDATE import *
from PACKETS.UTIL import *



class Interpreter():
    def __init__(self):
        console.log("Interpreter starting...")

        INTERPRETER.append(self)

        self.cmd = ""
        self.running = True
        self.ADDONS = ADDONS.copy()

        self.loadedPackages = {}



        self.askCommand("starttasks")

        while self.running:
            self.askCommand()



    def execGlobal(self, code):
        try:
            exec(code)
            return False
        except Exception as e:
            return str(e)

    def utilLoadPackage(self, args):
        if args[1].upper() in self.ADDONS:
            if args[0].upper() in self.loadedPackages:
                console.log("[red]A packet is already loaded with that name!")
            else:
                execstring = "global module; module = " + args[1].upper() + "()"
                exec(execstring)
                self.loadedPackages[args[0].upper()] = module
                module.giveInterpreter(self)

        else:
            console.log("[red]Unknown Packet/ unknown error")

    def initializePacket(self, packet):
        execstring = "global module; module = " + packet + "()"
        try:
            exec(execstring)
            self.loadedPackages[packet] = module
            module.giveInterpreter(self)
            return 0
        except:
            console.log(f"[red]Error Packet {packet} was not found in the kernel!")
            return 1


    def askCommand(self, cmd=None):
        if cmd != None:
            self.cmd = cmd
        else:
            print("\n")
            try:
                self.cmd = console.input("[green]%> ")
            except:
                pass


        self.cmd = shlex.split(self.cmd)
        if len(self.cmd) == 0:
            return 0
        self.cmd[0] = self.cmd[0].upper()
        self.args = self.cmd.copy()
        self.args.remove(self.cmd[0])
        if self.cmd[0] in self.loadedPackages:
            try:
                if len(self.cmd) > 1:
                    self.args.remove(self.cmd[1])
                    exec("self.loadedPackages[self.cmd[0]]." + str(self.cmd[1]) + "(" + str(self.args) + ")")
                else:
                    self.loadedPackages[self.cmd[0]].run()
            except Exception as e:
                console.log("[red]An Error accoured: " + str(e))
        elif self.cmd[0] in self.ADDONS:
            execstring = "global module; module = " + self.cmd[0]+ "()"
            exec(execstring)
            try:

                self.loadedPackages[self.cmd[0]] = module
                module.giveInterpreter(self)
                if len(self.cmd) > 1:
                    self.args.remove(self.cmd[1])
                    exec("module." + str(self.cmd[1]) + "(" + str(self.args) + ")")
                else:
                    module.run()
            except Exception as e:
                console.log("[red]An Error accoured: " + str(e))
        else:
            print("[red]This command/addon is unknown. Import it with 'import <dest>' or install it with 'install <packet>'")