#!/usr/bin/env python
import xml.etree.ElementTree as ET
from datetime import datetime

# Parse the XML file
xml_file = r'g:\dr_vinita\xml convert\reports.xls'
tree = ET.parse(xml_file)
root = tree.getroot()

# Extract data from XML
print("XML Root tag:", root.tag)
print("\nExtracted data:")

# Try to understand the structure
def print_structure(element, level=0):
    indent = "  " * level
    attrs = ' '.join(f'{k}="{v}"' for k, v in element.attrib.items())
    print(f"{indent}<{element.tag} {attrs}>", end="")
    
    if element.text and element.text.strip():
        print(f" {element.text.strip()[:50]}")
    else:
        print()
    
    for child in element:
        print_structure(child, level + 1)

print_structure(root)

# Now let's create a structured report
report_data = []
for elem in root.iter():
    if elem.text and elem.text.strip():
        report_data.append({
            'tag': elem.tag,
            'text': elem.text.strip(),
            'attributes': elem.attrib
        })

print(f"\n\nTotal data elements found: {len(report_data)}")
