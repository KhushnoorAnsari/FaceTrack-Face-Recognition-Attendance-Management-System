import pandas as pd
from fpdf import FPDF

csv_file = "attendance_logs/attendance.csv"  # Update the path if needed
pdf_file = "attendance_logs/attendance_report.pdf"

def convert_csv_to_pdf():
    try:
        df = pd.read_csv(csv_file)  # ✅ Ensure Pandas is imported
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add a title
        pdf.cell(200, 10, "Attendance Report", ln=True, align="C")
        pdf.ln(10)

        # Add table headers
        for col in df.columns:
            pdf.cell(40, 10, col, border=1)
        pdf.ln()

        # Add table rows
        for _, row in df.iterrows():
            for item in row:
                pdf.cell(40, 10, str(item), border=1)
            pdf.ln()

        pdf.output(pdf_file)
        print(f"PDF generated successfully: {pdf_file}")

    except Exception as e:
        print(f"Error: {e}")

# Example Usage
convert_csv_to_pdf()
