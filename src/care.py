import tkinter as tk
from PIL import Image, ImageTk

def open_safety_tips_window():
    # Create the tips window
    tips_win = tk.Toplevel(root)
    tips_win.title("Driver Safety Guidelines")
    
    # Get screen width and height for full screen
    w, h = tips_win.winfo_screenwidth(), tips_win.winfo_screenheight()
    tips_win.geometry(f"{w}x{h}+0+0")  # Full screen window
    tips_win.resizable(False, False)

    # Set background image for safety tips window
    bg_img = Image.open("bg9.jpg")
    bg_img = bg_img.resize((w, h))  # Resize to screen size
    bg_photo = ImageTk.PhotoImage(bg_img)

    bg_label = tk.Label(tips_win, image=bg_photo)
    bg_label.image = bg_photo  # Keep a reference
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Title of the tips page
    title = tk.Label(tips_win, text="🚗 Driver Safety Guidelines", font=("Arial", 20, "bold"), fg="#003366", bg="light gray")
    title.pack(pady=5)

    care_tips = [
        "✅ Always wear a seatbelt.",
        "✅ Take breaks every 2 hours on long drives.",
        "✅ Avoid using mobile phones while driving.",
        "✅ Never drive under the influence of alcohol or drugs.",
        "✅ Keep your eyes on the road and hands on the wheel.",
        "✅ Use indicators and follow traffic signals.",
        "✅ Ensure proper sleep before long drives.",
    ]

    consequence_tips = [
        "❌ Skipping breaks can lead to drowsiness and accidents.",
        "❌ Not wearing a seatbelt increases injury risk during crashes.",
        "❌ Distracted driving is a major cause of road accidents.",
        "❌ Driving tired or drunk can result in license suspension or jail.",
        "❌ Ignoring safety can endanger your life and others on road.",
    ]

    frame = tk.Frame(tips_win, bg="light gray", padx=20, pady=20)
    frame.place(relx=0.2, rely=0.6, anchor='center')

    tk.Label(frame, text="Things to take care of while driving:", font=("Arial", 16, "bold"), bg="light gray", fg="green").pack(anchor='w', pady=(10, 5))
    for tip in care_tips:
        tk.Label(frame, text=tip, font=("Arial", 13), bg="light gray", anchor="w").pack(anchor='w', padx=20)

    tk.Label(frame, text="Consequences if not followed:", font=("Arial", 16, "bold"), bg="light gray", fg="red").pack(anchor='w', pady=(20, 5))
    for con in consequence_tips:
        tk.Label(frame, text=con, font=("Arial", 13), bg="light gray", anchor="w").pack(anchor='w', padx=20)

    close_btn = tk.Button(frame, text="Close", font=("Arial", 12), command=tips_win.destroy, bg="#003366", fg="white")
    close_btn.pack(pady=20)

# MAIN WINDOW
root = tk.Tk()
root.title("Driver Drowsiness Detection Project")

# Get screen width and height for full screen
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{w}x{h}+0+0")  # Full screen window
root.resizable(False, False)

# Set background image for main window
bg_img_main = Image.open("bg33.png")
bg_img_main = bg_img_main.resize((w, h))  # Resize to screen size
bg_photo_main = ImageTk.PhotoImage(bg_img_main)

bg_label_main = tk.Label(root, image=bg_photo_main)
bg_label_main.image = bg_photo_main  # Keep a reference
bg_label_main.place(x=0, y=0, relwidth=1, relheight=1)

# Overlay frame for widgets (buttons, etc.)
overlay_frame = tk.Frame(root, bg="#ffffff", bd=2)
overlay_frame.place(relx=0.5, rely=0.4, anchor="center")

# Button to open safety guidelines page
btn = tk.Button(text="Open Safety Guidelines Page", command=open_safety_tips_window,
                font=("Arial", 50), bg="light green", fg="black")
btn.place(x=300, y=650)

root.mainloop()
