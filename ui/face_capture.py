import cv2
import os
import csv
import tkinter as tk
from tkinter import messagebox

# CSV path to store name-email pairs
csv_file = "student_emails.csv"
header = ["Name", "Email"]

def save_details():
    name = name_entry.get().strip()
    email = email_entry.get().strip()

    if not name or not email:
        messagebox.showwarning("Input Error", "Please enter both name and email.")
        return

    # Save to CSV
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(header)
        writer.writerow([name, email])

    # Create directory to store images
    save_path = f"dataset/{name}/"
    os.makedirs(save_path, exist_ok=True)

    messagebox.showinfo("Success", f"Registered {name}. Starting face capture...")

    # Start webcam and capture 50 images
    cap = cv2.VideoCapture(0)
    count = 0
    while count < 50:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Capturing Faces", frame)
        cv2.imwrite(f"{save_path}/{count}.jpg", frame)
        count += 1
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    messagebox.showinfo("Done", "Face capture complete.")
    root.destroy()

# Create UI
root = tk.Tk()
root.title("Student Registration")

tk.Label(root, text="Enter Student Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Enter Student Email:").grid(row=1, column=0, padx=10, pady=10)
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=1, column=1)

submit_button = tk.Button(root, text="Register & Capture", command=save_details)
submit_button.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
