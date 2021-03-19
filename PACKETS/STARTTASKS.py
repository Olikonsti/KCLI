from PACKET import *

class STARTTASKS(PACKET):
    def __init__(self):
        PACKET.__init__(self)
        self.info = "A Packet to automatically initialize packages they were specified with 'add' or 'addimport'\n" \
                    "'list'\n" \
                    "'removeimport'"


    def run(self, args):

        if len(args) > 0 and PACKET.run(self, args) == 0:
            pass
        else:
            pass

        if args[0].upper() == "RUN":
            try:
                f = open(DATAFOLDER + "STARTTASKS/STARTTASKS.py", "r")
                exec(f.read())
                f.close()
                console.log("Starting Starttasks")
                for i in taskimport:
                    console.log("Starting import of " + i)
                    self.interpreter.askCommand("import " + DATAFOLDER + "EXTERNPACKAGES/" + i + "/" + i)
                for i in tasklist:
                    self.interpreter.askCommand(i)

            except Exception as e:
                console.log("[red]FATAL ERROR: Starttasks Packet ran into a fatal startup error! \n\n" + str(e))
                console.log("\nResolve the Error and restart the program!")
                console.input("PRESS ENTER TO EXIT")
                self.interpreter.askCommand("util exit")

        elif args[0].upper() == "LIST":
            try:
                f = open(DATAFOLDER + "STARTTASKS/STARTTASKS.py", "r")
                exec(f.read())
                f.close()
                console.log("Startimports:\n")
                for i in taskimport:
                    console.log("   " + i)
                console.log("\nStartcommands:\n")
                for i in tasklist:
                    console.log("   " + i)

            except Exception as e:
                console.log("[red]FATAL ERROR: Starttasks Packet ran into a fatal startup error! \n\n" + str(e))

        elif args[0].upper() == "ADD":
            try:
                f = open(DATAFOLDER + "STARTTASKS/STARTTASKS.py", "r")
                exec(f.read())
                f.close()
                w = ""
                for i in args[1:]:
                    w += i + " "
                console.log("adding Starttask " + w)
                tasklist.append(w)
                f = open(DATAFOLDER + "STARTTASKS/STARTTASKS.py", "w")
                f.write("global taskimport; taskimport = " + str(taskimport) + "\nglobal tasklist; tasklist = " + str(tasklist))
                f.close()
            except Exception as e:
                console.log("[red]" + str(e))

        elif args[0].upper() == "ADDIMPORT":
            try:

                f = open(DATAFOLDER + "STARTTASKS/STARTTASKS.py", "r")
                exec(f.read())
                f.close()
                console.log("adding Startimport " + args[1])
                if args[1].upper() not in taskimport:
                    taskimport.append(args[1])
                else:
                    console.log("Starttask already in list")
                f = open(DATAFOLDER + "STARTTASKS/STARTTASKS.py", "w")
                f.write("global taskimport; taskimport = " + str(taskimport) + "\nglobal tasklist; tasklist = " + str(tasklist))
                f.close()
            except Exception as e:
                console.log("[red]" + str(e))

        elif args[0].upper() == "REMOVEIMPORT":
            try:

                f = open(DATAFOLDER + "STARTTASKS/STARTTASKS.py", "r")
                exec(f.read())
                f.close()
                if args[1].upper() in taskimport:
                    taskimport.remove(args[1])
                    console.log("removing Startimport " + args[1])
                else:
                    console.log("Starttask not in list")
                f = open(DATAFOLDER + "STARTTASKS/STARTTASKS.py", "w")
                f.write("global taskimport; taskimport = " + str(taskimport) + "\nglobal tasklist; tasklist = " + str(tasklist))
                f.close()
            except Exception as e:
                console.log("[red]" + str(e))



