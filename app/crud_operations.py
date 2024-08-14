import sqlite3
from app.models import Item

def connect_db():
    return sqlite3.connect('items.db')

def create_table():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL
            )
        ''')
        conn.commit()

def get_next_available_id():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM items ORDER BY id')
        ids = cursor.fetchall()
        if not ids:
            return 1
        last_id = ids[-1][0]
        available_ids = set(range(1, last_id + 2)) - set(id[0] for id in ids)
        return min(available_ids) if available_ids else last_id + 1

def create_item(name, description):
    item_id = get_next_available_id()
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO items (id, name, description) VALUES (?, ?, ?)', (item_id, name, description))
        conn.commit()

def read_items():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM items')
        return cursor.fetchall()

def update_item(item_id, name, description):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE items SET name = ?, description = ? WHERE id = ?', (name, description, item_id))
        conn.commit()

def delete_item(item_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM items WHERE id = ?', (item_id,))
        conn.commit()