import tkinter as tk
from kidney_biopsy_report_generator import ReportGeneratorApp

root = tk.Tk()
root.withdraw()
app = ReportGeneratorApp(root)
print('Loaded records:', len(app.data_map))
root.destroy()
