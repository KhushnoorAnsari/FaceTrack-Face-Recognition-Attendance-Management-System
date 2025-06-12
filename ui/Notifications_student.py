import os
import pandas as pd
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv

# 📧 Your email and app password
EMAIL_ADDRESS = "ansariabutayyab@gmail.com"
EMAIL_PASSWORD = "pquy hclz jfeu zkqp"  # App Password, not your Gmail password

# Paths
dataset_path = "dataset"
csv_file = "attendance_logs/attendance.csv"
email_data_file = "student_emails.csv"

# Load student name-email map
def load_student_emails():
    student_emails = {}
    if os.path.exists(email_data_file):
        with open(email_data_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["Name"].strip()
                email = row["Email"].strip()
                student_emails[name] = email
    return student_emails

# Get registered students from folders
def get_registered_students():
    return [name for name in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, name))]

# Get today's attendance from CSV
def get_today_attendance():
    if not os.path.exists(csv_file):
        return []

    df = pd.read_csv(csv_file)
    today = datetime.now().strftime("%Y-%m-%d")

    if "Date" not in df.columns or "Name" not in df.columns:
        print("⚠️ CSV missing required columns")
        return []

    today_records = df[df["Date"] == today]
    return today_records["Name"].tolist()

# Send email notification
def send_email(to_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"📧 Email sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email to {to_email}: {e}")

# Notify absentees
def notify_absent_students():
    now = datetime.now()
    if now.hour < 12:
        print("⏰ It's not 12 PM yet. Notifications will be sent after 12.")
        return

    registered = set(get_registered_students())
    present = set(get_today_attendance())
    absentees = registered - present

    student_emails = load_student_emails()

    for student in absentees:
        email = student_emails.get(student)
        if email:
            send_email(email, "Absence Alert", f"Dear {student}, you are marked absent today.")
        else:
            print(f"⚠️ No email found for {student}")

# Run the script
notify_absent_students()
