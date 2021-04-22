from tkinter import *
import tkinter.ttk as ttk
import requests
from bs4 import BeautifulSoup
from GLOBAL import *

class mainclass(Frame):
    def __init__(self, notebook, packet):
        Frame.__init__(self, notebook)
        self.packet = packet
        self.copy_Addons = self.packet.interpreter.ADDONS.copy()

        self.inner = packet.VerticalScrolledFrame(self, width=50)
        self.inner.pack(side=BOTTOM)

        self.searchframe = Frame(self)
        self.searchframe.pack()
        self.searchBox = ttk.Entry(self.searchframe)
        self.searchBox.pack(side=LEFT)
        self.searchReset = ttk.Button(self.searchframe, text="X", width=3,
                                      command=lambda: self.searchBox.delete(0, END))
        self.searchReset.pack(side=LEFT)
        self.last_search = ""
        self.searching = False
        self.searching_reset = False

        global LISTIMAGE

        class LISTIMAGE():
            def __init__(self, parent, pack):
                i = pack
                self.packImageContainer = parent
                r = requests.get(str(SERVERURL) + "/" + str(i) + "/" + "1icon.png")
                with open(str(DATAFOLDER) + "/TEMP/" + "1icon.png" + i, 'wb') as pypdf:
                    pypdf.write(r.content)
                self.icon = Image.open(DATAFOLDER + "TEMP/" + "1icon.png" + i).convert("RGBA")
                self.icon = self.icon.resize((60, 60), Image.BOX)
                self.image = ImageTk.PhotoImage(self.icon)
                self.packImageContainer.create_image(30, 30, image=self.image)




        self.redraw_frame()

        self.update_task()

    def update_task(self):
        self.packet.window.after(100, self.update_task)

        if self.searchBox.get() == "":
            self.searching = False

            if self.searching_reset == False:
                self.redraw_frame()
                self.searching_reset = True

        else:
            self.searching_reset = False
            self.searching = True
            if self.last_search != self.searchBox.get().upper():
                self.redraw_frame()
            self.last_search = self.searchBox.get().upper()



        if self.packet.interpreter.ADDONS != self.copy_Addons:
            self.redraw_frame()

        self.copy_Addons = self.packet.interpreter.ADDONS.copy()

    def redraw_frame(self):
        self.packets_names = []
        self.inner.destroy()

        self.amount_found = 0

        self.inner = self.packet.VerticalScrolledFrame(self)
        self.inner.pack(side=BOTTOM, fill=BOTH, expand=TRUE)

        packets = self.get_url_paths(SERVERURL, ".py")
        packets.remove(packets[0])
        for i in packets.copy():
            b = i
            b = b.removeprefix(SERVERURL)
            b = b.removeprefix("/")
            b = b.removesuffix("/")
            if b in self.packet.interpreter.ADDONS:
                packets.remove(i)

        for i in packets:
            b = i.removeprefix(SERVERURL)
            b = b.removeprefix("/")
            b = b.removesuffix("/")
            self.packets_names.append(b)

        self.packets_names.remove("message.txt")

        if self.searching:
            for i in self.packets_names.copy():
                if i.startswith(self.searchBox.get().upper()):
                    self.amount_found += 1
                else:
                    self.packets_names.remove(i)
        else:
            self.packet.window.unbind_all('<Return>')
            self.amount_found += 1

        if self.amount_found == 0:
            Label(self.inner.interior, text="Nothing Found").pack()



        self.createButton(self.packets_names)

    def createButton(self, list):
        self.images = []

        lineFrame = Frame(self.inner.interior)
        lineFrame.pack()

        counter = -1
        for i in list:

            if counter < 2:
                counter += 1
            else:
                counter = 0
                lineFrame = Frame(self.inner.interior)
                lineFrame.pack()

            itemframe = Frame(lineFrame, highlightthickness=1, highlightbackground="lightgrey")
            itemframe.pack(side=LEFT, pady=2, padx=2)

            button = self.packet.INSTALLBUTTON(self.packet, itemframe, i, self)
            button.pack(side=LEFT, padx=5)
            self.packImageContainer = Canvas(itemframe, width=60, height=60, highlightthickness=1, highlightbackground="lightgrey")
            self.packImageContainer.pack(side=RIGHT, pady=5, padx=(0, 5))

            try:
                self.image = LISTIMAGE(self.packImageContainer, i)
                self.images.append(self.image)
            except:
                pass

    def exit_window(self):
        self.packet.notebook.pack(
            expand=True, fill=BOTH)

    def install(self, pack):
        a = threading.Thread(target=lambda: self.packet.interpreter.askCommand("INSTALL get " + pack))
        a.start()
        message = Label(self.packet.window, text=f"Install task for {pack} is running... Please wait", fg="white", bg="green")
        message.pack(fill=X)
        self.exit_window()
        while a.is_alive():
            self.packet.window.update()
        message.destroy()

    def get_url_paths(self, url, ext='', params={}):
        response = requests.get(url, params=params)
        if response.ok:
            response_text = response.text
        else:
            return response.raise_for_status()
        soup = BeautifulSoup(response_text, 'html.parser')
        parent = [url + node.get('href') for node in soup.find_all('a') if not node.get('href').endswith(ext) and not node.get('href').startswith("?")]
        return parent