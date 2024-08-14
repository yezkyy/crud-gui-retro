import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from app import crud_operations
from gui.forms import ItemForm
from gui.theme import apply_theme
from gui.buttons import create_buttons

def refresh_items(listbox):
    listbox.delete(0, tk.END)
    items = crud_operations.read_items()
    for item in items:
        listbox.insert(tk.END, f"ID: {item[0]} - Name: {item[1]}")

def create_item():
    form = ItemForm(root, title="Create Item")
    if form.name and form.description:
        crud_operations.create_item(form.name, form.description)
        refresh_items(item_listbox)

def update_item():
    selected = item_listbox.curselection()
    if not selected:
        messagebox.showwarning("Select Item", "Please select an item to update.")
        return
    item_id = item_listbox.get(selected).split()[1]
    form = ItemForm(root, title="Update Item")
    if form.name and form.description:
        crud_operations.update_item(item_id, form.name, form.description)
        refresh_items(item_listbox)

def delete_item():
    selected = item_listbox.curselection()
    if not selected:
        messagebox.showwarning("Select Item", "Please select an item to delete.")
        return
    item_id = item_listbox.get(selected).split()[1]
    crud_operations.delete_item(item_id)
    refresh_items(item_listbox)

def search_items():
    search_term = simpledialog.askstring("Search", "Enter item name to search:")
    if search_term:
        listbox_items = [item for item in crud_operations.read_items() if search_term.lower() in item[1].lower()]
        item_listbox.delete(0, tk.END)
        for item in listbox_items:
            item_listbox.insert(tk.END, f"ID: {item[0]} - Name: {item[1]}")

def exit_app():
    root.quit()

def setup_db():
    crud_operations.create_table()

def main():
    global root, item_listbox

    setup_db()

    root = tk.Tk()
    root.title("Enhanced CRUD GUI")

    apply_theme(root)  # Apply the updated theme

    # Frame for buttons
    button_frame = tk.Frame(root, bg='#3E2A6F')
    button_frame.pack(pady=10)

    create_buttons(button_frame, create_item, update_item, delete_item, exit_app)

    # Search bar
    search_button = tk.Button(root, text="Search", command=search_items, bg='#AB47BC', fg='white', font=('Courier', 12, 'bold'), relief=tk.RAISED, bd=4)
    search_button.pack(pady=10)

    # Listbox for displaying items
    item_listbox = tk.Listbox(root, width=60, height=15, bg='#CE93D8', fg='#4A0072', font=('Courier', 12), selectbackground='#D500F9', selectforeground='white')
    item_listbox.pack(padx=20, pady=10)

    refresh_items(item_listbox)

    root.mainloop()

if __name__ == "__main__":
    main()
