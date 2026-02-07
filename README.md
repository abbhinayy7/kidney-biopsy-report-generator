# Kidney Biopsy Report Generator

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Mac%20%7C%20Linux-blue.svg)]()

A professional desktop application for managing and generating kidney biopsy pathology reports in PDF format. Built with Python and Tkinter, this tool streamlines the creation and organization of medical reports.

---

## 🎯 Features

✅ **Easy Report Loading** - Load existing kidney biopsy cases by Biopsy Number
✅ **Live Preview** - See a formatted preview of the report before generating PDF
✅ **Multi-Tab Interface** - Organized form with 4 tabs (Patient Info, Case Details, Clinical Findings, Report)
✅ **PDF Generation** - Create professional, formatted PDF reports
✅ **Bulk Processing** - Generate multiple reports at once from a list
✅ **Smart Data Mapping** - Automatically maps JSON data to form fields
✅ **Field Validation** - Ensures all required fields are filled
✅ **Cross-Platform** - Works on Windows, macOS, and Linux

---

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Guide](#usage-guide)
- [Project Structure](#project-structure)
- [Features in Detail](#features-in-detail)
- [Data Format](#data-format)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/kidney-biopsy-report-generator.git
cd kidney-biopsy-report-generator
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

**Or install manually:**
```bash
pip install fpdf
```

### Step 3: Verify Installation
```bash
python kidney_biopsy_report_generator.py
```

---

## 🎬 Quick Start

### Windows Users
Simply double-click:
```
Launch_Report_Generator.bat
```

### All Platforms
```bash
python kidney_biopsy_report_generator.py
```

### Example Workflow
1. **Load a Report** - Enter a Biopsy Number and click "Load"
2. **Review Preview** - A preview window shows the report data
3. **Edit if Needed** - Modify any fields in the form
4. **Generate PDF** - Click "Generate PDF Report" and choose save location

---

## 📖 Usage Guide

### Loading a Report by Biopsy Number

1. In the **Quick Toolbar** at the top, enter a Biopsy Number
2. Click the **"Load"** button
3. The form auto-fills with existing data
4. A **Report Preview** window opens showing formatted data
5. Review and close the preview
6. Edit any fields if needed

### Generating a Single PDF Report

1. Fill in or load all required fields:
   - Report ID
   - Patient Name
   - Age
   - Gender
   - Receipt Date

2. Click **"Generate PDF Report"**
3. Choose where to save the file
4. Success message appears when PDF is created

### Bulk Generating Multiple Reports

1. Click **"Bulk Generate"**
2. Choose data source:
   - **From File**: Upload a .txt or .csv with Biopsy Numbers
   - **Manual Entry**: Enter comma-separated Biopsy Numbers
3. Select output folder for PDFs
4. All reports generate automatically
5. See summary of successful/failed generations

### Clearing the Form

- Click **"Clear All"** to reset all fields
- You'll be asked to confirm

---

## 🏗️ Project Structure

```
kidney-biopsy-report-generator/
├── kidney_biopsy_report_generator.py  # Main application
├── reports_data.json                  # Master data file
├── Launch_Report_Generator.bat        # Windows launcher
├── requirements.txt                   # Python dependencies
├── README.md                          # This file
├── Individual_PDF_Reports/            # Generated PDFs
├── Reports_By_Year/                   # Reports organized by year
├── Test_Reports/                      # Test data
└── repo/                              # Additional files
```

---

## 🎨 Features in Detail

### Tab 1: Patient Information
- **Report ID** - Unique identifier
- **Patient Name** - Full name
- **Age** - Patient age
- **Gender** - Male/Female
- **Receipt Date** - When specimen received
- **Year** - Fiscal year

### Tab 2: Case Details
- **Case Reference Number** - CR No.
- **Biopsy Number** - Primary identifier for loading data
- **Ward Number** - Hospital ward
- **Referred By** - Referring physician
- **Reference Number** - Additional reference
- **Specimen Received** - Specimen details

### Tab 3: Clinical Findings
- **Microscopic Findings** - Detailed pathological observations
- **Pathological Impression** - Clinical diagnosis and assessment

### Tab 4: Report & Impressions
- **Keywords/Diagnosis** - Key diagnostic terms
- **Clinical Notes** - Additional clinical information
- **Reported By** - Pathologist name
- **Report Date** - Date of report
- **ICD Code** - Medical coding

### Report Preview Window
- Automatically opens after loading a report
- Shows all loaded data in formatted layout
- Scrollable text area
- Read-only display
- Close button to dismiss

### PDF Report Output
Professional formatting with:
- Report title and department header
- Organized sections
- All filled data included
- Pathologist signature line
- Report date and timestamp
- ICD code documentation

---

## 📊 Data Format

### reports_data.json Structure
```json
[
  ["ID", "Name", "Age", "Sex", "Receipt Date", "Biopsy No.", ...],
  ["001", "John Doe", "45", "Male", "01-01-2024", "BIO-2024-001", ...],
  ["002", "Jane Smith", "52", "Female", "02-01-2024", "BIO-2024-002", ...],
  ...
]
```

**Key Requirements:**
- First row must be column headers
- Must include "Biopsy No." or "Biopsy Number" column
- Supports flexible column naming (e.g., "Name" or "Patient Name")
- UTF-8 encoding recommended

### Expected Columns
| Column | Alternative Names | Type |
|--------|------------------|------|
| ID | Report ID | String |
| Name | Patient Name | String |
| Age | - | String/Number |
| Sex | Gender | String |
| Receipt Date | - | String (DD-MM-YYYY) |
| Biopsy No. | Biopsy Number | String |
| Ward No. | Ward Number | String |
| CR No. | Case Reference Number | String |
| Referred by | Referred By | String |
| Report | Microscopic Findings | String (Long) |
| Impression | Pathological Impression | String (Long) |
| Keywords | Diagnosis, Keywords/Diagnosis | String |
| Note | Clinical Notes | String |
| Reported By | - | String |
| Date of Report | Report Date | String |
| ICD Code | - | String |

---

## 🔧 Troubleshooting

### Issue: "reports_data.json not found"
**Solution:** Place `reports_data.json` in the same directory as the script, or update the path in line 147-148.

### Issue: "Biopsy Number not found in data file"
**Solution:** 
- Verify the Biopsy Number exists in reports_data.json
- Check spelling exactly
- Ensure reports_data.json is properly formatted

### Issue: PDF won't generate
**Solution:**
- Verify all required fields are filled (ID, Name, Age, Sex, Receipt Date)
- Ensure you have write permissions to the save location
- Try saving to a different folder

### Issue: Special characters appear incorrectly in PDF
**Solution:**
- Ensure reports_data.json is saved as UTF-8
- Use standard Latin characters if possible

### Issue: Application won't start on Windows
**Solution:**
- Verify Python 3.8+ is installed: `python --version`
- Try running from PowerShell: `python kidney_biopsy_report_generator.py`
- Reinstall dependencies: `pip install --upgrade fpdf`

---

## 🛠️ Requirements

```
fpdf==1.7.2
```

The application uses Python's built-in `tkinter` for the GUI, which is included with most Python distributions.

---

## 📦 Installation from requirements.txt

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Make** your changes
4. **Commit** with clear messages (`git commit -m 'Add amazing feature'`)
5. **Push** to your branch (`git push origin feature/amazing-feature`)
6. **Open** a Pull Request

### Development Setup
```bash
git clone https://github.com/yourusername/kidney-biopsy-report-generator.git
cd kidney-biopsy-report-generator
pip install -r requirements.txt
python kidney_biopsy_report_generator.py
```

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Dr. Vinita

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 👨‍⚕️ About

Developed for medical professionals to streamline the creation and management of kidney biopsy pathology reports. Built with attention to medical documentation standards and user experience.

---

## 📧 Contact & Support

- **Issues:** Report bugs via [GitHub Issues](https://github.com/yourusername/kidney-biopsy-report-generator/issues)
- **Questions:** Start a [GitHub Discussion](https://github.com/yourusername/kidney-biopsy-report-generator/discussions)

---

## 🎓 How It Works

```
┌─────────────────────────────────────────────────┐
│  KIDNEY BIOPSY REPORT GENERATOR WORKFLOW        │
└─────────────────────────────────────────────────┘

Step 1: Load Data
   ↓
   Application loads reports_data.json at startup
   Creates searchable database by Biopsy Number
   
Step 2: Enter Biopsy Number
   ↓
   User enters Biopsy Number in quick toolbar
   
Step 3: Auto-Fill & Preview
   ↓
   Form fields populate automatically
   Report preview window opens
   User can review data before editing
   
Step 4: Edit (Optional)
   ↓
   User can modify any field in the form
   
Step 5: Generate PDF
   ↓
   System validates required fields
   Creates professional PDF with formatting
   Saves to user-selected location
   
Step 6: Confirmation
   ↓
   Success message with file location
```

---

## ✨ Version History

### v1.0.0 (Current)
- ✅ Core report generation functionality
- ✅ Biopsy Number-based loading
- ✅ Report preview window
- ✅ Bulk PDF generation
- ✅ Four-tab form interface
- ✅ Professional PDF formatting

---

## 🚀 Future Enhancements

Potential features for future versions:
- [ ] Database integration (SQL)
- [ ] Email report delivery
- [ ] Digital signature support
- [ ] Report templates customization
- [ ] Analytics dashboard
- [ ] Dark mode support
- [ ] Multi-language support
- [ ] Cloud backup integration

---



*Last Updated: February 6, 2026*
