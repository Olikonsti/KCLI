from tkinter import *
import tkinter.ttk as ttk
from GLOBAL import *


class mainclass(Frame):
    def __init__(self, notebook, packet):
        Frame.__init__(self, notebook)
        self.packet = packet

        self.installed_packs_frame_border = LabelFrame(self, text="Installed Packages")
        self.installed_packs_frame_border.pack(side=LEFT, fill=Y)
        self.installed_packs_frame = packet.VerticalScrolledFrame(self.installed_packs_frame_border)
        self.installed_packs_frame.pack(fill=Y, expand=True)

        self.exclusion_list = ["RESTORE", "GUI"]
        self.installed_packs_shown = []

        self.config()
        for i in packet.interpreter.ADDONS:
            if i in ADDONS or i in self.exclusion_list:
                self.installed_packs_shown.append(i)
            else:
                self.installed_packs_shown.append(i)
                a = packet.BUTTON(packet, self.installed_packs_frame.interior, i)
                a.pack()



        self.update_task()

    def update_task(self):
        self.after(1000, self.update_task)

        # Packet starter frame refresh
        if self.installed_packs_shown == self.packet.interpreter.ADDONS:
            pass
        else:
            # clear frame
            self.installed_packs_frame.destroy()
            self.installed_packs_frame = self.packet.VerticalScrolledFrame(self.installed_packs_frame_border)
            self.installed_packs_frame.pack(fill=Y, expand=True)

            console.log(self.installed_packs_shown)
            console.log(self.packet.interpreter.ADDONS)

            for i in self.installed_packs_shown.copy():
                if i not in self.packet.interpreter.ADDONS:
                    self.installed_packs_shown.remove(i)

            for i in self.packet.interpreter.ADDONS:
                if i in ADDONS or i in self.exclusion_list:
                    pass
                else:
                    if i not in self.installed_packs_shown:
                        self.installed_packs_shown.append(i)
                        console.log("appended: " + i)
                    a = self.packet.BUTTON(self.packet, self.installed_packs_frame.interior, i)
                    a.pack()