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
        self.ADDONS = ADDONS

        self.loadedPackages = {}



        self.askCommand("starttasks run")

        while self.running:
            self.askCommand()



    def execGlobal(self, code):
        try:
            exec(code)
            return False
        except Exception as e:
            return str(e)

    def utilLoadPackage(self, args):
        if args[2].upper() in self.ADDONS:
            if args[1].upper() in self.loadedPackages:
                console.log("[red]A packet is already loaded with that name!")
            else:
                execstring = "global module; module = " + args[2].upper() + "()"
                exec(execstring)
                self.loadedPackages[args[1].upper()] = module
                module.giveInterpreter(self)

        else:
            console.log("[red] Unknown Packet/ unknown error")



    def askCommand(self, cmd=None):
        if cmd != None:
            self.cmd = cmd
        else:
            print("\n")
            self.cmd = console.input("[green]%> ")


        self.cmd = shlex.split(self.cmd)
        if len(self.cmd) == 0:
            return 0
        self.cmd[0] = self.cmd[0].upper()
        self.args = self.cmd.copy()
        self.args.remove(self.cmd[0])
        if self.cmd[0] in self.loadedPackages:
            try:
                self.loadedPackages[self.cmd[0]].run(self.args)
            except Exception as e:
                console.log("[red]An Error accoured: " + str(e))
        elif self.cmd[0] in self.ADDONS:
            execstring = "global module; module = " + self.cmd[0]+ "()"
            exec(execstring)
            self.loadedPackages[self.cmd[0]] = module
            module.giveInterpreter(self)
            module.run(self.args)
        else:
            print("[red]This command/addon is unknown. Import it with import <dest>")