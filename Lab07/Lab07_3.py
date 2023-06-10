import tkinter as tk
from tkinter import ttk
import sqlite3

root = tk.Tk()
root.title("Student Management")


def fetch_data():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  age INTEGER,
                  grade INTEGER,
                  address TEXT)''')
    c.execute("SELECT * FROM students")
    result = c.fetchall()
    c.close()
    conn.close()
    return result


treeview = ttk.Treeview(root)
treeview["columns"] = ("id", "name", "age", "grade", "address")
treeview.column("#0", width=0)
treeview.heading("id", text="ID")
treeview.heading("name", text="Name")
treeview.heading("age", text="Age")
treeview.heading("grade", text="Grade")
treeview.heading("address", text="Address")
treeview.pack()


def load_data():
    data = fetch_data()
    treeview.delete(*treeview.get_children())
    for row in data:
        treeview.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))


def open_new_student_window():
    new_window = tk.Toplevel(root)
    new_window.title("Add New Student")
    name_label = ttk.Label(new_window, text="Name:")
    name_label.pack()
    name_entry = ttk.Entry(new_window)
    name_entry.pack()
    age_label = ttk.Label(new_window, text="Age:")
    age_label.pack()
    age_entry = ttk.Entry(new_window)
    age_entry.pack()
    grade_label = ttk.Label(new_window, text="Grade:")
    grade_label.pack()
    grade_entry = ttk.Entry(new_window)
    grade_entry.pack()
    address_label = ttk.Label(new_window, text="Address:")
    address_label.pack()
    address_entry = ttk.Entry(new_window)
    address_entry.pack()

    def add_new():
        new_name = name_entry.get()
        new_age = age_entry.get()
        new_grade = grade_entry.get()
        new_address = address_entry.get()
        conn = sqlite3.connect('student.db')
        c = conn.cursor()
        sql = "INSERT INTO students (name, age, grade, address) VALUES (?, ?, ?, ?)"
        params = (new_name, new_age, new_grade, new_address)
        c.execute(sql, params)
        conn.commit()
        c.close()
        conn.close()
        load_data()
        new_window.destroy()

    add_button = ttk.Button(new_window, text="Add", command=add_new)
    add_button.pack()


add_new_student_button = tk.Button(root, text="Add New Student", command=open_new_student_window)
add_new_student_button.pack(side="left")


def open_details_window(event):
    def deleteStudent():
        selected_item = treeview.focus()
        if selected_item:
            item_data = treeview.item(selected_item)
            item_values = item_data["values"]
            student_id = item_values[0]
            conn = sqlite3.connect('student.db')
            c = conn.cursor()
            c.execute("DELETE FROM students WHERE id=?", (student_id,))
            conn.commit()
            c.close()
            conn.close()
            load_data()

    selected_item = treeview.focus()
    if selected_item:
        item_data = treeview.item(selected_item)
        item_values = item_data["values"]
        details_window = tk.Toplevel(root)
        details_window.title("Details")
        id_label = ttk.Label(details_window, text="ID:")
        id_label.pack()
        id_entry = ttk.Entry(details_window)
        id_entry.insert(0, item_values[0])
        id_entry.config(state="disabled")
        id_entry.pack()
        name_label = ttk.Label(details_window, text="Name:")
        name_label.pack()
        name_entry = ttk.Entry(details_window)
        name_entry.insert(0, item_values[1])
        name_entry.pack()
        age_label = ttk.Label(details_window, text="Age:")
        age_label.pack()
        age_entry = ttk.Entry(details_window)
        age_entry.insert(0, item_values[2])
        age_entry.pack()
        grade_label = ttk.Label(details_window, text="Grade:")
        grade_label.pack()
        grade_entry = ttk.Entry(details_window)
        grade_entry.insert(0, item_values[3])
        grade_entry.pack()
        address_label = ttk.Label(details_window, text="Address:")
        address_label.pack()
        address_entry = ttk.Entry(details_window)
        address_entry.insert(0, item_values[4])
        address_entry.pack()
        delete_button = tk.Button(details_window, text="Delete Student", command=deleteStudent)
        delete_button.pack()


treeview.bind("<Double-1>", open_details_window)


load_data()
root.mainloop()
print(fetch_data())
