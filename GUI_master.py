from tkinter import *
import tkinter as tk
from tkinter import ttk, LEFT, END
import time
import numpy as np
import cv2
import os
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox as ms
import smtplib
from subprocess import call
from email.message import EmailMessage
import imghdr  # Needed for email image attachment

root = tk.Tk()
root.configure(background="#2874a6")

# SQLite database connection
my_conn = sqlite3.connect('face.db')

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Face Attendance System")

# Background image
image2 = Image.open('bg4.jpg')
image2 = image2.resize((w, h), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

# Frame for buttons
frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=280, height=500, bd=5, font=('times', 15, ' bold '), bg="seashell4")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=5, y=140)

# Function to create the face data
def Create_database():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    if face_cascade.empty():
        ms.showerror("Error", "Failed to load Haar cascade XML file.")
        return

    cap = cv2.VideoCapture(0)
    id = entry2.get()
    sampleN = 0

    while True:
        ret, img = cap.read()
        if not ret:
            ms.showerror("Error", "Failed to read from camera.")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            sampleN += 1
            os.makedirs("facesData", exist_ok=True)
            cv2.imwrite(f"facesData/User.{id}.{sampleN}.jpg", gray[y:y + h, x:x + w])
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.waitKey(100)

        cv2.imshow('img', img)
        cv2.waitKey(1)

        if sampleN >= 40:
            break

    cap.release()
    cv2.destroyAllWindows()
    entry2.delete(0, 'end')
    ms.showinfo("Success", f"Face data for ID {id} saved successfully.")

# Function to send email with image attachment
def mail():
    Sender_Email = "pragati.code@gmail.com"
    Reciever_Email = "prerana.sct@gmail.com"
    Password = 'ymtp edak ytds hgvk'
    newMessage = EmailMessage()
    newMessage['Subject'] = "Unauthenticated person"
    newMessage['From'] = Sender_Email
    newMessage['To'] = Reciever_Email

    try:
        with open('abc.png', 'rb') as f:
            image_data = f.read()
            image_type = imghdr.what(f.name)
            image_name = f.name
        newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(Sender_Email, Password)
            smtp.send_message(newMessage)
        ms.showinfo("Success", "Mail sent successfully!")

    except smtplib.SMTPAuthenticationError:
        ms.showerror("Authentication Error", "Username and Password not accepted.\nCheck your credentials or use an App Password.")
    except FileNotFoundError:
        ms.showerror("File Error", "Attachment image not found (abc.png).")
    except Exception as e:
        ms.showerror("Error", f"An unexpected error occurred:\n{str(e)}")

# Function to train the database
def Train_database():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    path = "facesData"

    def getImagesWithID(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faces = []
        IDs = []
        for imagePath in imagePaths:
            facesImg = Image.open(imagePath).convert('L')
            faceNP = np.array(facesImg, 'uint8')
            ID = int(os.path.split(imagePath)[-1].split(".")[1])
            faces.append(faceNP)
            IDs.append(ID)
            cv2.imshow("Adding faces for training", faceNP)
            cv2.waitKey(10)
        return np.array(IDs), faces

    Ids, faces = getImagesWithID(path)
    recognizer.train(faces, Ids)
    recognizer.save("trainingdata.yml")
    cv2.destroyAllWindows()

# ✅ Updated function with stricter recognition threshold
def Test_database():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainingdata.yml')

    cascadePath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    if faceCascade.empty():
        ms.showerror("Error", "Failed to load Haar cascade XML file.")
        return

    font = cv2.FONT_HERSHEY_SIMPLEX
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, img = cam.read()
        if not ret:
            ms.showerror("Error", "Failed to read from camera.")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5, minSize=(int(minW), int(minH)))

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            confidence_text = "  {0}%".format(round(100 - confidence))

            print(f"Predicted ID: {id}, Confidence: {confidence}")

            if confidence < 50:
                with sqlite3.connect('face.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM User WHERE id=?", (id,))
                    person_data = cursor.fetchone()
                if person_data:
                    ms.showinfo("Message", f"Person {person_data[1]} Authenticated!")
                    cam.release()
                    cv2.destroyAllWindows()
                    call(["python", "care.py"])
                    call(["python", "Drowsiness_Detection1.py"])
                    return
                else:
                    id = "Unknown"
                    cv2.imwrite('abc.png', img)
                    mail()
            else:
                id = "Unknown"
                cv2.imwrite('abc.png', img)
                mail()

            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, confidence_text, (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imshow('Camera Feed', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

# Display user data from DB
def ID():
    framed = tk.LabelFrame(root, text=" --WELCOME-- ", width=600, height=50, bd=5, font=('times', 14, ' bold '), bg="pink")
    framed.grid(row=0, column=0, sticky='nw')
    framed.place(x=500, y=200)
    my_conn = sqlite3.connect('face.db')
    r_set = my_conn.execute("SELECT * FROM User")
    i = 0
    for student in r_set:
        for j in range(len(student)):
            e = tk.Entry(framed, width=15, fg='blue') 
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i += 1

# Open registration script
def reg():
    call(["python", "Drowsiness_Detection1.py"])

# Exit
def window():
    root.destroy()

# GUI Buttons
button1 = tk.Button(frame_alpr, text="Registration", command=reg, width=20, height=1, font=('times', 15, ' bold '), bg="black", fg="white")
button1.place(x=10, y=40)

button1 = tk.Button(frame_alpr, text="Create Face Data", command=Create_database, width=15, height=1, font=('times', 15, ' bold '), bg="black", fg="white")
button1.place(x=10, y=100)

button2 = tk.Button(frame_alpr, text="Train Face Data", command=Train_database, width=20, height=1, font=('times', 15, ' bold '), bg="black", fg="white")
button2.place(x=10, y=160)

button4 = tk.Button(frame_alpr, text="Data Display", command=ID, width=20, height=1, font=('times', 15, ' bold '), bg="black", fg="white")
button4.place(x=10, y=220)

button3 = tk.Button(frame_alpr, text="Face authentication", bd=5, command=Test_database, width=20, height=1, font=('times', 15, ' bold '), bg="black", fg="white")
button3.place(x=10, y=280)

exit = tk.Button(frame_alpr, text="Exit", command=window, width=20, height=1, font=('times', 15, ' bold '), bg="red", fg="white")
exit.place(x=10, y=340)

entry2 = tk.Entry(frame_alpr, bd=2, width=7)
entry2.place(x=210, y=110)

root.mainloop()
