from tkinter import *
import tkinter.ttk as ttk
from GLOBAL import *

class mainclass(ttk.Frame):
    def __init__(self, notebook, packet):
        ttk.Frame.__init__(self, notebook)
        self.packet = packet

        class AttributeSelectBox(ttk.LabelFrame):
            def __init__(self, parent, text, values):
                super().__init__(parent)
                self.var = StringVar()
                self.config(text=text)
                self.inner = ttk.Combobox(self, textvariable=self.var, state="readonly", values=values)
                self.inner.pack(pady=4, padx=4)

        class AttributeSpinBox(ttk.LabelFrame):
            def __init__(self, parent, text):
                super().__init__(parent)
                self.var = IntVar()
                self.config(text=text)
                self.inner = ttk.Spinbox(self, textvariable=self.var, from_=-10000, to=10000)
                self.inner.pack(pady=4, padx=4)

        class AttributeSwichBox(ttk.Frame):
            def __init__(self, parent, text, mode="checkbutton", state=NORMAL):
                super().__init__(parent)
                self.var = BooleanVar()
                if mode != "switch":
                    self.inner = ttk.Checkbutton(self, text=text, variable=self.var)
                else:
                    try:
                        self.inner = ttk.Checkbutton(self, text=text, variable=self.var, style='Switch', state=state)
                    except:
                        self.inner = ttk.Checkbutton(self, text=text, variable=self.var, state=state)
                self.inner.pack(pady=(0, 8), padx=8)

        #scrollframe
        self.scrollFrame = self.packet.VerticalScrolledFrame(self)
        self.scrollFrame.pack(expand=True, fill=BOTH, padx=4, pady=4)
        if self.packet.theme == "equilux":
            self.scrollFrame.canvas.config(bg="#464646")
        if self.packet.theme == "adapta":
            self.scrollFrame.canvas.config(bg="#FAFBFC")
        if self.packet.theme == "arc":
            self.scrollFrame.canvas.config(bg="#F5F6F7")

        #notes
        ttk.Label(self.scrollFrame.interior, text="Note: modern-dark, modern-light and equilux themes can be slow!", justify=LEFT).pack(side=TOP)


        #appereance
        # theme
        if self.packet.ugly_themes == "True":
            themes = ["modern-dark", "equilux", "modern-light", "adapta", "breeze", "arc", "clam", "win10", "win95"]
        else:
            themes = ["modern-dark", "equilux", "modern-light", "adapta", "breeze", "arc"]

        self.appearance_frame = ttk.LabelFrame(self.scrollFrame.interior, text="Appearance")
        self.appearance_frame.pack(anchor=NW, pady=(0, 10), padx=10)

        self.theme_select = AttributeSelectBox(self.appearance_frame, "Gui Theme", themes)
        try:
            self.theme_select.inner.current(themes.index(packet.theme))
        except Exception as e:
            console.log(e)
        self.theme_select.pack(anchor=NW, pady=(4, 8), padx=8)

        self.ugly_themes_s = AttributeSwichBox(self.appearance_frame, "Display ugly themes in the theme selection", mode="switch")
        with open(f"{DATAFOLDER}/PROGRAMDATA/GUI/ugly_themes.txt", "r") as f:
            self.ugly_themes_s.var.set(f.read())
        self.ugly_themes_s.pack(anchor=NW)

        self.int_packs_s = AttributeSwichBox(self.appearance_frame, "Display Interpreter Packages on Home Tab", mode="switch")
        with open(f"{DATAFOLDER}/PROGRAMDATA/GUI/interpreter_packs.txt", "r") as f:
            self.int_packs_s.var.set(f.read())
        self.int_packs_s.pack(anchor=NW)

        self.menu_s_frame = ttk.Frame(self.appearance_frame)
        self.menu_s_frame.pack()

        self.menuMode_s = AttributeSwichBox(self.menu_s_frame,
                                             "Use GUI Window as Menu without Titlebar",
                                             mode="switch")
        with open(f"{DATAFOLDER}/PROGRAMDATA/GUI/menu_mode.txt", "r") as f:
            self.menuMode_s.var.set(f.read())
            self.menu_advanced_button = ttk.Button(self.menu_s_frame, text="Edit", command=lambda: self.menu_popup.place(x=400, y=18))
            self.menu_advanced_button.pack(side=RIGHT, padx=(0, 8))
        self.menuMode_s.pack(anchor=NW)

        self.MoveGui = AttributeSwichBox(self.appearance_frame, "Move Gui at startup to last known Gui position[SOON]",
                                             mode="switch")
        with open(f"{DATAFOLDER}/PROGRAMDATA/GUI/interpreter_packs.txt", "r") as f:
            pass
            #self.MoveGui.var.set(f.read())
        self.MoveGui.pack(anchor=NW)

        #self.lib_display = AttributeSwichBox(self.scrollFrame.interior, "Display Library Packages on install Packages Tab and Home Tab (SOON)", mode="switch")
        #self.lib_display.pack(anchor=NW)

        self.update_frame = ttk.LabelFrame(self.scrollFrame.interior, text="Updates")
        self.update_frame.pack(anchor=NW, pady=(0, 10), padx=10)

        # other
        self.a_update = AttributeSwichBox(self.update_frame, "Update Gui Automatically", mode="switch")
        with open(f"{DATAFOLDER}/PROGRAMDATA/GUI/auto_update.txt", "r") as f:
            self.a_update.var.set(f.read())
        self.a_update.pack(anchor=NW, pady=(4, 0))

        self.menu_popup = ttk.LabelFrame(self.scrollFrame.interior, width=350, height=250, text="Edit Menu Options")
        self.menu_popup_exit = ttk.Button(self.menu_popup, text="X", width=3, command=lambda: self.menu_popup.place(x=-400, y=-400))
        self.menu_popup_exit.place(x=0, y=0)

        self.posx_s = AttributeSpinBox(self.menu_popup, "X")
        with open(f"{DATAFOLDER}/PROGRAMDATA/GUI/menu_x.txt", "r") as f:
            self.posx_s.var.set(int(f.read()))
        self.posx_s.pack(pady=(30, 0), padx=10)

        self.posy_s = AttributeSpinBox(self.menu_popup, "Y")
        with open(f"{DATAFOLDER}/PROGRAMDATA/GUI/menu_y.txt", "r") as f:
            self.posy_s.var.set(int(f.read()))
        self.posy_s.pack(pady=8, padx=10)

        self.topmost = AttributeSwichBox(self.menu_popup, "Place Menu topmost",
                                               mode="switch")
        with open(f"{DATAFOLDER}/PROGRAMDATA/GUI/menu_topmost.txt", "r") as f:
            self.topmost.var.set(f.read())
        self.topmost.pack(anchor=NW, pady=(4, 8), padx=8)

        self.menu_popup.place(x=-400, y=-400)

        self.bottomFrame = ttk.Frame(self)
        self.reset_button = ttk.Button(self.bottomFrame, text="Reset to default", command=self.reset)
        self.reset_button.pack(side=LEFT, padx=1)
        self.apply_button = ttk.Button(self.bottomFrame, text="Apply", command=self.apply)
        self.apply_button.pack(side=LEFT, padx=1)
        self.bottomFrame.pack(anchor=SE, side=BOTTOM)

        self.updateloop()

    def updateloop(self):
        self.packet.window.after(100, self.updateloop)
        if self.menuMode_s.var.get():
            self.menu_advanced_button.config(state=NORMAL)
            self.MoveGui.inner.config(state=DISABLED)
        else:
            self.menu_popup.place(x=-400, y=-400)
            self.menu_advanced_button.config(state=DISABLED)
            self.MoveGui.inner.config(state=NORMAL)

        if self.MoveGui.var.get():
            self.menu_advanced_button.config(state=DISABLED)
            self.menuMode_s.inner.config(state=DISABLED)
        else:
            if self.menuMode_s.var.get():
                self.menu_advanced_button.config(state=NORMAL)
            else:
                self.menu_advanced_button.config(state=DISABLED)
            self.menuMode_s.inner.config(state=NORMAL)



    def reset(self):
        if messagebox.askquestion("KCLI GUI Warning", "Do you want to reset all KCLI GUI settings to default?", icon="warning") == "yes":
            self.packet.reset()
            self.packet.window.destroy()
            self.packet.interpreter.askCommand("util unload GUI")
            self.packet.interpreter.askCommand("GUI")
            del self
            return 0

    def apply(self):
        console.log("Applying...")

        # Theme
        with open(f"{DATAFOLDER}/PROGRAMDATA/GUI/theme.txt", "w") as f:
            f.write(self.theme_select.var.get())

        # other
        with open(f"{DATAFOLDER}/PROGRAMDATA/GUI/interpreter_packs.txt", "w") as f:
            f.write(str(self.int_packs_s.var.get()))

        with open(f"{DATAFOLDER}/PROGRAMDATA/GUI/ugly_themes.txt", "w") as f:
            f.write(str(self.ugly_themes_s.var.get()))

        with open(f"{DATAFOLDER}/PROGRAMDATA/GUI/auto_update.txt", "w") as f:
            f.write(str(self.a_update.var.get()))

        with open(f"{DATAFOLDER}/PROGRAMDATA/GUI/menu_mode.txt", "w") as f:
            f.write(str(self.menuMode_s.var.get()))

        with open(f"{DATAFOLDER}/PROGRAMDATA/GUI/menu_x.txt", "w") as f:
            f.write(str(self.posx_s.var.get()))

        with open(f"{DATAFOLDER}/PROGRAMDATA/GUI/menu_y.txt", "w") as f:
            f.write(str(self.posy_s.var.get()))

        with open(f"{DATAFOLDER}/PROGRAMDATA/GUI/menu_topmost.txt", "w") as f:
            f.write(str(self.topmost.var.get()))




        # restarting
        self.packet.window.destroy()
        self.packet.interpreter.askCommand("util unload GUI")
        self.packet.interpreter.askCommand("GUI")
        del self
        return 0
