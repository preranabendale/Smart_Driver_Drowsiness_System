# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:27:05 2021
@author: om
"""

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time

global fn
fn = ""

# ======================== Root Window Setup ============================
root = tk.Tk()
root.configure(background="#520052")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Smart Driver Drowsiness System ")

# ======================== Background Video Setup ============================
video_path = "v1.mp4"  # Replace with your video file
cap = cv2.VideoCapture(video_path)

def update_background():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (1600, 900))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        background_label.imgtk = imgtk
        background_label.configure(image=imgtk)
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart video
    background_label.after(33, update_background)

background_label = tk.Label(root)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
update_background()

# ======================== Title Label ============================
label_l1 = tk.Label(root, text="Smart Driver Drowsiness System ",
                    font=("Copperplate Gothic Bold", 30),
                    background="sky blue", fg="black", width=55, height=2)
label_l1.place(x=0, y=0)

# ======================== Marquee Animation ============================


# ======================== Functions ============================
def reg():
    from subprocess import call
    call(["python", "registration 2.py"])

def log():
    from subprocess import call
    call(["python", "log.py"])

def window():
    root.destroy()

# ======================== Buttons ============================
button_register = tk.Button(root, text="Register", command=reg, width=15, height=2,
                            font=('times', 12, 'bold'), bg="sky blue", fg="black")
button_register.place(x=50, y=150)

button_login = tk.Button(root, text="Login", command=log, width=15, height=2,
                         font=('times', 12, 'bold'), bg="sky blue", fg="black")
button_login.place(x=50, y=220)

button_exit = tk.Button(root, text="Exit", command=window, width=15, height=2,
                        font=('times', 12, 'bold'), bg="sky blue", fg="black")
button_exit.place(x=50, y=290)

# ======================== Start GUI ============================
root.mainloop()
