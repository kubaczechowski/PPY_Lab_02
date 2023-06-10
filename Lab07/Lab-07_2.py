import tkinter as tk
from tkinter import ttk
import sqlite3

root = tk.Tk()
root.title("Book Store")


def fetch_data():
    conn = sqlite3.connect('bookstore.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS books
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT,
                  author TEXT,
                  price REAL,
                  category TEXT)''')
    c.execute("SELECT * FROM books")
    result = c.fetchall()
    c.close()
    conn.close()
    return result


treeview = ttk.Treeview(root)
treeview["columns"] = ("id", "title", "author", "price", "category")
treeview.column("#0", width=0)
treeview.heading("id", text="ID")
treeview.heading("title", text="Tytuł")
treeview.heading("author", text="Autor")
treeview.heading("price", text="Cena")
treeview.heading("category", text="Kategoria")
treeview.pack()


def load_data():
    data = fetch_data()
    treeview.delete(*treeview.get_children())
    for row in data:
        treeview.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))


def open_new_book_window():
    new_window = tk.Toplevel(root)
    new_window.title("Dodaj nową książkę")
    title_label = ttk.Label(new_window, text="Tytuł:")
    title_label.pack()
    title_entry = ttk.Entry(new_window)
    title_entry.pack()
    author_label = ttk.Label(new_window, text="Autor:")
    author_label.pack()
    author_entry = ttk.Entry(new_window)
    author_entry.pack()
    price_label = ttk.Label(new_window, text="Cena:")
    price_label.pack()
    price_entry = ttk.Entry(new_window)
    price_entry.pack()
    category_label = ttk.Label(new_window, text="Kategoria:")
    category_label.pack()
    category_entry = ttk.Entry(new_window)
    category_entry.pack()

    def add_new():
        # Pobranie wartości z widgetów
        new_title = title_entry.get()
        new_author = author_entry.get()
        new_price = price_entry.get()
        new_category = category_entry.get()
        conn = sqlite3.connect('bookstore.db')
        c = conn.cursor()
        sql = "INSERT INTO books (title, author, price, category) VALUES (?, ?, ?, ?)"
        params = (new_title, new_author, new_price, new_category)
        c.execute(sql, params)
        conn.commit()
        c.close()  # Zamknięcie kursora
        conn.close()
        load_data()
        new_window.destroy()

    add_button = ttk.Button(new_window, text="Dodaj", command=add_new)
    add_button.pack()


add_new_book_button = tk.Button(root, text="Dodaj nową książkę", command=open_new_book_window)
add_new_book_button.pack(side="left")


def open_details_window(event):
    def deleteBook():
        # Usuwanie:
        print(id_entry.get())
        book_id = (id_entry.get())
        conn = sqlite3.connect('bookstore.db')
        c = conn.cursor()
        c.execute("DELETE FROM Books WHERE id=?", (book_id,))
        conn.commit()
        c.close()
        conn.close()
        load_data()

    # Pobranie zaznaczonego elementu
    selected_item = treeview.focus()
    if selected_item:
        # Pobranie danych z zaznaczonego elementu
        item_data = treeview.item(selected_item)
        item_values = item_data["values"]
    # Tworzenie nowego okna
    details_window = tk.Toplevel(root)
    details_window.title("Szczegóły")
    # Tworzenie i wyświetlanie widgetów opartych na danych z zaznaczonego elementu
    id_label = ttk.Label(details_window, text="ID:")
    id_label.pack()
    id_entry = ttk.Entry(details_window)
    id_entry.insert(0, item_values[0])
    id_entry.config(state="disabled")  # Uniemożliwienie zmiany id
    id_entry.pack()
    title_label = ttk.Label(details_window, text="Tytuł:")
    title_label.pack()
    title_entry = ttk.Entry(details_window)
    title_entry.insert(0, item_values[1])
    title_entry.pack()
    author_label = ttk.Label(details_window, text="Autor:")
    author_label.pack()
    author_entry = ttk.Entry(details_window)
    author_entry.insert(0, item_values[2])
    author_entry.pack()
    price_label = ttk.Label(details_window, text="Cena:")
    price_label.pack()
    price_entry = ttk.Entry(details_window)
    price_entry.insert(0, item_values[3])
    price_entry.pack()
    category_label = ttk.Label(details_window, text="Kategoria:")
    category_label.pack()
    category_entry = ttk.Entry(details_window)
    category_entry.insert(0, item_values[4])
    category_entry.pack()
    delete_button = tk.Button(details_window, text="usun ksiazke", command=deleteBook)
    delete_button.pack()


treeview.bind("<Double-1>", open_details_window)


load_data()
root.mainloop()
print(fetch_data())
