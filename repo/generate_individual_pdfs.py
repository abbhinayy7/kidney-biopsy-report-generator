#!/usr/bin/env python
"""
Generate individual PDF reports for each kidney biopsy case using fpdf2
"""
import json
import os
from datetime import datetime
from fpdf import FPDF
import sys

# Load the data
print("Loading data...")
with open(r'g:\dr_vinita\xml convert\reports_data.json', 'r', encoding='utf-8') as f:
    rows_data = json.load(f)

headers = rows_data[0] if rows_data else []
data_rows = rows_data[1:] if len(rows_data) > 1 else []

# Create output directory
output_dir = r'g:\dr_vinita\xml convert\Individual_PDF_Reports'
os.makedirs(output_dir, exist_ok=True)

# Directory for organized reports (by year)
year_dir = r'g:\dr_vinita\xml convert\Reports_By_Year'
os.makedirs(year_dir, exist_ok=True)

print(f"Output directory: {output_dir}")
print(f"Creating {len(data_rows)} individual PDF reports...")
print("This may take several minutes...\n")

# Counter for progress
total_reports = len(data_rows)
processed = 0
successful = 0
failed = 0

def clean_text(text, max_length=None):
    """Clean and format text"""
    if text is None:
        return "N/A"
    text = str(text).strip()
    if not text:
        return "N/A"
    if max_length:
        return text[:max_length] + ("..." if len(text) > max_length else "")
    return text

