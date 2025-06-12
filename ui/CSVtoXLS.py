import pandas as pd
import os
import smtplib  # No need to install
import ssl

csv_file = "attendance_logs/attendance.csv"  # Updated path
excel_file = "attendance_logs/attendance_records.xlsx"  # Save Excel in the same folder

def convert_csv_to_excel():
    if not os.path.exists(csv_file):
        print("Error: CSV file not found in attendance_logs folder!")
        return
    
    try:
        df = pd.read_csv(csv_file, encoding="utf-8")  # Read CSV
        df.to_excel(excel_file, index=False)  # Save as Excel
        print(f"CSV converted to Excel successfully! Saved at: {excel_file}")
    except Exception as e:
        print(f"Error: {e}")

# Example Usage
convert_csv_to_excel() 