#!/usr/bin/env python
import json
from collections import defaultdict
from datetime import datetime

# Load the extracted data
with open(r'g:\dr_vinita\xml convert\reports_data.json', 'r') as f:
    rows_data = json.load(f)

# Extract headers and data
headers = rows_data[0] if rows_data else []
data_rows = rows_data[1:] if len(rows_data) > 1 else []

# Create analysis
gender_count = defaultdict(int)
age_groups = defaultdict(int)
referred_by_count = defaultdict(int)
yearly_count = defaultdict(int)
keywords_list = defaultdict(int)

for row in data_rows:
    if len(row) >= 20:
        # Extract fields
        gender = row[9].strip() if len(row) > 9 else ""
        age_str = row[7].strip() if len(row) > 7 else ""
        referred_by = row[8].strip() if len(row) > 8 else ""
        year = row[2].strip() if len(row) > 2 else ""
        keywords = row[18].strip() if len(row) > 18 else ""
        
        # Count gender
        if gender:
            gender_count[gender] += 1
        
        # Parse age and group
        try:
            age_num = int(''.join(c for c in age_str if c.isdigit()))
            if age_num < 10:
                age_groups['0-9'] += 1
            elif age_num < 20:
                age_groups['10-19'] += 1
            elif age_num < 30:
                age_groups['20-29'] += 1
            elif age_num < 40:
                age_groups['30-39'] += 1
            elif age_num < 50:
                age_groups['40-49'] += 1
            elif age_num < 60:
                age_groups['50-59'] += 1
            else:
                age_groups['60+'] += 1
        except:
            pass
        
        # Count referred by doctors
        if referred_by:
            referred_by_count[referred_by] += 1
        
        # Count by year
        if year:
            yearly_count[year] += 1
        
        # Count keywords
        if keywords:
            keyword_list = [k.strip() for k in keywords.split(',')]
            for kw in keyword_list:
                if kw:
                    keywords_list[kw] += 1

