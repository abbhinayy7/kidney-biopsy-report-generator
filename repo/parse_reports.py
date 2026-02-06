#!/usr/bin/env python
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime
import json

# Parse the XML file
xml_file = r'g:\dr_vinita\xml convert\reports.xls'
tree = ET.parse(xml_file)
root = tree.getroot()

# Define the namespace
ns = {'ss': 'urn:schemas-microsoft-com:office:spreadsheet'}

# Extract data by rows
rows_data = []
for row in root.findall('.//ss:Row', ns):
    row_cells = []
    for cell in row.findall('.//ss:Cell', ns):
        data_elem = cell.find('.//ss:Data', ns)
        if data_elem is not None and data_elem.text:
            row_cells.append(data_elem.text.strip())
        else:
            row_cells.append('')
    if any(row_cells):  # Only add non-empty rows
        rows_data.append(row_cells)

print(f"Total rows extracted: {len(rows_data)}")
print(f"\nFirst row (likely headers):")
if rows_data:
    print(rows_data[0])

# Save to JSON for easier processing
with open(r'g:\dr_vinita\xml convert\reports_data.json', 'w') as f:
    json.dump(rows_data, f, indent=2)

print("\nData saved to reports_data.json")

# Generate statistics
print(f"\n\n=== QUICK STATISTICS ===")
print(f"Total reports: {len(rows_data) - 1 if rows_data else 0}")  # Subtract header row
if len(rows_data) > 1:
    print(f"Data columns per row: {len(rows_data[0])}")

# Print sample of data (first 5 non-header rows)
print(f"\n\n=== SAMPLE DATA ===")
for i, row in enumerate(rows_data[1:6]):  # Skip header
    print(f"\nReport {i+1}:")
    if len(row) > 5:
        print(f"  Date: {row[1]}")
        print(f"  Patient Name: {row[6] if len(row) > 6 else 'N/A'}")
        print(f"  Age: {row[7] if len(row) > 7 else 'N/A'}")
        print(f"  Gender: {row[9] if len(row) > 9 else 'N/A'}")
        print(f"  Test Type: {row[10] if len(row) > 10 else 'N/A'}")
