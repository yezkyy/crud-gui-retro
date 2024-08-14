import tkinter as tk
from tkinter import simpledialog

class ItemForm(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        self.name = None
        self.description = None
        super().__init__(parent, title)

    def body(self, master):
        tk.Label(master, text="Name:").grid(row=0)
        tk.Label(master, text="Description:").grid(row=1)

        self.name_entry = tk.Entry(master)
        self.description_entry = tk.Entry(master)

        self.name_entry.grid(row=0, column=1)
        self.description_entry.grid(row=1, column=1)

        return self.name_entry

    def apply(self):
        self.name = self.name_entry.get()
        self.description = self.description_entry.get()