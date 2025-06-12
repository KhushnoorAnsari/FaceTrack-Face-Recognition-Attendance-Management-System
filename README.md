# 📌 FaceTrack – Facial Recognition Attendance Management System

A smart, contactless attendance management system developed using **Python**, combining **OpenCV**, **face_recognition**, **Tkinter**, and **SQLite** to mark attendance automatically through facial recognition.

---

## 📖 Table of Contents

## 📖 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Working](#working)
- [Future Enhancements](#future-enhancements)
- [Acknowledgments](#acknowledgments)

---

## Features

✅ Face capture and registration  
✅ LBPH-based face recognition  
✅ Real-time webcam feed processing  
✅ GUI for Admin and Student using Tkinter  
✅ Automated attendance marking with date and time  
✅ CSV, PDF, and Excel report generation  
✅ Email and notification support (SMTP, Twilio)  
✅ Secure admin panel with password protection

---

## Tech Stack

- **Language**: Python 3.10+
- **Libraries**:
  - OpenCV
  - face_recognition (built on dlib)
  - Pandas, NumPy
  - Tkinter
  - smtplib, Twilio, PIL
  - fpdf, pickle, os, datetime
- **Database**: SQLite (local) + CSV files
- **IDE Used**: VS Code, Jupyter Notebook (prototyping)

---

## Project Structure

│── ui/ # Stores registered face images
│ ├── face_capture.py # Captures face images & saves them in dataset/
│ ├── train_model.py # Trains model using collected images
│ ├── recognize.py # Recognizes faces & marks attendance
│ ├── main_ui.py # Main interface for the application
│ ├── attendance_logs/ # Stores attendance records
│ ├── attendance.csv # CSV file for attendance logs
├── attendance.xlsx # Excel file for attendance logs
├── attendance.pdf #Pdf file for attendance logs
│ ├── dataset/ # Stores face images of students/employees
│ ├── person1/ # Folder for each person (e.g., "John_Doe")
│ │ ├── 1.jpg # Face images of the person
│ │ ├── 2.jpg
│ │ ├── ...
│ ├── person2/
│ │ ├── 1.jpg
│ │ ├── 2.jpg
│ │ ├── ...
│ │── trained_model/ # Stores trained facial encodings
│ │ ├── face_encodings.pkl # Pickle file for storing face encodings
│── init_attendance # To initialize the "attendence.csv file"
│── main.py # Main application script
│── requirements.txt # Dependencies list
│── README.md # Project documentation

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/KhushnoorAnsari/FaceTrack-Facial-Recognition-Attendance-Management-System.git
   cd FaceTrack
   ```

2. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

---

## Usage

🧑‍💻 Register Faces: Run face_capture.py to store facial images.

🧠 Train Model: Run train_model.py to encode and store faces.

🚀 Start System: Run main.py to launch the GUI.

🎯 Mark Attendance: Use “Recognize Me” in the Student Panel.

📁 View Logs: Attendance is stored in attendance_logs/.

---

## Working

📸 Captures faces → 🧠 Trains LBPH model

🎥 Real-time recognition through webcam

📝 Logs attendance automatically with timestamps

📧 Optional: Sends email/SMS alerts to users

---

## Future Enhancements

☁️ Cloud integration for multi-branch deployment

📱 Mobile App with Flutter/Kivy

🛡️ Spoof detection (anti-fraud measures)

🔐 Integration with biometric door lock systems

📊 Attendance analytics dashboard

---

## Acknowledgments

Special thanks to the Open Source Community for libraries like OpenCV, dlib, and face_recognition.

📚 Developed as part of an academic project by a team of two passionate developers:

####👩‍💻 Khushnoor

## ####👨‍💻 Suryansh Saini
