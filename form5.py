from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageTk

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

        # Generate barcode for each record
        barcode_data = f"{record[1]} - {record[2]} - {record[3]}"
        code128 = barcode.get_barcode_class('code128')
        code = code128(barcode_data, writer=ImageWriter(), add_checksum=False)
        barcode_image = code.render()

        # Convert the PIL Image to a Tkinter PhotoImage
        tk_image = ImageTk.PhotoImage(Image.fromarray(barcode_image._image_array))

        # Display the barcode image in a new column
        tree.insert(tree.get_children()[-1], 0, values=('', '', '', ''), image=tk_image)

        # Save the reference to avoid garbage collection
        tree.image_references.append(tk_image)

# Add a new column for the barcode
columns = ("Barcode", "ID", "Name", "Phone", "Email")
tree = ttk.Treeview(root, columns=columns, show='headings')

# Set column headings
for col in columns:
    tree.heading(col, text=col)

tree.grid(row=5, column=2, columnspan=3, pady=10)

# Display existing records
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

# Image references to avoid garbage collection
tree.image_references = []

# Add Edit and Delete buttons
edit_button = Button(root, text="Edit", command=edit_record)
edit_button.grid(row=6, column=2, pady=5)

delete_button = Button(root, text="Delete", command=delete_record)
delete_button.grid(row=6, column=3, pady=5)

root.mainloop()
