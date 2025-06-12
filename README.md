# 📌 FaceTrack – Facial Recognition Attendance Management System

A smart, contactless attendance management system developed using **Python**, combining **OpenCV**, **face_recognition**, **Tkinter**, and **SQLite** to mark attendance automatically through facial recognition.

---

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

│── ui/                          # Stores registered face images<br>
│ ├── face_capture.py            # Captures face images & saves them in dataset/<br>
│ ├── train_model.py            # Trains model using collected images<br>
│ ├── recognize.py              # Recognizes faces & marks attendance<br>
│ ├── main_ui.py                # Main interface for the application<br>
│ ├── attendance_logs/          # Stores attendance records<br>
│ ├── attendance.csv            # CSV file for attendance logs<br>
├── attendance.xlsx             # Excel file for attendance logs<br>
├── attendance.pdf              #Pdf file for attendance logs<br>
│ ├── dataset/                  # Stores face images of students/employees<br>
│ ├── person1/                  # Folder for each person (e.g., "John_Doe")<br>
│ │ ├── 1.jpg                   # Face images of the person<br>
│ │ ├── 2.jpg                     <br>
│ │ ├── ...                          <br>
│ ├── person2/                         <br>
│ │ ├── 1.jpg                        <br>
│ │ ├── 2.jpg                         <br>
│ │ ├── ...                          <br>
│ │── trained_model/             # Stores trained facial encodings<br>
│ │ ├── face_encodings.pkl       # Pickle file for storing face encodings<br>
│── init_attendance              # To initialize the "attendence.csv file"<br>
│── main.py                      # Main application script<br>
│── requirements.txt             # Dependencies list<br>
│── README.md                    # Project documentation<br>

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

## 🙌 Acknowledgments

Special thanks to the Open Source Community for libraries like OpenCV, dlib, and face_recognition.

📚 Developed as part of an academic project by a team of two passionate developers:

- 👩‍💻 [Khushnoor](https://github.com/KhushnoorAnsari/KhushnoorAnsari)  
- 👨‍💻 [Suryansh Saini](#)  <!-- Replace with actual username if different -->

