from tkinter import *
from tkinter.ttk import *

class App():
    def __init__(self, master):
        self.master = master

        self.master.title("xPick")

        self.frame = Frame(self.master, padding="20", relief='sunken')
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))

        self.search = StringVar()
        self.search_entry = Entry()
        self.search_entry.grid(row=1, column=0, columnspan=3, sticky=N+S+E+W)
        self.search_entry.configure(foreground='green')
        self.search_entry.focus()

        self.progress = Progressbar(self.frame)
        self.progress.grid(column=1, row=3, columnspan=3, sticky=N+S+E+W)
        self.progress.start()

root = Tk()
app = App(root)
root.mainloop()
