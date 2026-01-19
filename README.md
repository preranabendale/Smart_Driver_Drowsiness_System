#  Smart Driver Drowsiness System

##  Project Overview
The Smart Driver Drowsiness System is a real-time computer vision based safety application
that continuously monitors the driver’s face to detect drowsiness and yawning using a live camera feed.

When fatigue is detected, the system immediately triggers a buzzer alert
and sends an email with the driver’s live location to emergency contacts,
helping to prevent road accidents caused by driver sleepiness.



## Problem Statement
Driver fatigue is one of the major causes of road accidents worldwide.
Long driving hours can lead to loss of concentration, yawning, and sleep,
which increases the risk of accidents.

This project aims to improve road safety by continuously monitoring the driver
and providing instant alerts and notifications when drowsiness is detected.



##  Solution
The system captures real-time video using a webcam and analyzes the driver’s facial features.
Eye closure duration and mouth movements are monitored to detect drowsiness and yawning.

If the driver’s eyes remain closed for a specific time or yawning is detected:
- A buzzer alert is activated to wake the driver
- An email alert with the driver’s live location is sent to predefined contacts



##  Key Features
- Continuous real-time driver face monitoring
- Eye closure based drowsiness detection
- Yawning detection using facial landmarks
- Buzzer alert system for immediate warning
- Email alert with live location sharing
- Simple and user-friendly GUI using Tkinter



##  Technologies Used
- Python
- OpenCV
- Dlib
- Tkinter
- Imutils
- SMTP (for email alerts)
- GPS / Location API (for live location)


##  Project Structure

Smart_Driver_Drowsiness_System/
│
├── GUI_main.py              # Main GUI file to start the application
├── master.py                # Controls overall project workflow and logic
├── register.py              # Handles user registration and email setup
├── Drowsiness_Detection1.py  # Face & drowsiness detection logic
├── alarm.wav                 # Buzzer alert sound
├── shape_predictor.dat        # Facial landmark detection model
└── README.md                  # Project documentation


##  How to Run the Project
1. Clone the repository  
   git clone https://github.com/preranabendale/Smart_Driver_Drowsiness_System.git

2. Install required libraries  
   pip install opencv-python dlib imutils

3. Run the application  
   python GUI_main.py



## Applications
- Driver safety and monitoring systems
- Accident prevention systems
- Smart vehicle safety solutions
- Real-time computer vision applications

## Author
Prerana Bendale  

