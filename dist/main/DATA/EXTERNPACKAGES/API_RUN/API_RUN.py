from PACKET import *PACKETNAME = "API_RUN"class API_RUN(PACKET):    def __init__(self):        PACKET.__init__(self)        self.packname = "API_RUN"        self.packinfo = "a gui to delete all packages"        self.packversion = 1.3    def setup(self, args=None):        PACKET.setup(self)        self.download_dependency("codeEdit.py")    def run(self):        global codeEdit        codeEdit = self.loadExternClass("codeEdit.py")        #self.interpreter.initializePacket("GUI")        try:            gui = self.interpreter.loadedPackages["GUI"]        except:            self.interpreter.askCommand("GUI")            gui = self.interpreter.loadedPackages["GUI"]        self.gui = gui        self.code_EDIT = codeEdit(self)        #self.code_field.bind("<(>", lambda e: self.code_field.after(10, self.finish_bracket))        #self.code_field.bind('<">', lambda e: self.code_field.after(10, self.finish_quotes))    def finish_bracket(self):        cursor = self.code_field.index("current")        print()        self.code_field.insert(round(float(cursor)-0.1, 1), ")")        self.code_field.mark_set("insert", cursor)    def finish_quotes(self):        cursor = self.code_field.index("current")        self.code_field.insert(round(float(cursor)-0.1, 1), '"')        self.code_field.mark_set("insert", cursor)