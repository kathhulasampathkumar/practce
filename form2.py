from tkinter import *
import sqlite3
from tkinter import ttk

root = Tk()
root.geometry("700x500")

# Create a SQLite database and connect to it
conn = sqlite3.connect('registration.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS registrations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        email TEXT
    )
''')

def getvals():
    name = nameval.get()
    phone = phoneval.get()
    email = emailval.get()

    # Insert data into the table
    cursor.execute('INSERT INTO registrations (name, phone, email) VALUES (?, ?, ?)', (name, phone, email))

    # Commit the changes to the database
    conn.commit()

    # Clear the entry fields
    nameval.set("")
    phoneval.set("")
    emailval.set("")

    print("Data Inserted")
    display_records()

def display_records():
    records = cursor.execute('SELECT * FROM registrations').fetchall()

    # Clear previous records in the Treeview
    for row in tree.get_children():
        tree.delete(row)

    # Insert new records into the Treeview
    for record in records:
        tree.insert("", "end", values=record)

Label(root, text="Python Registration Form", font="ar 15 bold").grid(row=0, column=3)
Label(root, text="Name", font="ar 10 ").grid(row=1, column=2)
Label(root, text="Phone", font="ar 10 ").grid(row=2, column=2)
Label(root, text="Email", font="ar 10 ").grid(row=3, column=2)

nameval = StringVar()
phoneval = StringVar()
emailval = StringVar()

EntyName = Entry(root, textvariable=nameval).grid(row=1, column=3)
EntyPhone = Entry(root, textvariable=phoneval).grid(row=2, column=3)
EntyEmail = Entry(root, textvariable=emailval).grid(row=3, column=3)

Button(text="Submit", command=getvals).grid(row=4, column=3)

# Create a Treeview to display records
columns = ("ID", "Name", "Phone", "Email")
tree = ttk.Treeview(root, columns=columns, show='headings')

# Set column headings
for col in columns:
    tree.heading(col, text=col)

tree.grid(row=5, column=2, columnspan=2, pady=10)

# Display existing records
display_records()

root.mainloop()
