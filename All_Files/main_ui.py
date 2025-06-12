import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import subprocess
import urllib.request
import io
import os
import platform

# Predefined admin passwords
admin_credentials = {
    "A": "1234@5",
    "B": "3456@7",
    "C": "5678@9"
}

# Global variable for background image
bg_image = None

# Load background image from URL
def load_background(url):
    try:
        image_bytes = urllib.request.urlopen(url).read()
        image = Image.open(io.BytesIO(image_bytes))
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print("Error loading background image:", e)
        return None

def start_recognition():
    subprocess.run(["python", "recognize.py"])

def capture_faces():
    try:
        subprocess.run(["python", "face_capture.py"], check=True)
        messagebox.showinfo("Success", "Face capture completed. Training model now...")
        subprocess.run(["python", "train_model.py"], check=True)
        messagebox.showinfo("Success", "Model training completed successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

def open_attendance_log():
    try:
        subprocess.run(["python", "CSVtoXLS.py"], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to convert CSV to Excel.\n{e}")
        return

    file_path = os.path.join(os.path.dirname(__file__), "attendance_logs", "attendance_records.xlsx")

    if os.path.exists(file_path):
        try:
            if platform.system() == "Windows":
                os.startfile(file_path)
            elif platform.system() == "Darwin":
                subprocess.call(["open", file_path])
            else:
                subprocess.call(["xdg-open", file_path])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open the file:\n{e}")
    else:
        messagebox.showerror("File Not Found", f"The file '{file_path}' does not exist.")

def open_attendance_report():
    try:
        subprocess.run(["python", "CSVtoPDF.py"], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to convert CSV to PDF.\n{e}")
        return

    file_path = os.path.join(os.path.dirname(__file__), "attendance_logs", "attendance_report.pdf")

    if os.path.exists(file_path):
        try:
            if platform.system() == "Windows":
                os.startfile(file_path)
            elif platform.system() == "Darwin":
                subprocess.call(["open", file_path])
            else:
                subprocess.call(["xdg-open", file_path])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open the file:\n{e}")
    else:
        messagebox.showerror("File Not Found", f"The file '{file_path}' does not exist.")

def send_email():
    subprocess.run(["python", "SendEmail.py"])

def send_notifications():
    subprocess.run(["python", "Notifications_student.py"])
    
def show_admin_panel():
    """Prompt for name and password before showing admin options"""
    root.lift()  # Bring window to front
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)

    name = simpledialog.askstring("Authentication", "Enter your Name :", parent=root)
    if name is None:  # User clicked Cancel
        return

    if name not in admin_credentials:
        messagebox.showerror("Access Denied", "Invalid Name.")
        return

    password = simpledialog.askstring("Authentication", f"Enter password for {name}:", show="*", parent=root)
    if password is None:  # User clicked Cancel
        return

    if password != admin_credentials[name]:
        messagebox.showerror("Access Denied", "Incorrect password.")
        return

    # Now clear and set background only after authentication
    clear_window()
    set_background()

    # If correct password, show admin panel
    tk.Label(root, text="Admin Panel", font=("Arial", 28, "bold")).place(relx=0.5, rely=0.2, anchor="center")

    tk.Button(root, text="Capture Faces", command=capture_faces, width=20, height=2).place(relx=0.5, rely=0.37, anchor="center")
    tk.Button(root, text="Attendance Log", command=open_attendance_log, width=20, height=2).place(relx=0.5, rely=0.44, anchor="center")
    tk.Button(root, text="Attendance Report", command=open_attendance_report, width=20, height=2).place(relx=0.5, rely=0.51, anchor="center")
    tk.Button(root, text="Send Email", command=send_email, width=20, height=2).place(relx=0.5, rely=0.58, anchor="center")
    tk.Button(root, text="Send Notifications", command=send_notifications, width=20, height=2).place(relx=0.5, rely=0.65, anchor="center")
    tk.Button(root, text="Back", command=show_role_selection, width=20, height=2).place(relx=0.5, rely=0.72, anchor="center")

def show_student_panel():
    clear_window()
    set_background()
    tk.Label(root, text="Student Panel", font=("Arial", 28, "bold")).place(relx=0.5, rely=0.3, anchor="center")
    tk.Button(root, text="Recognize Me", command=start_recognition, width=20, height=2).place(relx=0.5, rely=0.4, anchor="center")
    tk.Button(root, text="Back", command=show_role_selection, width=20, height=2).place(relx=0.5, rely=0.5, anchor="center")

def show_role_selection():
    clear_window()
    set_background()
    tk.Label(root, text="FaceTrack", font=("Arial", 34, "bold"), fg="black").place(relx=0.5, rely=0.3, anchor="center")
    tk.Button(root, text="Admin", command=show_admin_panel, width=20, height=2).place(relx=0.5, rely=0.4, anchor="center")
    tk.Button(root, text="Student", command=show_student_panel, width=20, height=2).place(relx=0.5, rely=0.5, anchor="center")

def set_background():
    global bg_image
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def close_app():
    root.destroy()

# Create main window
root = tk.Tk()
root.title("Facial Recognition Attendance System")
root.geometry("1024x600")
root.state("zoomed")

frame_top = tk.Frame(root, bg="#222222")
frame_top.pack(fill="x")

btn_close = tk.Button(frame_top, text="❌", command=close_app, bg="#ff4d4d", fg="white", border=0)
btn_close.pack(side="right", padx=5, pady=2)

btn_maximize = tk.Button(frame_top, text="🔳", command=lambda: root.state("zoomed"), bg="#cccccc", fg="black", border=0)
btn_maximize.pack(side="right", padx=5, pady=2)

btn_minimize = tk.Button(frame_top, text="➖", command=lambda: root.iconify(), bg="#cccccc", fg="black", border=0)
btn_minimize.pack(side="right", padx=5, pady=2)

# Load background image
bg_image_url = "https://justtotaltech.com/wp-content/uploads/2021/07/X-Best-facial-recognition-software-to-explore-in-2021.jpg"
bg_image = load_background(bg_image_url)

# Start with role selection screen
show_role_selection()

# Start the main loop
root.mainloop()
