# KCLI
My own CLI for installing many programs without extracting zip folders

## Creating a KCLI Package

- step 1:

    create the following folder structure and change PYGEO to the name of your package:
   
    ![Screenshot 2021-03-24 191113](https://user-images.githubusercontent.com/68354546/112466782-84418880-8d66-11eb-8b3a-6e176e984a3e.png)

    in the .zip you can put an .exe and folder that the package can execute easily

- step 2:

    edit the .py file (the packet script)
    Example:
    ```python
from PACKET import *

PACKETNAME = "PYGEO"



class PYGEO(PACKET):

    def __init__(self):

        PACKET.__init__(self)


        self.name = "PYGEO"
        self.info = "a math plotting program"

    def setup(self):
        self.download_dependency("dist.zip")
        
        self.unzip(DATAFOLDER2 + "EXTERNPACKAGES\\" + self.name,"\\dist.zip")



    def run(self, args):

        

        if PACKET.run(self, args) == 0:

            pass

        else:

            return 0

        os.system("cd " + DATAFOLDER + "EXTERNPACKAGES/" + self.name + "/ & main.exe")```
        
   fdksljfd
