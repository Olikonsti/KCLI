from tkinter import *
import tkinter.ttk as ttk
from GLOBAL import *


class mainclass(Frame):
    def __init__(self, notebook, packet):
        Frame.__init__(self, notebook)
        self.packet = packet

        self.message_field_border = ttk.LabelFrame(self, text="Message")
        self.message_field_border.pack(side=RIGHT, fill=BOTH, expand=True, pady=5, padx=5)

        self.message_field = packet.VerticalScrolledFrame(self.message_field_border)
        self.message_field.pack(fill=BOTH, expand=True, anchor=NW, side=LEFT)

        if requests.get(SERVERURL + "/" + "message.txt").status_code == 200:
            Label(self.message_field.interior, text=requests.get(
                SERVERURL + "/message.txt").text, justify=LEFT).pack(anchor=NW, pady=5, padx=5)



        self.installed_packs_frame_border = ttk.LabelFrame(self, text="Installed Packages")
        self.installed_packs_frame_border.pack(side=LEFT, fill=Y, pady=5, padx=5)

        self.searchframe = Frame(self.installed_packs_frame_border)
        self.searchframe.pack()
        self.searchBox = ttk.Entry(self.searchframe)
        self.searchBox.pack(side=LEFT)
        self.searchReset = ttk.Button(self.searchframe, text="X", width=3, command=lambda: self.searchBox.delete(0, END))
        self.searchReset.pack(side=LEFT)
        self.last_search = ""
        self.searching = False
        self.searching_reset = False

        self.installed_packs_frame = packet.VerticalScrolledFrame(self.installed_packs_frame_border, width=400)
        self.installed_packs_frame.pack(fill=BOTH, expand=True)

        self.exclusion_list = ["RESTORE"]
        self.installed_packs_shown = []

        for i in packet.interpreter.ADDONS:
            if i in ADDONS or i in self.exclusion_list:
                self.installed_packs_shown.append(i)
            else:
                self.installed_packs_shown.append(i)
                a = packet.BUTTON(packet, self.installed_packs_frame.interior, i)
                a.pack(expand=True, fill=X)

        self.update_task()

    def update_task(self):
        self.after(70, self.update_task)

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

        # Packet starter frame refresh
        if self.installed_packs_shown == self.packet.interpreter.ADDONS:
            pass
        else:
            self.redraw_frame()



    def redraw_frame(self):
        # clear frame
        self.installed_packs_frame.destroy()
        self.installed_packs_frame = self.packet.VerticalScrolledFrame(self.installed_packs_frame_border)
        self.installed_packs_frame.pack(fill=BOTH, expand=True)

        for i in self.installed_packs_shown.copy():
            if i not in self.packet.interpreter.ADDONS:
                self.installed_packs_shown.remove(i)

        self.amount_found = 0
        for i in self.packet.interpreter.ADDONS:
            if i in ADDONS or i in self.exclusion_list:
                pass
            else:
                if i not in self.installed_packs_shown:
                    self.installed_packs_shown.append(i)

                if self.searching:
                    if i.startswith(self.searchBox.get().upper()):
                        a = self.packet.BUTTON(self.packet, self.installed_packs_frame.interior, i)
                        a.pack(expand=True, fill=X)
                        if self.amount_found == 0:
                            self.packet.window.bind_all("<Return>", lambda e: [a.click(), self.searchBox.delete(0, END)])
                        self.amount_found += 1
                else:
                    self.packet.window.unbind_all('<Return>')
                    self.amount_found += 1
                    a = self.packet.BUTTON(self.packet, self.installed_packs_frame.interior, i)
                    a.pack(expand=True, fill=X)
        if self.amount_found == 0:
            Label(self.installed_packs_frame.interior, text="Nothing Found").pack()