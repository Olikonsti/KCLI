from GLOBAL import *

class mainclass():
    def __init__(self, api):
        self.last_path = ""
        frame = Frame()
        self.frame = frame
        self.api = api
        api.gui.create_tab(frame, "API_RUN")

        self.navBar = Frame(frame, height=5)
        self.navBar.pack(fill=X)

        ttk.Separator(self.navBar).pack(fill=X, side=BOTTOM)

        self.back_button = ttk.Button(self.navBar, text="x", width=3, command=self.exit)
        self.back_button.pack(side=LEFT)

        self.run_button = ttk.Button(self.navBar, text="Run", command=self.runc)
        self.run_button.pack(side=LEFT, padx=(40, 0))

        self.save_button = ttk.Button(self.navBar, text="Save", command=self.saveFile)
        self.save_button.pack(side=LEFT)

        self.open_button = ttk.Button(self.navBar, text="Open", command=self.openFile)
        self.open_button.pack(side=LEFT)

        self.code_field = Text(frame, font="Consolas 12")
        self.code_field.pack(expand=True, fill=BOTH)

    def saveFile(self):
        file = filedialog.asksaveasfile("w")
        if file:
            f = open(file.name, "w")
            f.write(self.code_field.get(0.0, END))
            f.close()

    def openFile(self):
        file = filedialog.askopenfile()
        self.last_path = ""
        if file:
            f = open(file.name)
            code = f.read()
            f.close()

            self.code_field.delete('1.0', END)
            self.code_field.insert(0.0, code)

    def runc(self):
        #self.interpreter.execGlobal(self.code_field.get(0.0, END))
        api = self.api
        try:
            exec(self.code_field.get(0.0, END))
        except Exception as e:
            messagebox.showerror("API_RUN Error while running code", e)

    def exit(self, args=None):
        self.api.gui.notebook.select(self.api.gui.homePage)
        self.frame.destroy()