# Generate HTML Report
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kidney Biopsy Reports - Comprehensive Analysis</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 20px;
            line-height: 1.6;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .executive-summary {{
            background: #f8f9fa;
            border-left: 4px solid #667eea;
            padding: 20px;
            margin-bottom: 30px;
            border-radius: 5px;
        }}
        
        .metrics {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }}
        
        .metric-card {{
            background: white;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            transition: transform 0.3s ease;
        }}
        
        .metric-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        
        .metric-value {{
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
            margin: 10px 0;
        }}
        
        .metric-label {{
            font-size: 0.95em;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .section {{
            margin-bottom: 40px;
        }}
        
        .section-title {{
            font-size: 1.8em;
            color: #333;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }}
        
        .data-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }}
        
        .data-table th {{
            background: #f0f0f0;
            color: #333;
            padding: 12px;
            text-align: left;
            font-weight: 600;
            border-bottom: 2px solid #ddd;
        }}
        
        .data-table td {{
            padding: 12px;
            border-bottom: 1px solid #eee;
        }}
        
        .data-table tr:hover {{
            background: #f9f9f9;
        }}
        
        .chart-container {{
            margin: 20px 0;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 8px;
        }}
        
        .bar {{
            display: flex;
            align-items: center;
            margin: 10px 0;
        }}
        
        .bar-label {{
            width: 150px;
            font-weight: 500;
        }}
        
        .bar-content {{
            flex: 1;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            height: 30px;
            border-radius: 5px;
            display: flex;
            align-items: center;
            padding: 0 10px;
            color: white;
            font-weight: 600;
            margin: 0 10px;
        }}
        
        .bar-value {{
            min-width: 40px;
            text-align: right;
        }}
        
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            border-top: 1px solid #ddd;
        }}
        
        .timestamp {{
            color: #999;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Pathology Reports Dashboard</h1>
            <p>Kidney Biopsy Analysis & Statistics</p>
            <p class="timestamp">Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
        
        <div class="content">
            <!-- Executive Summary -->
            <div class="executive-summary">
                <h3>Executive Summary</h3>
                <p>This comprehensive report presents an analysis of {len(data_rows)} kidney biopsy reports from the medical pathology database. 
                The dataset spans multiple years and includes detailed patient demographics, clinical findings, and pathological impressions. 
                This analysis provides insights into patient distribution, gender demographics, age patterns, and referring physicians.</p>
            </div>
            
            <!-- Key Metrics -->
            <div class="metrics">
                <div class="metric-card">
                    <div class="metric-label">Total Reports</div>
                    <div class="metric-value">{len(data_rows)}</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">Data Fields</div>
                    <div class="metric-value">{len(headers)}</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">Years Covered</div>
                    <div class="metric-value">{len(yearly_count)}</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">Referring Doctors</div>
                    <div class="metric-value">{len(referred_by_count)}</div>
                </div>
            </div>
            
            <!-- Gender Distribution -->
            <div class="section">
                <h2 class="section-title">Gender Distribution</h2>
                <div class="chart-container">
"""

# Add gender distribution data
for gender, count in sorted(gender_count.items(), key=lambda x: x[1], reverse=True):
    if gender:
        percentage = (count / len(data_rows) * 100) if len(data_rows) > 0 else 0
        html_content += f"""
                    <div class="bar">
                        <div class="bar-label">{gender}</div>
                        <div class="bar-content" style="width: {min(percentage * 3, 100)}%;">{count}</div>
                        <div class="bar-value">{percentage:.1f}%</div>
                    </div>
"""

html_content += """
                </div>
                <table class="data-table">
                    <tr>
                        <th>Gender</th>
                        <th>Count</th>
                        <th>Percentage</th>
                    </tr>
"""

for gender, count in sorted(gender_count.items(), key=lambda x: x[1], reverse=True):
    if gender:
        percentage = (count / len(data_rows) * 100) if len(data_rows) > 0 else 0
        html_content += f"                    <tr><td>{gender}</td><td>{count}</td><td>{percentage:.2f}%</td></tr>\n"

html_content += """
                </table>
            </div>
            
            <!-- Age Distribution -->
            <div class="section">
                <h2 class="section-title">Age Group Distribution</h2>
                <div class="chart-container">
"""

# Add age distribution data
age_order = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60+']
for age_group in age_order:
    if age_group in age_groups:
        count = age_groups[age_group]
        percentage = (count / len(data_rows) * 100) if len(data_rows) > 0 else 0
        html_content += f"""
                    <div class="bar">
                        <div class="bar-label">{age_group} years</div>
                        <div class="bar-content" style="width: {min(percentage * 3, 100)}%;">{count}</div>
                        <div class="bar-value">{percentage:.1f}%</div>
                    </div>
"""

html_content += """
                </div>
                <table class="data-table">
                    <tr>
                        <th>Age Group</th>
                        <th>Count</th>
                        <th>Percentage</th>
                    </tr>
"""

for age_group in age_order:
    if age_group in age_groups:
        count = age_groups[age_group]
        percentage = (count / len(data_rows) * 100) if len(data_rows) > 0 else 0
        html_content += f"                    <tr><td>{age_group} years</td><td>{count}</td><td>{percentage:.2f}%</td></tr>\n"

html_content += """
                </table>
            </div>
            
            <!-- Year-wise Distribution -->
            <div class="section">
                <h2 class="section-title">Year-wise Distribution</h2>
                <table class="data-table">
                    <tr>
                        <th>Year</th>
                        <th>Number of Reports</th>
                        <th>Percentage</th>
                    </tr>
"""

for year in sorted(yearly_count.keys()):
    count = yearly_count[year]
    percentage = (count / len(data_rows) * 100) if len(data_rows) > 0 else 0
    html_content += f"                    <tr><td>{year}</td><td>{count}</td><td>{percentage:.2f}%</td></tr>\n"

html_content += """
                </table>
            </div>
            
            <!-- Top Referring Physicians -->
            <div class="section">
                <h2 class="section-title">Top Referring Physicians</h2>
                <table class="data-table">
                    <tr>
                        <th>Physician Name</th>
                        <th>Number of Referrals</th>
                        <th>Percentage</th>
                    </tr>
"""

# Get top 15 referring doctors
top_doctors = sorted(referred_by_count.items(), key=lambda x: x[1], reverse=True)[:15]
for doctor, count in top_doctors:
    if doctor:
        percentage = (count / len(data_rows) * 100) if len(data_rows) > 0 else 0
        html_content += f"                    <tr><td>{doctor}</td><td>{count}</td><td>{percentage:.2f}%</td></tr>\n"

html_content += """
                </table>
            </div>
            
            <!-- Keywords/Diagnoses -->
            <div class="section">
                <h2 class="section-title">Top Clinical Keywords/Diagnoses</h2>
                <table class="data-table">
                    <tr>
                        <th>Keyword</th>
                        <th>Frequency</th>
                        <th>Percentage</th>
                    </tr>
"""

# Get top 20 keywords
top_keywords = sorted(keywords_list.items(), key=lambda x: x[1], reverse=True)[:20]
for keyword, count in top_keywords:
    if keyword:
        percentage = (count / len(data_rows) * 100) if len(data_rows) > 0 else 0
        html_content += f"                    <tr><td>{keyword}</td><td>{count}</td><td>{percentage:.2f}%</td></tr>\n"

html_content += """
                </table>
            </div>
            
            <!-- Data Dictionary -->
            <div class="section">
                <h2 class="section-title">Data Fields Dictionary</h2>
                <table class="data-table">
                    <tr>
                        <th>Field Name</th>
                        <th>Description</th>
                    </tr>
"""

field_descriptions = {
    "ID": "Unique identifier for each report",
    "Receipt Date": "Date when the biopsy sample was received",
    "Year": "Year of receipt",
    "CR No.": "Case Reference Number",
    "Biopsy No.": "Biopsy sample number",
    "Ward No.": "Ward number from where patient was referred",
    "Name": "Patient name",
    "Age": "Patient age in years",
    "Referred by": "Name of the referring physician",
    "Sex": "Patient gender (Male/Female)",
    "Reference No.": "Clinical reference number",
    "Specimen Received": "Type of specimen received",
    "Report": "Detailed pathological findings",
    "Impression": "Clinical impression and diagnosis",
    "Note": "Additional clinical notes",
    "Addendum": "Any additional information",
    "Reported By": "Name of the pathologist",
    "Date of Report": "Date when report was finalized",
    "Keywords": "Associated clinical keywords",
    "ICD Code": "International Classification of Diseases code"
}

for header in headers:
    description = field_descriptions.get(header, "Clinical data field")
    html_content += f"                    <tr><td><strong>{header}</strong></td><td>{description}</td></tr>\n"

html_content += """
                </table>
            </div>
        </div>
        
        <div class="footer">
            <p><strong>Report Information:</strong> This comprehensive analysis was automatically generated from the pathology database.</p>
            <p>For detailed case information, please refer to individual patient records in the database.</p>
            <p class="timestamp">Generated: {}</p>
        </div>
    </div>
</body>
</html>
""".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# Save the HTML report
output_file = r'g:\dr_vinita\xml convert\REPORTS_ANALYSIS.html'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"✓ Report successfully created!")
print(f"✓ File saved as: REPORTS_ANALYSIS.html")
print(f"✓ Location: {output_file}")
print(f"\nReport Summary:")
print(f"  - Total Reports: {len(data_rows)}")
print(f"  - Male/Female Ratio: {gender_count.get('Male', 0)}/{gender_count.get('Female', 0)}")
print(f"  - Top Age Group: {max(age_groups.items(), key=lambda x: x[1])[0]}")
print(f"  - Data Spanning: {min(yearly_count.keys())} to {max(yearly_count.keys())}")
print(f"  - Top Referring Doctor: {max(referred_by_count.items(), key=lambda x: x[1])[0]}")
