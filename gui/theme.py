import tkinter as tk
from tkinter import ttk

def apply_theme(root):
    root.configure(bg='#3E2A6F')

    # Apply styles
    style = ttk.Style()
    style.configure('TButton',
                    background='#6A1B9A',
                    foreground='white',
                    font=('Courier', 12, 'bold'),
                    relief='raised')
    style.configure('TFrame', background='#3E2A6F')
    style.configure('TLabel', background='#3E2A6F', foreground='white')
    style.configure('TEntry', background='#CE93D8', foreground='#4A0072')

def create_buttons(frame, create_cmd, update_cmd, delete_cmd, exit_cmd):
    ttk.Button(frame, text="Create Item", command=create_cmd).grid(row=0, column=0, padx=10)
    ttk.Button(frame, text="Update Item", command=update_cmd).grid(row=0, column=1, padx=10)
    ttk.Button(frame, text="Delete Item", command=delete_cmd).grid(row=0, column=2, padx=10)
    ttk.Button(frame, text="Exit", command=exit_cmd).grid(row=0, column=3, padx=10)
