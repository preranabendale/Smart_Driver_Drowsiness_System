# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 22:27:30 2025

@author: Lokesh
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 12:56:46 2025

@author: Lokesh
"""

import tkinter 
import tkinter as tk
import sqlite3
import random
from tkinter import messagebox as ms
from PIL import Image,ImageTk

import re
import numpy


root=tk.Tk()
root.configure(background='white')
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))
root.title("REGISTRATION FORM")

image2=Image.open('img1.png')
image2=image2.resize((w,h),Image.LANCZOS)

background_image= ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image
  
background_label.place(x=0,y=0)


#######################################################################################################################################3

Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.IntVar()
age = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()
policeno = tk.IntVar()
value = random.randint(1, 1000)
print(value)

# database code
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
               "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
db.commit()



# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# db = sqlite3.connect('project1.db')
# cursor = db.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS registration"
#                "(Name TEXT, Email TEXT, password TEXT, Address TEXT,Country  TEXT, PhoneNo TEXT)")
# db.commit()



# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 

def insert():
    fname = Fullname.get()
    addr = address.get()
    un = username.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    pwd = password.get()
    cnpwd = password1.get()
    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM admin_registration WHERE username = ?')
    c.execute(find_user, [(username.get())])

    # else:
    #   ms.showinfo('Success!', 'Account Created Successfully !')

    # to check mail
    #regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
    # validation
    if (fname.isdigit() or (fname == "")):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "please enter valid name")
    elif (addr == ""):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter Address")
    elif (email == "") or (a == False):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif ((time > 100) or (time == 0)):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter valid age")
    elif (c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif (pwd == ""):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter valid password")
    elif (var == False):
        ms.showinfo("Message", "Please Enter gender")
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    elif (pwd != cnpwd):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO admin_registration(Fullname, address, username, Email, Phoneno, Gender, age , password) VALUES(?,?,?,?,?,?,?,?)',
                (fname, addr, un, email, mobile, gender, time, pwd))

            conn.commit()
            db.close()
            ms.askquestion("askquestion", "Are you sure?")
            ms.askokcancel("askokcancel", "Want to continue?")
            ms.showinfo('Success!', 'Account Created Successfully !')
            # window.destroy()
            
            from subprocess import call
            call(["python", "log.py"])
            
            
            window.destroy()


            
##################################################################################################################################################
label=tk.Label(root,text="Registeration Form",font=("Forte",30),fg="white",bg="black")
label.place(x=610,y=80)

canvas=tk.Canvas(root,background="black",highlightbackground="red",borderwidth=3)
canvas.place(x=580,y=150,width=400,height=590)



label=tk.Label(root,text="Name:",font=("Calibri",14),
               bg="black",fg="white")
label.place(x=620,y=200)
entry=tk.Entry(root,border=2,textvar=Fullname)
entry.place(x=800,y=205)

label=tk.Label(root,text="Email:",font=("Calibri",14),
              bg="black",fg="white")
label.place(x=620,y=250)
entry=tk.Entry(root,border=2,textvar=Email)
entry.place(x=800,y=255)

label=tk.Label(root,text="Password:",font=("Calibri",14),
             bg="black",fg="white")
label.place(x=620,y=300)
entry=tk.Entry(root,border=2,show="*",textvar=password)
entry.place(x=800,y=305)

label=tk.Label(root,text="Re-Enter Password:",font=("Calibri",14),
            bg="black",fg="white")
label.place(x=620,y=350)
entry=tk.Entry(root,border=2,show="*",textvar=password1)
entry.place(x=800,y=355)

label=tk.Label(root,text="Address:",font=("Calibri",14),
            bg="black",fg="white")
label.place(x=620,y=400)
entry=tk.Entry(root,border=2,textvar=address)
entry.place(x=800,y=405)


label=tk.Label(root,text="Username:",font=("Calibri",14),
           bg="black",fg="white")
label.place(x=620,y=450)
entry=tk.Entry(root,border=2,textvar=username)
entry.place(x=800,y=455)

label=tk.Label(root,text="Phone no:",font=("Calibri",14),
            bg="black",fg="white")
label.place(x=620,y=500)
entry=tk.Entry(root,border=2,textvar=Phoneno)
entry.place(x=800,y=505)

label=tk.Label(root,text="Age:",font=("Calibri",14),
            bg="black",fg="white")
label.place(x=620,y=540)
entry=tk.Entry(root,border=2,textvar=age)
entry.place(x=800,y=545)

a1=tk.Label(root,text="Gender:",font=("Calibri",14),bg="black",fg="white").place(x=620,y=590)
tk.Radiobutton(root,text="Male",font=("Calibri",10),bg="white",value=1,variable=var).place(x=800,y=590)
tk.Radiobutton(root,text="FeMale",font=("Calibri",10),bg="white",value=2,variable=var).place(x=880,y=590)


def reg():
    from subprocess import call
    call(['python','log.py'])
    
btn=tk.Button(root,text="Create Account",font=("Arial"),width=20, command=insert,
              
              bg="#2980b9",
              fg="black",
            )
btn.place(x=700,y=650)



register2=tk.Label(root,text="Already have an account? " ,bg="black",fg="white",font=('Cambria',11)).place(x=720,y=700)


def reg():
    from subprocess import call
    call(['python','log.py'])

button1=tk.Button(root,text="log in",fg='black' ,bg='#1e8449',command=reg)
button1.place(x=900,y=700)

root.mainloop()

