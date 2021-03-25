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
        self.version = "v1.1"

    def setup(self):                        # gets called once, when the packet is intalled
    
        self.download_dependency("dist.zip") # downloads the dist.zip that can have .exe files or folders in it
        self.unzip(DATAFOLDER2 + "EXTERNPACKAGES\\" + self.name,"\\dist.zip")       # this line is just for unpacking the zip folder



    def run(self, args):                    # this function gets called everytime the packet is launched in the KCLI (args are the commands arguments)

        

        if PACKET.run(self, args) == 0:     # this code just checks if the command is a special command like info or version
            pass
        else:
            return 0

        os.system("cd " + DATAFOLDER + "EXTERNPACKAGES/" + self.name + "/ & main.exe")      # this line executes the .exe of the packet
 ```

