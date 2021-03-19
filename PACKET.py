from GLOBAL import *


class PACKET():
    def __init__(self):
        self.interpreter = None
        self.info = "Generic Packet info..."
        self.name = "PACKET"

    def giveInterpreter(self, interpreter):
        self.interpreter = interpreter

    def setup(self):
        console.log("This Packet does not have a setup function.")

    def unzip(self, zipFilePath, zipFile):
        with zipfile.ZipFile(zipFilePath + zipFile, 'r') as zip_ref:
            zip_ref.extractall(zipFilePath)
        os.system("del " + zipFilePath + zipFile)

    def download_dependency(self, file):
        r = requests.get(str(SERVERURL) + "/" + str(self.name) + "/" + file)
        with open(str(DATAFOLDER) + "/EXTERNPACKAGES/" + str(self.name) + "/" + str(file), 'wb') as pypdf:
            pypdf.write(r.content)

    def run(self, args):

        ret = 1

        if len(args) > 0:
            if args[0].upper() == "INFO":
                console.log(self.info)
            elif args[0].upper() == "SETUP":
                self.setup()
            else:
                ret = 0
        else:
            ret = 0

        return ret