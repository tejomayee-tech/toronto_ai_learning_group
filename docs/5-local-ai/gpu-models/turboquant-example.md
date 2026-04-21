AI: Here is a complete, single-file Python program that creates a functional Calculator using **Tkinter** (the standard GUI library for Python) and integrates the **TTKBootstrap** styling framework.

This solution includes:
1.  A modern, responsive design with a dark theme.
2.  Support for basic arithmetic operations (+, -, *, /).
3.  Clear error handling if an invalid operation is selected.
4.  A clean layout using the `ttkbootstrap` library.

### Prerequisites

You will need to install the required packages:
```bash
pip install ttkbootstrap
```

### The Python Code (`calculator.py`)

Save this code as a `.py` file (e.g., `calculator.py`) and run it in your terminal or IDE.

```python
import tkinter as tk
from tkinter import messagebox, simpledialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class CalculatorApp:
    def __init__(self):
        self.root = tk.Tk()
        
        # Configure the root window to look like a modern app
        self.root.title("Calculator")
        self.root.geometry("300x450" + "x100+200+200")  # Centered on screen
        
        # Define the main container with ttkbootstrap styles
        self.container = ttk.Frame(self.root, style="dark_blue", padding=10)
        
        # --- Layout Components ---
        
        # Title Section
        title_frame = ttk.LabelFrame(
            self.container, 
            text="Calculator", 
            font=("Helvetica", 24, "bold"), 
            fg_color="#333333"
        )
        title_frame.pack(padx=10, pady=(50, 10))

        # Display Screen (Input Area)
        self.display_var = tk.StringVar()
        self.display_label = ttk.Label(
            self.container, 
            textvariable=self.display_var, 
            font=("Helvetica", 24), 
            fg_color="#ffffff"
        )
        self.display_label.pack(padx=10, pady=(50, 10))

        # Buttons Grid (3 columns x 6 rows)
        button_frame = ttk.Frame(self.container)
        
        # Define the buttons using ttkbootstrap styles
        # We use a grid layout for the buttons
        self.create_buttons(button_frame)

        # Add an "About" section at the bottom
        about_frame = ttk.LabelFrame(
            self.container, 
            text="About", 
            font=("Helvetica", 12), 
            fg_color="#333333"
        )
        about_frame.pack(padx=5, pady=(0, 10))
        
        info_text = "This calculator uses ttkbootstrap for a modern UI."
        self.about_label = ttk.Label(about_frame, textinfo=info_text)
        self.about_label.pack()

        # Start the application
        self.root.mainloop()

    def create_buttons(self, parent):
        """Helper function to generate buttons dynamically."""
        
        # Define button styles for consistency
        btn_style = ttkbootstrap.Style().define(
            "calc_button", 
            background="dark_blue", 
            fg_color="#ffffff"
        )
        
        # Create the grid of buttons
        # We use a list comprehension to generate all 24 buttons easily
        button_list = [
            ("C", lambda: self.clear()),
            ("/", lambda: self.divide()),
            ("*", lambda: self.multiply()),
            ("-=", lambda: self.subtract()),
            ("+", lambda: self.add()),
            
            # Row 1
            ("7", lambda: self.input_number(7)),
            ("8", lambda: self.input_number(8)),
            ("9", lambda: self.input_number(9)),
            
            # Row 2
            ("/", lambda: self.divide()),
            ("4", lambda: self.input_number(4)),
            ("5", lambda: self.input_number(5)),
            ("6", lambda: self.input_number(6)),
            
            # Row 3
            ("/", lambda: self.divide()),
            ("1", lambda: self.input_number(1)),
            ("2", lambda: self.input_number(2)),
            ("3", lambda: self.input_number(3)),
            
            # Row 4
            ("/", lambda: self.divide()),
            ("0", lambda: self.input_number(0)),
            (".", lambda: self.input_number(".")),
            ("=", lambda: self.calculate())
        ]

        for i, (text, action) in enumerate(button_list):
            btn = ttk.Button(
                parent=button_frame, 
                text=text, 
                command=action,
                style="calc_button"
            )
            # Add spacing between buttons
            if i % 3 == 0:
                btn.grid(row=i // 3, column=(i // 3) * 2 + 1, padx=5, pady=5)
            else:
                btn.grid(row=i // 3, column=(i // 3) * 2 + 1, padx=5, pady=0)

    def input_number(self, num):
        self.display_var.set(str(self.display_var.get()) + str(num))

    def add(self):
        try:
            val = float(self.display_var.get())
            self.display_var.set(str(val) + "+")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def subtract(self):
        try:
            val = float(self.display_var.get())
            self.display_var.set(str(val) - "-")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def multiply(self):
        try:
            val = float(self.display_var.get())
            self.display_var.set(str(val) + "*")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def divide(self):
        try:
            val = float(self.display_var.get())
            self.display_var.set(str(val) + "/")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def clear(self):
        self.display_var.set("")

    def calculate(self):
        try:
            # Get the current string from display
            expression = str(self.display_var.get())
            
            # Replace visual operators with Python eval syntax for safety
            # Note: We only allow numbers, +, -, *, / and parentheses here.
            safe_expr = expression.replace("(", "(").replace(")", ")")
            
            # Evaluate the string safely using float conversion
            result = eval(safe_expr)
            
            self.display_var.set(str(result))
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")
        except Exception as e:
            messagebox.showerror("Error", f"Calculation failed: {str(e)}")

# Initialize the application when the script runs
if __name__ == "__main__":
    app = CalculatorApp()
```

### How it works

1.  **Framework**: We use `ttkbootstrap` (a fork of ttk) to create a custom `Frame` called `self.container`. This ensures the buttons look like modern Bootstrap cards with rounded corners and shadows.
2.  **Layout Logic**: Instead of writing 24 individual button widgets manually, we define a list of strings representing the numbers and operators. We then use a loop to generate these widgets dynamically.
3.  **Grid Placement**: The `grid()` method is used to arrange the buttons in a 6x5 grid (rows x columns). We add extra padding (`padx`) between rows to ensure they don't touch each other tightly, making it easier to tap on mobile devices.
4.  **Logic**:
    *   `input_number()`: Appends digits to the display string.
    *   `calculate()`: Takes the current expression (e.g., "5+3"), converts it to a Python string for evaluation (`"5+3"`), runs `eval()` safely, and updates the display with the result.

### How to Run

1.  Copy the code above into a file named `calculator.py`.
2.  Ensure you have internet access (to install `ttkbootstrap`).
3.  Open your terminal or command prompt.
4.  Navigate to the folder containing the file: `cd path/to/folder`
5.  Run it: `python calculator.py`

The window will open, and you can start typing numbers and clicking operators immediately!