#!/usr/bin/env python
"""
Kidney Biopsy Report Generator - Interactive Utility
Allows users to enter report details and generate PDF reports
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime
import os
from fpdf import FPDF

class ReportGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kidney Biopsy Report Generator")
        self.root.geometry("900x800")
        
        # Dictionary to store all fields - INITIALIZE FIRST
        self.fields = {}
        
        # Set style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Color scheme
        self.bg_color = "#f0f0f0"
        self.root.configure(bg=self.bg_color)
        
        # Create main frame
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title = ttk.Label(self.main_frame, text="KIDNEY BIOPSY REPORT GENERATOR", 
                         font=("Arial", 14, "bold"))
        title.pack(pady=10)
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Tab 1: Patient Information
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Patient Information")
        self.create_patient_tab()
        
        # Tab 2: Case Details
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Case Details")
        self.create_case_tab()
        
        # Tab 3: Clinical Findings
        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="Clinical Findings")
        self.create_findings_tab()
        
        # Tab 4: Report & Impressions
        self.tab4 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab4, text="Report & Impressions")
        self.create_report_tab()
        
        # Button frame
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        self.generate_btn = ttk.Button(button_frame, text="Generate PDF Report", 
                                       command=self.generate_report)
        self.generate_btn.pack(side=tk.LEFT, padx=5)
        
        self.clear_btn = ttk.Button(button_frame, text="Clear All", 
                                    command=self.clear_all)
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        self.exit_btn = ttk.Button(button_frame, text="Exit", 
                                   command=root.quit)
        self.exit_btn.pack(side=tk.RIGHT, padx=5)
        
    def create_patient_tab(self):
        """Create patient information input fields"""
        frame = ttk.Frame(self.tab1)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create scrollbar
        canvas = tk.Canvas(frame, bg=self.bg_color, highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Patient fields
        self.fields_list = [
            ('ID', 'Report ID', 'text'),
            ('Name', 'Patient Name', 'text'),
            ('Age', 'Age (e.g., 25 years)', 'text'),
            ('Sex', 'Gender (Male/Female)', 'combo', ['Male', 'Female']),
            ('Receipt Date', 'Receipt Date (DD-MM-YYYY)', 'text'),
            ('Year', 'Year', 'text'),
        ]
        
        row = 0
        for field in self.fields_list[:6]:
            label = ttk.Label(scrollable_frame, text=field[1] + ":")
            label.grid(row=row, column=0, sticky='w', pady=8, padx=5)
            
            if field[2] == 'text':
                entry = ttk.Entry(scrollable_frame, width=40)
                entry.grid(row=row, column=1, sticky='ew', pady=8, padx=5)
                self.fields[field[0]] = entry
            elif field[2] == 'combo':
                combo = ttk.Combobox(scrollable_frame, values=field[3], width=38)
                combo.grid(row=row, column=1, sticky='ew', pady=8, padx=5)
                self.fields[field[0]] = combo
            
            row += 1
        
        scrollable_frame.columnconfigure(1, weight=1)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def create_case_tab(self):
        """Create case details input fields"""
        frame = ttk.Frame(self.tab2)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        case_fields = [
            ('CR No.', 'Case Reference Number', 'text'),
            ('Biopsy No.', 'Biopsy Number', 'text'),
            ('Ward No.', 'Ward Number', 'text'),
            ('Referred by', 'Referred By (Doctor Name)', 'text'),
            ('Reference No.', 'Reference Number', 'text'),
            ('Speciment Received', 'Specimen Received', 'text'),
        ]
        
        row = 0
        for field in case_fields:
            label = ttk.Label(frame, text=field[1] + ":")
            label.grid(row=row, column=0, sticky='w', pady=8, padx=5)
            
            entry = ttk.Entry(frame, width=50)
            entry.grid(row=row, column=1, sticky='ew', pady=8, padx=5)
            self.fields[field[0]] = entry
            
            row += 1
        
        frame.columnconfigure(1, weight=1)
    
    def create_findings_tab(self):
        """Create clinical findings input fields"""
        frame = ttk.Frame(self.tab3)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Microscopic Report
        label = ttk.Label(frame, text="Microscopic Findings (Report):")
        label.grid(row=0, column=0, sticky='nw', pady=5, padx=5)
        
        report_text = tk.Text(frame, height=6, width=60)
        report_text.grid(row=0, column=1, sticky='ew', pady=5, padx=5)
        self.fields['Report'] = report_text
        
        # Impression
        label = ttk.Label(frame, text="Pathological Impression:")
        label.grid(row=1, column=0, sticky='nw', pady=5, padx=5)
        
        impression_text = tk.Text(frame, height=6, width=60)
        impression_text.grid(row=1, column=1, sticky='ew', pady=5, padx=5)
        self.fields['Impression'] = impression_text
        
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
    
    def create_report_tab(self):
        """Create additional report fields"""
        frame = ttk.Frame(self.tab4)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        row = 0
        
        # Keywords
        label = ttk.Label(frame, text="Keywords/Diagnosis:")
        label.grid(row=row, column=0, sticky='nw', pady=5, padx=5)
        
        keywords_text = tk.Text(frame, height=4, width=60)
        keywords_text.grid(row=row, column=1, sticky='ew', pady=5, padx=5)
        self.fields['Keywords'] = keywords_text
        
        row += 1
        
        # Additional fields
        simple_fields = [
            ('Note', 'Clinical Notes', 'text_area'),
            ('Reported By', 'Reported By (Pathologist Name)', 'text'),
            ('Date of Report', 'Report Date (DD-MM-YYYY)', 'text'),
            ('ICD Code', 'ICD Code', 'text'),
        ]
        
        for field in simple_fields:
            label = ttk.Label(frame, text=field[1] + ":")
            label.grid(row=row, column=0, sticky='nw', pady=5, padx=5)
            
            if field[2] == 'text_area':
                text_widget = tk.Text(frame, height=4, width=60)
                text_widget.grid(row=row, column=1, sticky='ew', pady=5, padx=5)
                self.fields[field[0]] = text_widget
            else:
                entry = ttk.Entry(frame, width=50)
                entry.grid(row=row, column=1, sticky='ew', pady=5, padx=5)
                self.fields[field[0]] = entry
            
            row += 1
        
        frame.columnconfigure(1, weight=1)
    
    def get_field_value(self, field_name):
        """Get value from field"""
        widget = self.fields[field_name]
        if isinstance(widget, tk.Text):
            return widget.get("1.0", tk.END).strip()
        else:
            return widget.get()
    
    def generate_report(self):
        """Generate PDF report"""
        try:
            # Validate required fields
            required_fields = ['ID', 'Name', 'Age', 'Sex', 'Receipt Date']
            missing = [f for f in required_fields if not self.get_field_value(f)]
            
            if missing:
                messagebox.showerror("Missing Fields", 
                                   f"Please fill in: {', '.join(missing)}")
                return
            
            # Ask for save location
            file_path = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
                initialfile=f"{self.get_field_value('ID')}_{self.get_field_value('Name')}.pdf"
            )
            
            if not file_path:
                return
            
            # Create PDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Helvetica", "", 10)
            
            # Title
            pdf.set_font("Helvetica", "B", 14)
            pdf.cell(0, 8, "KIDNEY BIOPSY PATHOLOGY REPORT", ln=True, align="C")
            pdf.set_font("Helvetica", "", 9)
            pdf.cell(0, 6, "Department of Pathology - Medical Analysis Center", 
                    ln=True, align="C")
            pdf.ln(4)
            
            # Patient Information
            pdf.set_font("Helvetica", "B", 10)
            pdf.cell(0, 6, "PATIENT INFORMATION", ln=True)
            pdf.set_font("Helvetica", "", 9)
            
            patient_data = [
                ('ID', 'Report ID'),
                ('Name', 'Patient Name'),
                ('Age', 'Age'),
                ('Sex', 'Gender'),
                ('Receipt Date', 'Receipt Date'),
                ('Year', 'Year'),
            ]
            
            for field, label in patient_data:
                pdf.cell(40, 6, label + ":", border=0)
                pdf.cell(0, 6, self.get_field_value(field), ln=True, border=0)
            
            pdf.ln(2)
            
            # Case Details
            pdf.set_font("Helvetica", "B", 10)
            pdf.cell(0, 6, "CASE DETAILS", ln=True)
            pdf.set_font("Helvetica", "", 9)
            
            case_data = [
                ('CR No.', 'Case Reference'),
                ('Biopsy No.', 'Biopsy Number'),
                ('Ward No.', 'Ward'),
                ('Referred by', 'Referred By'),
                ('Reference No.', 'Reference No.'),
                ('Speciment Received', 'Specimen'),
            ]
            
            for field, label in case_data:
                pdf.cell(40, 6, label + ":", border=0)
                pdf.cell(0, 6, self.get_field_value(field)[:40], ln=True, border=0)
            
            pdf.ln(2)
            
            # Microscopic Findings
            report_val = self.get_field_value('Report')
            if report_val:
                pdf.set_font("Helvetica", "B", 10)
                pdf.cell(0, 6, "MICROSCOPIC FINDINGS", ln=True)
                pdf.set_font("Helvetica", "", 9)
                pdf.multi_cell(0, 5, report_val)
                pdf.ln(2)
            
            # Impression
            impression_val = self.get_field_value('Impression')
            if impression_val:
                pdf.set_font("Helvetica", "B", 10)
                pdf.cell(0, 6, "PATHOLOGICAL IMPRESSION", ln=True)
                pdf.set_font("Helvetica", "", 9)
                pdf.multi_cell(0, 5, impression_val)
                pdf.ln(2)
            
            # Clinical Notes
            note_val = self.get_field_value('Note')
            if note_val:
                pdf.set_font("Helvetica", "B", 10)
                pdf.cell(0, 6, "CLINICAL NOTES", ln=True)
                pdf.set_font("Helvetica", "", 9)
                pdf.multi_cell(0, 5, note_val)
                pdf.ln(2)
            
            # Keywords
            keywords_val = self.get_field_value('Keywords')
            if keywords_val:
                pdf.set_font("Helvetica", "B", 10)
                pdf.cell(0, 6, "KEYWORDS/DIAGNOSIS", ln=True)
                pdf.set_font("Helvetica", "", 9)
                pdf.multi_cell(0, 5, keywords_val)
                pdf.ln(2)
            
            # Footer
            pdf.ln(2)
            pdf.set_font("Helvetica", "B", 9)
            pdf.cell(40, 6, "Reported By:", border=0)
            pdf.cell(0, 6, self.get_field_value('Reported By'), ln=True, border=0)
            
            pdf.cell(40, 6, "Report Date:", border=0)
            pdf.cell(0, 6, self.get_field_value('Date of Report'), ln=True, border=0)
            
            pdf.cell(40, 6, "ICD Code:", border=0)
            pdf.cell(0, 6, self.get_field_value('ICD Code'), ln=True, border=0)
            
            # Timestamp
            pdf.ln(3)
            pdf.set_font("Helvetica", "", 8)
            timestamp = f"PDF Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            pdf.cell(0, 6, timestamp, ln=True, align="C")
            
            # Save PDF
            pdf.output(file_path)
            
            messagebox.showinfo("Success", 
                              f"PDF report generated successfully!\n\nSaved to:\n{file_path}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error generating report:\n{str(e)}")
    
    def clear_all(self):
        """Clear all fields"""
        response = messagebox.askyesno("Clear All", 
                                      "Are you sure you want to clear all fields?")
        if response:
            for widget in self.fields.values():
                if isinstance(widget, tk.Text):
                    widget.delete("1.0", tk.END)
                else:
                    widget.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ReportGeneratorApp(root)
    root.mainloop()