def create_patient_report(row_data, report_num, headers):
    """Create a single PDF report"""
    global successful, failed
    
    try:
        # Extract data fields
        fields = {}
        for i, header in enumerate(headers):
            if i < len(row_data):
                fields[header] = clean_text(row_data[i])
            else:
                fields[header] = "N/A"
        
        # Create filename from case ID and patient name
        case_id = fields.get('ID', f"Case_{report_num}")
        patient_name = fields.get('Name', 'Unknown').replace(' ', '_')[:15]
        year = fields.get('Year', '2016')
        
        # Create safe filename
        filename = f"{case_id}_{patient_name}.pdf"
        filepath = os.path.join(output_dir, filename)
        
        # Also save in year-based subdirectory
        year_subdir = os.path.join(year_dir, f"Year_{year}")
        os.makedirs(year_subdir, exist_ok=True)
        year_filepath = os.path.join(year_subdir, filename)
        
        # Create PDF document
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", "", 10)
        
        # Title
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 8, "KIDNEY BIOPSY PATHOLOGY REPORT", ln=True, align="C")
        pdf.set_font("Helvetica", "", 9)
        pdf.cell(0, 6, "Department of Pathology - Medical Analysis Center", ln=True, align="C")
        pdf.ln(4)
        
        # Report metadata section
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(0, 6, "PATIENT INFORMATION", ln=True)
        pdf.set_font("Helvetica", "", 9)
        
        # Patient info table-like display
        pdf.cell(40, 6, "Report ID:", border=0)
        pdf.cell(0, 6, fields['ID'], ln=True, border=0)
        
        pdf.cell(40, 6, "Name:", border=0)
        pdf.cell(0, 6, fields['Name'], ln=True, border=0)
        
        pdf.cell(40, 6, "Age:", border=0)
        pdf.cell(0, 6, fields['Age'], ln=True, border=0)
        
        pdf.cell(40, 6, "Gender:", border=0)
        pdf.cell(0, 6, fields['Sex'], ln=True, border=0)
        
        pdf.ln(2)
        
        # Case Details
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(0, 6, "CASE DETAILS", ln=True)
        pdf.set_font("Helvetica", "", 9)
        
        pdf.cell(40, 6, "Receipt Date:", border=0)
        pdf.cell(0, 6, fields['Receipt Date'], ln=True, border=0)
        
        pdf.cell(40, 6, "Biopsy No:", border=0)
        pdf.cell(0, 6, fields['Biopsy No.'], ln=True, border=0)
        
        pdf.cell(40, 6, "Case Ref:", border=0)
        pdf.cell(0, 6, fields['CR No.'], ln=True, border=0)
        
        pdf.cell(40, 6, "Ward:", border=0)
        pdf.cell(0, 6, fields['Ward No.'], ln=True, border=0)
        
        pdf.cell(40, 6, "Referred By:", border=0)
        pdf.cell(0, 6, fields['Referred by'], ln=True, border=0)
        
        pdf.ln(2)
        
        # Specimen & Findings
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(0, 6, "SPECIMEN & FINDINGS", ln=True)
        pdf.set_font("Helvetica", "", 9)
        
        pdf.cell(40, 6, "Specimen:", border=0)
        pdf.cell(0, 6, fields['Speciment Received'][:30], ln=True, border=0)
        
        pdf.ln(2)
        
        # Microscopic Findings
        if fields['Report'] != 'N/A':
            pdf.set_font("Helvetica", "B", 10)
            pdf.cell(0, 6, "MICROSCOPIC FINDINGS", ln=True)
            pdf.set_font("Helvetica", "", 9)
            report_text = clean_text(fields['Report'], 500)
            pdf.multi_cell(0, 5, report_text)
            pdf.ln(2)
        
        # Impression
        if fields['Impression'] != 'N/A':
            pdf.set_font("Helvetica", "B", 10)
            pdf.cell(0, 6, "PATHOLOGICAL IMPRESSION", ln=True)
            pdf.set_font("Helvetica", "", 9)
            impression_text = clean_text(fields['Impression'], 400)
            pdf.multi_cell(0, 5, impression_text)
            pdf.ln(2)
        
        # Clinical Notes
        if fields['Note'] != 'N/A' and len(fields['Note']) > 2:
            pdf.set_font("Helvetica", "B", 10)
            pdf.cell(0, 6, "CLINICAL NOTES", ln=True)
            pdf.set_font("Helvetica", "", 9)
            notes_text = clean_text(fields['Note'], 300)
            pdf.multi_cell(0, 5, notes_text)
            pdf.ln(2)
        
        # Keywords
        if fields['Keywords'] != 'N/A':
            pdf.set_font("Helvetica", "B", 10)
            pdf.cell(0, 6, "KEYWORDS/DIAGNOSIS", ln=True)
            pdf.set_font("Helvetica", "", 9)
            pdf.multi_cell(0, 5, fields['Keywords'])
            pdf.ln(2)
        
        # Footer section
        pdf.ln(2)
        pdf.set_font("Helvetica", "B", 9)
        pdf.cell(40, 6, "Reported By:", border=0)
        pdf.cell(0, 6, fields['Reported By'], ln=True, border=0)
        
        pdf.cell(40, 6, "Report Date:", border=0)
        pdf.cell(0, 6, fields['Date of Report'], ln=True, border=0)
        
        pdf.cell(40, 6, "ICD Code:", border=0)
        pdf.cell(0, 6, fields['ICD Code'], ln=True, border=0)
        
        # Document timestamp
        pdf.ln(3)
        pdf.set_font("Helvetica", "", 8)
        timestamp = f"PDF Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        pdf.cell(0, 6, timestamp, ln=True, align="C")
        
        # Save to both locations
        pdf.output(filepath)
        
        # Copy to year subdirectory
        pdf.output(year_filepath)
        
        successful += 1
        return True
        
    except Exception as e:
        failed += 1
        print(f"Error creating report {report_num}: {str(e)[:50]}")
        return False

# Generate all reports
print(f"Starting PDF generation for {total_reports} reports...")
for idx, row_data in enumerate(data_rows):
    processed += 1
    if processed % 200 == 0:
        percentage = (processed / total_reports * 100)
        print(f"Progress: {processed}/{total_reports} ({percentage:.1f}%) - {successful} successful, {failed} failed")
    
    create_patient_report(row_data, idx + 1, headers)

print(f"\n{'='*70}")
print(f"REPORT GENERATION COMPLETE")
print(f"{'='*70}")
print(f"Total Reports Processed: {total_reports}")
print(f"Successfully Generated: {successful}")
print(f"Failed: {failed}")
print(f"\nOutput Locations:")
print(f"  • Main directory: {output_dir}")
print(f"  • Organized by year: {year_dir}")
print(f"{'='*70}")
