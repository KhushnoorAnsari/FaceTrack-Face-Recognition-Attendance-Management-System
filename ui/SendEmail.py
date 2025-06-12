import smtplib
import ssl
from email.message import EmailMessage
import os
from tkinter import messagebox


# Recommended: Store sensitive info in environment variables for security
EMAIL_SENDER = os.getenv("EMAIL_SENDER", "ansariabutayyab@gmail.com")
EMAIL_PASSWORD = "pquy hclz jfeu zkqp"  # You can set this in your system environment variables
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER", "auroramkktao@gmail.com")

# File paths
csv_file = "attendance_logs/attendance.csv"
excel_file = "attendance_logs/attendance_records.xlsx"
pdf_file = "attendance_logs/attendance_report.pdf"

def send_email_report():
    missing_files = [f for f in [csv_file, excel_file, pdf_file] if not os.path.exists(f)]
    
    if missing_files:
        messagebox.showerror("File Error", f"Missing file(s):\n" + "\n".join(missing_files))
        return

    msg = EmailMessage()
    msg["Subject"] = "Daily Attendance Report"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg.set_content("Dear Admin,\n\nPlease find attached the daily attendance report.\n\nBest regards,\nFaceTrack System")

    # Attach all 3 files
    attachments = [(csv_file, "attendance.csv"), (excel_file, "attendance_records.xlsx"), (pdf_file, "attendance_report.pdf")]
    
    for file_path, file_name in attachments:
        try:
            with open(file_path, "rb") as f:
                msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=file_name)
        except Exception as e:
            messagebox.showerror("Attachment Error", f"Failed to attach {file_name}.\n{e}")
            return

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        messagebox.showinfo("Success", "📧 Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Authentication Error", "Failed to login. Please check your email and password.")
    except Exception as e:
        messagebox.showerror("Email Error", f"Failed to send email.\n{e}")

def send_email_report():
    print("Checking file existence...")
    missing_files = [f for f in [csv_file, excel_file, pdf_file] if not os.path.exists(f)]
    
    if missing_files:
        print("Missing files:", missing_files)
        messagebox.showerror("File Error", f"Missing file(s):\n" + "\n".join(missing_files))
        return

    print("Building email...")
    msg = EmailMessage()
    msg["Subject"] = "Daily Attendance Report"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg.set_content("Dear Admin,\n\nPlease find attached the daily attendance report.\n\nBest regards,\nFaceTrack System")

    print("Attaching files...")
    attachments = [(csv_file, "attendance.csv"), (excel_file, "attendance_records.xlsx"), (pdf_file, "attendance_report.pdf")]
    
    for file_path, file_name in attachments:
        try:
            with open(file_path, "rb") as f:
                msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=file_name)
        except Exception as e:
            print(f"Attachment error: {file_name}, {e}")
            messagebox.showerror("Attachment Error", f"Failed to attach {file_name}.\n{e}")
            return

    try:
        print("Connecting to Gmail SMTP...")
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            print("Sending email...")
            server.send_message(msg)
        print("Email sent successfully.")
        messagebox.showinfo("Success", "📧 Email sent successfully!")
    except smtplib.SMTPAuthenticationError as e:
        print("Authentication error:", e)
        messagebox.showerror("Authentication Error", "Failed to login. Please check your email and password.")
    except Exception as e:
        print("General error:", e)
        messagebox.showerror("Email Error", f"Failed to send email.\n{e}")


if __name__ == "__main__":
    send_email_report()
