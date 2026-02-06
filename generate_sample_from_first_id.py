import os
import tkinter as tk
from kidney_biopsy_report_generator import ReportGeneratorApp

out_dir = r'g:\dr_vinita\xml convert\Test_Reports'
os.makedirs(out_dir, exist_ok=True)

root = tk.Tk()
root.withdraw()
app = ReportGeneratorApp(root)

if not app.data_map:
    print('No records loaded from reports_data.json')
    root.destroy()
    raise SystemExit(1)

first_id = next(iter(app.data_map.keys()))
print('Using Report ID:', first_id)
row = app.data_map[first_id]
app.populate_fields_from_row(row)

safe_name = f"{row.get('ID','')}_{row.get('Name','Unknown').replace(' ','_')}.pdf".replace('/','_').replace('\\','_')
out_path = os.path.join(out_dir, safe_name)

try:
    app._create_pdf_to_path(out_path)
    print('Sample PDF created:', out_path)
except Exception as e:
    print('Error generating sample PDF:', str(e))

root.destroy()
