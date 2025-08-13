import tkinter as tk 
import tkinter
import sqlite3
import random
from tkinter import messagebox as ms
from PIL import Image,ImageTk
from tkinter.ttk import *

root=tk.Tk()
root.configure(background='white')

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))
root.title("login")

image2=Image.open('img1.jpg')
image2=image2.resize((w,h),Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root,image=background_image)
background_label.image = background_image
background_label.place(x=0,y=0)

#############################################################################################################


Email = tk.StringVar()
password = tk.StringVar() 
def registration():
    from subprocess import call
    call(["python","registration 2.py"])
    root.destroy()\
 
# def registration():
#     from subprocess import call
#     call(["python","GUI_master.py"])
#     root.destroy()

def login():
        # Establish Connection

    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
                        "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
         db.commit()

         find_entry = ('SELECT * FROM admin_registration WHERE Email = ? and password = ?')
         c.execute(find_entry, [(Email.get()), (password.get())])
         result = c.fetchall()
        
         if result:
            msg = ""
            # self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n Loged In'
            # msg = self.head['text']
            #            self.head['pady'] = 150
            print(msg)
            ms.showinfo("messege", "Login sucessfully")
            # ===========================================
            root.destroy()
            from subprocess import call
            call(['python','registration.py'])


            

            # ================================================
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')



a11=tk. Label(root,text='Login Here ',fg='white',bg ='black',font=('Forte',25)).place(x=700,y=50)

canvas1=tk.Canvas(root,background="gray",highlightbackground="red")
canvas1.place(x=560,y=100,width=450,height=250)

#login=Label(root,text="Login",font=('Arial',25),foreground='green').place(x=270,y=350)
a11=tk. Label(root,text='Enter Email',bg='black',fg="white",font=('Cambria',15)).place(x=600,y=130)
a12=tk. Label(root,text='Enter Password',bg='black',fg="white",font=('Cambria',15)).place(x=600,y=180)

b11=tk.Entry(root,width=40, textvariable=Email).place(x=750,y=130,)
b12=tk. Entry(root,width=40,show='*', textvariable=password).place(x=750,y=180,)


# def forgot():
#     from subprocess import call
#     call(['python','movie forgot password.py'])


# button2=tk.Button(root,text="Forgot Password?",fg='black',bg='#27ae60',command=forgot)
# button2.place(x=850,y=430)



button2=tk.Button(root,text="Log in",font=("Bold",9),command=login,width=50,bg='#2980b9')
button2.place(x=610,y=250)

a=tk. Label(root,text='Not a Member?',font=('Cambria',11),bg='black',fg="white").place(x=800,y=300)

def reg():
    from subprocess import call
    call(['python','registration 2.py'])

button1=tk.Button(root,text="sign up",fg='black',bg='#27ae60',command=reg)
button1.place(x=915,y=300,width=55)



root.mainloop()