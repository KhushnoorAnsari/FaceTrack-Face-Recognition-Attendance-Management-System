import os
import pandas as pd

attendance_file = "attendance_logs/attendance.csv"

# Ensure the folder exists
os.makedirs(os.path.dirname(attendance_file), exist_ok=True)

# Create CSV with required columns if it doesn't exist
if not os.path.exists(attendance_file):
    df = pd.DataFrame(columns=["Name", "Date", "Time", "Status"])
    df.to_csv(attendance_file, index=False)
    print("✅ attendance.csv created successfully with columns: Name, Date, Time, Status")
else:
    print("ℹ️ attendance.csv already exists!")
