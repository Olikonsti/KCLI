from GLOBAL import *


class PACKET():
    def __init__(self):
        self.interpreter = None
        self.packinfo = "Generic Packet info..."
        self.packname = "PACKET"
        self.packversion = "v1.0"

    def giveInterpreter(self, interpreter):
        self.interpreter = interpreter

    def uninstall(self):
        console.log(f"packed {self.packname} will now run its uninstall task!")

    def setup(self, args=None):
        self.download_dependency("1icon.png")

    def info(self, args):
        console.log(self.packinfo)

    def version(self, args):
        console.log(self.packversion)

    def givePacketInstance(self, packet):
        response = self.interpreter.initializePacket(packet)
        if response == 1:
            return None
        else:
            return self.interpreter.loadedPackages[packet]

    def unzip(self, zipFilePath, zipFile):
        with zipfile.ZipFile(zipFilePath + zipFile, 'r') as zip_ref:
            zip_ref.extractall(zipFilePath)
        os.system("del " + zipFilePath + zipFile)

    def loadExternClass(self, filename):
        f = open(str(DATAFOLDER) + "/EXTERNPACKAGES/" + str(self.packname) + "/" + filename, "r")
        code = f.read()
        f.close()
        try:
            exec(f"global mainclass;" + code)

        except Exception as e:
            console.log(f"[red]An error in the Subpacket ({filename}) in the Packet ({self.packname}) accoured: {e}")

        return mainclass



    def download_dependency(self, file):
        r = requests.get(str(SERVERURL) + "/" + str(self.packname) + "/" + file)
        with open(str(DATAFOLDER) + "/EXTERNPACKAGES/" + str(self.packname) + "/" + str(file), 'wb') as pypdf:
            pypdf.write(r.content)

    def run(self):
        console.log("[yellow] The Packet.run(args) has been depreciated!!! Please use Packet.runasfunctions from now on!")
        return 0