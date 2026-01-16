import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# -------------------------------
# Helper function to load CSV data
# -------------------------------
def load_csv():
    file_path = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    if not file_path:
        return

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
            data = [line.split(",") for line in lines]
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read file:\n{e}")
        return

    if not data:
        messagebox.showwarning("Empty", "The selected file is empty.")
        return

    headers = data[0]
    rows = data[1:]

    # Clear old content
    tree.delete(*tree.get_children())

    # Set new columns (this is the key fix)
    tree["columns"] = list(range(len(headers)))
    
    # Configure column headings
    for i, header in enumerate(headers):
        tree.heading(i, text=header)
        tree.column(i, width=120, anchor=CENTER)

    # Insert rows
    for row in rows:
        tree.insert("", END, values=row)

    messagebox.showinfo("Success", f"Loaded {len(rows)} rows from:\n{file_path}")

# -------------------------------
# Additional functions
# -------------------------------
def export_to_csv():
    if not tree["columns"]:
        messagebox.showwarning("No Data", "No data to export.")
        return
        
    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    if not file_path:
        return
        
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            # Write headers
            headers = [tree.heading(col)['text'] for col in tree["columns"]]
            f.write(",".join(headers) + "\n")
            # Write data rows
            for item in tree.get_children():
                values = tree.item(item)['values']
                f.write(",".join(values) + "\n")
        messagebox.showinfo("Success", f"Data exported to:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to export file:\n{e}")

# -------------------------------
# Main Window setup
# -------------------------------
app = ttk.Window(themename="flatly")
app.title("📄 CSV Data Viewer")
app.geometry("900x600")

# Title label with better styling
title_frame = ttk.Frame(app)
title_frame.pack(fill=X, padx=10, pady=10)

ttk.Label(title_frame, text="📄 CSV Data Viewer", font=("Helvetica", 20, "bold")).pack(side=LEFT)

# Button frame
btn_frame = ttk.Frame(app)
btn_frame.pack(fill=X, padx=10, pady=5)

ttk.Button(btn_frame, text="Load CSV File", bootstyle=PRIMARY, command=load_csv).pack(side=LEFT, padx=5)
ttk.Button(btn_frame, text="Export to CSV", bootstyle=SUCCESS, command=export_to_csv).pack(side=LEFT, padx=5)

# Treeview with enhanced configuration
tree_frame = ttk.Frame(app)
tree_frame.pack(fill=BOTH, expand=True, padx=10, pady=(0, 10))

tree = ttk.Treeview(tree_frame, show="headings", bootstyle=INFO)
tree.pack(side=LEFT, fill=BOTH, expand=True)

# Scrollbars
y_scroll = ttk.Scrollbar(tree_frame, orient=VERTICAL, command=tree.yview)
y_scroll.pack(side=RIGHT, fill=Y)
tree.configure(yscrollcommand=y_scroll.set)

x_scroll = ttk.Scrollbar(app, orient=HORIZONTAL, command=tree.xview)
x_scroll.pack(fill=X, padx=10, pady=(0, 10))
tree.configure(xscrollcommand=x_scroll.set)

# Add sample data if no data loaded (for demonstration)
sample_headers = ["Name", "Age", "City", "Occupation"]
sample_data = [
    ["John Doe", "30", "New York", "Engineer"],
    ["Jane Smith", "25", "Los Angeles", "Designer"],
    ["Bob Johnson", "35", "Chicago", "Manager"]
]

# Add sample data to demonstrate the UI
tree["columns"] = list(range(len(sample_headers)))
for i, header in enumerate(sample_headers):
    tree.heading(i, text=header)
    tree.column(i, width=120, anchor=CENTER)

for row in sample_data:
    tree.insert("", END, values=row)

# Start app
app.mainloop()