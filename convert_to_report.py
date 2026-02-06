#!/usr/bin/env python
import sys

# Try different approaches to read the Excel file
try:
    import win32com.client as win32
    
    # Use Excel COM object
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = excel.Workbooks.Open(r'g:\dr_vinita\xml convert\reports.xls')
    ws = wb.Sheets(1)
    
    # Get data
    data = []
    for row in ws.UsedRange.Rows:
        row_data = []
        for cell in row.Cells:
            row_data.append(cell.Value)
        data.append(row_data)
    
    # Print for debugging
    print(f"Total rows: {len(data)}")
    for i, row in enumerate(data[:10]):
        print(f"Row {i}: {row}")
    
    wb.Close()
    excel.Quit()
    
except ImportError:
    print("win32com not available, trying pandas with openpyxl...")
    try:
        import pandas as pd
        # Try reading with pandas openpyxl
        df = pd.read_excel(r'g:\dr_vinita\xml convert\reports.xls')
        print(df)
    except Exception as e:
        print(f"Error: {e}")
