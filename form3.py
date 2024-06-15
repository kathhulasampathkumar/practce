from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

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

def edit_record():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("No Record Selected", "Please select a record to edit.")
        return

    record = tree.item(selected_item, 'values')
    new_name = simpledialog.askstring("Edit Name", "Enter new name:", initialvalue=record[1])
    new_phone = simpledialog.askstring("Edit Phone", "Enter new phone:", initialvalue=record[2])
    new_email = simpledialog.askstring("Edit Email", "Enter new email:", initialvalue=record[3])

    if new_name and new_phone and new_email:
        # Update the selected record in the database
        cursor.execute('''
            UPDATE registrations 
            SET name=?, phone=?, email=? 
            WHERE id=?
        ''', (new_name, new_phone, new_email, record[0]))

        # Commit the changes to the database
        conn.commit()

        print("Record Updated")
        display_records()

def delete_record():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("No Record Selected", "Please select a record to delete.")
        return

    confirmation = messagebox.askyesno("Delete Record", "Are you sure you want to delete this record?")
    if confirmation:
        record_id = tree.item(selected_item, 'values')[0]
        # Delete the selected record from the database
        cursor.execute('DELETE FROM registrations WHERE id=?', (record_id,))
        # Commit the changes to the database
        conn.commit()

        print("Record Deleted")
        display_records()

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

# Add Edit and Delete buttons
edit_button = Button(root, text="Edit", command=edit_record)
edit_button.grid(row=6, column=2, pady=5)

delete_button = Button(root, text="Delete", command=delete_record)
delete_button.grid(row=6, column=3, pady=5)

root.mainloop()
