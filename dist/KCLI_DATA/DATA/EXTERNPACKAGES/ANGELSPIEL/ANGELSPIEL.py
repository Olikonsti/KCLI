from PACKET import *PACKETNAME = "ANGELSPIEL"class ANGELSPIEL(PACKET):    def __init__(self):        PACKET.__init__(self)        self.packname = "ANGELSPIEL"        self.packinfo = "the all new ANGELSPIEL!!!\n(Beta prerelease)"        self.packversion = 0.1    def setup(self, args=None):        PACKET.setup(self)        self.download_dependency("dist.zip")        self.unzip(DATAFOLDER2 + "EXTERNPACKAGES\\" + self.packname,"\\dist.zip")    def run(self):        os.system("cd " + DATAFOLDER + "EXTERNPACKAGES/" + self.packname + "/ & start main.exe")    def test(self, args):        print("TEST")        