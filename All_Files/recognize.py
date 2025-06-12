import cv2
import face_recognition
import pickle
import pandas as pd
from datetime import datetime, time as dt_time
import time
import os

# Load trained encodings
with open("trained_model/face_encodings.pkl", "rb") as f:
    known_encodings = pickle.load(f)

known_names = list(known_encodings.keys())
recognized_names = set()

# Create attendance directory if not exists
attendance_file = "attendance_logs/attendance.csv"
os.makedirs(os.path.dirname(attendance_file), exist_ok=True)

# Start webcam
cap = cv2.VideoCapture(0)

# Warm-up camera
for _ in range(3):
    ret, _ = cap.read()
    if not ret:
        print("Error: Could not access the camera.")
        cap.release()
        cv2.destroyAllWindows()
        exit()

start_time = time.time()
cv2.namedWindow("Face Recognition", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Face Recognition", cv2.WND_PROP_TOPMOST, 1)

today = datetime.now().strftime('%Y-%m-%d')

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame from camera.")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    message = ""  # Message to display on screen

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(list(known_encodings.values()), face_encoding)
        name = "Unknown"

        if True in matches:
            match_idx = matches.index(True)
            name = known_names[match_idx]

            if name not in recognized_names:
                recognized_names.add(name)
                timestamp = datetime.now().strftime('%H:%M:%S')
                df = pd.DataFrame([[name, today, timestamp, "Present"]],
                                  columns=["Name", "Date", "Time", "Status"])
                df.to_csv(attendance_file, mode='a', header=not os.path.exists(attendance_file), index=False)
                message = f"Welcome, {name}. Your attendance has been recorded."
                print(message)
        else:
            message = "Face not recognized. Please try again or contact the administrator."
            print(message)

        # Draw rectangle and name
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Show message at bottom of the screen
    if message:
        cv2.putText(frame, message, (10, frame.shape[0] - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    cv2.imshow("Face Recognition", frame)

    if time.time() - start_time >= 10:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup camera
cap.release()
cv2.destroyAllWindows()

# Mark absentees after 1 PM
now = datetime.now()
if now.time() >= dt_time(13, 0):  # After 1 PM
    if os.path.exists(attendance_file):
        attendance_df = pd.read_csv(attendance_file)
    else:
        attendance_df = pd.DataFrame(columns=["Name", "Date", "Time", "Status"])

    already_marked = attendance_df[attendance_df["Date"] == today]["Name"].tolist()
    absent_names = [name for name in known_names if name not in already_marked]

    absent_entries = pd.DataFrame([[name, today, "", "Absent"] for name in absent_names],
                                  columns=["Name", "Date", "Time", "Status"])

    if not absent_entries.empty:
        absent_entries.to_csv(attendance_file, mode='a', header=False, index=False)
        print("✅ Absent entries added after 1 PM.")
    else:
        print("ℹ️ All students already marked present before 1 PM.")
