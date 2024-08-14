import tkinter as tk

def create_buttons(parent, create_item, update_item, delete_item, exit_app):
    button_frame = parent

    # Tombol CRUD
    tk.Button(button_frame, text="Create Item", command=create_item, **button_style()).grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="Update Item", command=update_item, **button_style()).grid(row=0, column=1, padx=10)
    tk.Button(button_frame, text="Delete Item", command=delete_item, **button_style()).grid(row=0, column=2, padx=10)

    # Tombol Exit
    tk.Button(parent.master, text="Exit", command=exit_app, **exit_button_style()).pack(pady=10)

def button_style():
    return {
        'bg': '#6A1B9A',
        'fg': 'white',
        'font': ('Courier', 12, 'bold'),
        'relief': tk.RAISED,
        'bd': 4,
    }

def exit_button_style():
    return {
        'bg': '#AB47BC',
        'fg': 'white',
        'font': ('Courier', 12, 'bold'),
        'relief': tk.RAISED,
        'bd': 4,
    }