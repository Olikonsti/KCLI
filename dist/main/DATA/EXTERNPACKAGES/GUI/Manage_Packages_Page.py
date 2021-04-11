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

        self.inner = packet.VerticalScrolledFrame(self)
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
            button = self.packet.INSTALLBUTTON(self.packet, self.inner.interior, b, self)
            button.pack()

        self.update_task()

    def update_task(self):
        self.packet.window.after(100, self.update_task)
        if self.packet.interpreter.ADDONS != self.copy_Addons:

            self.inner.destroy()

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
                button = self.packet.INSTALLBUTTON(self.packet, self.inner.interior, b, self)
                button.pack()



        self.copy_Addons = self.packet.interpreter.ADDONS.copy()

    def exit_window(self):
        self.packet.notebook.pack(
            expand=True, fill=BOTH)

    def install(self, pack):
        a = threading.Thread(target=lambda: self.packet.interpreter.askCommand("INSTALL get " + pack))
        a.start()
        self.exit_window()
        #self.launch_loading_screen(a)

    def launch_loading_screen(self, thread):
        self.packet.notebook.pack_forget()
        loading_page = self.packet.Loading_Page(self.packet.window, self.packet)
        while thread.is_alive():
            self.packet.window.update()
        loading_page.destroy()
        self.exit_window()

    def get_url_paths(self, url, ext='', params={}):
        response = requests.get(url, params=params)
        if response.ok:
            response_text = response.text
        else:
            return response.raise_for_status()
        soup = BeautifulSoup(response_text, 'html.parser')
        parent = [url + node.get('href') for node in soup.find_all('a') if not node.get('href').endswith(ext) and not node.get('href').startswith("?")]
        return parent