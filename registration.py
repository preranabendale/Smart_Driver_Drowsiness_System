from tkinter import *
import sqlite3
import tkinter as tk
from tkinter import messagebox as ms
from PIL import Image, ImageTk

# --- Tkinter window setup ---
root = Tk()
root.geometry('700x600')
root.title("Registration Form")

# --- Background Image ---
try:
    image2 = Image.open('m.jpg')  # Replace 'm.jpg' with your background image path
    image2 = image2.resize((700, 700), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(image2)
    background_label = tk.Label(root, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0)
except Exception as e:
    print("Background image not found or error loading:", e)

# --- Tkinter variables ---
Name = StringVar()
LastName = StringVar()
Address = StringVar()
Mobile = StringVar()

# --- Create DB and Table if not exist ---
def create_table():
    conn = sqlite3.connect('face.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Lastname TEXT,
            Address TEXT,
            Mobileno TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_table()

# --- Save data ---
def database():
    name = Name.get()
    lastname = LastName.get()
    address = Address.get()
    mobileno = Mobile.get()

    if (name.isdigit() or name == ""):
        ms.showinfo("Message", "Please enter a valid Name")
    elif (lastname.isdigit() or lastname == ""):
        ms.showinfo("Message", "Please enter a valid Last Name")
    elif address == "":
        ms.showinfo("Message", "Please enter a valid Address")
    elif len(mobileno) != 10 or not mobileno.isdigit():
        ms.showinfo("Message", "Please enter a valid 10-digit Mobile Number")
    else:
        try:
            conn = sqlite3.connect('face.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO User (Name, Lastname, Address, Mobileno) VALUES (?, ?, ?, ?)',
                           (name, lastname, address, mobileno))
            conn.commit()
            conn.close()
            ms.showinfo('Success', 'User Registered Successfully!')
            # Redirect to GUI_master.py after registration
            root.destroy()  # Close the current window
            from subprocess import call
            call(["python", "GUI_master.py"])  # Launch GUI_master.py after registration
        except Exception as e:
            ms.showerror("Database Error", str(e))

# --- Display Button Function ---
def display():
    from subprocess import call
    call(["python", "display.py"])

# --- UI Elements ---
label_0 = Label(root, text="Registration Form", width=25, font=("bold", 22), fg="#FF8040", bg="black")
label_0.place(x=150, y=50)

label_1 = Label(root, text="Name", width=25, font=("bold", 10))
label_1.place(x=150, y=130)
entry_1 = Entry(root, textvar=Name, width=25, font=("bold", 10))
entry_1.place(x=380, y=130)

label_2 = Label(root, text="Last Name", width=25, font=("bold", 10))
label_2.place(x=150, y=180)
entry_2 = Entry(root, textvar=LastName, width=25, font=("bold", 10))
entry_2.place(x=380, y=180)

label_3 = Label(root, text="Address", width=25, font=("bold", 10))
label_3.place(x=150, y=230)
entry_3 = Entry(root, textvar=Address, width=25, font=("bold", 10))
entry_3.place(x=380, y=230)

label_5 = Label(root, text="Mobile No", width=25, font=("bold", 10))
label_5.place(x=150, y=280)
entry_5 = Entry(root, textvar=Mobile, width=25, font=("bold", 10))
entry_5.place(x=380, y=280)

Button(root, text='Submit', width=25, bg='red', fg='white', command=database).place(x=150, y=330)
Button(root, text='Display', width=25, bg='red', fg='white', command=display).place(x=375, y=330)

root.mainloop()
