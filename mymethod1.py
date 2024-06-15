from tkinter import *
from tkinter import ttk
import win32api
import win32print
import tempfile
from tkinter.messagebox import showinfo
import mysql.connector

def installed_printer():
    printers = win32print.EnumPrinters(2)
    for p in printers:
        return(p)

printerdef = ''

def locprinter():
    pt = Toplevel()
    pt.title("Choose Printer")
    var1 = StringVar()
    LABEL = Label(pt, text="Select Printer", bg='goldenrod2', fg='black').pack(fill=X)
    PRCOMBO = ttk.Combobox(pt, width=35)
    print_list = []
    printers = list(win32print.EnumPrinters(2))
    for i in printers:
        print_list.append(i[2])
    PRCOMBO['values'] = print_list
    defprinter= win32print.GetDefaultPrinter()
    PRCOMBO.set(defprinter)
    PRCOMBO.pack(padx=5, pady=5)
    
    def select():
        global printerdef
        printerdef = PRCOMBO.get()
        pt.destroy()
        print_in_default_printer()

    BUTTON = ttk.Button(pt, text="Print", width=30, command=select).pack(pady=10)

def print_in_default_printer():
    printText = T2.get("1.0", END)
    print(printText)
    print(printerdef)
    
    win32print.SetDefaultPrinter(printerdef)
    filename = tempfile.mktemp(".txt")
    open(filename, "w").write(printText)
    # Bellow is call to print text from T2 textbox
    win32api.ShellExecute(
        0,
        "printto",
        filename,
        '"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )
    showinfo(title='Success', message='Print Successful', detail='Printing is done. Thank you!')

root = Tk()
root.title("Printer Selection in Tkinter")
root.geometry("400x400")

menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Print", command=locprinter)

LAB = Label(root, text="Write Something Here")
T2 = Text(root, width=40, height=10, wrap=WORD)
LAB.pack()
T2.pack(fill=BOTH, padx=5, pady=5)

# # MySQL Database Connection
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Rewamp@15",
#   database="test_server"
# )

# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM user_master")
# result = mycursor.fetchall()

# for row in result:
#     print(row)

root.mainloop()
