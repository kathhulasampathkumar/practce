from tkinter import *
import sqlite3

root = Tk()
root.geometry("500x500")

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

    print("Data Inserted")

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

root.mainloop()




# from tkinter import *
# root = Tk()
# root.geometry("500x500")
# def getvals():
#     print("Accepted")
# Label(root, text="Python Registration Form", font="ar 15 bold").grid(row=0, column=3)
# name=Label(root,text="Name", font="ar 10 ").grid(row=1, column=2)
# Phone=Label(root,text="Phone", font="ar 10 ").grid(row=2, column=2)
# Email=Label(root,text="Email",font="ar 10 ").grid(row=3, column=2)

# nameval=StringVar
# phoneval=StringVar
# emailval=StringVar

# EntyName = Entry(root, textvariable=nameval).grid(row=1, column=3)
# phoneval = Entry(root, textvariable=phoneval).grid(row=2, column=3)
# emailval = Entry(root, textvariable=emailval).grid(row=3, column=3)
# Button(text="Submit", command=getvals).grid(row=4,column=3)



# root.mainloop()