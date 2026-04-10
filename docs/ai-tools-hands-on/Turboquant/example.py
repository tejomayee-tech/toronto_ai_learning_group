import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class CalculatorApp:
    def __init__(self):
        # Initialize style and window
        self.root = ttk.Window(themename="darkly") # modern dark theme
        self.root.title("Modern Calculator")
        self.root.geometry("350x500")
        
        self.container = ttk.Frame(self.root, padding=20)
        self.container.pack(fill=BOTH, expand=YES)
        
        # --- Display Screen ---
        self.display_var = tk.StringVar(value="")
        self.display_entry = ttk.Entry(
            self.container, 
            textvariable=self.display_var, 
            font=("Helvetica", 20), 
            justify="right",
            state="readonly" # Prevents typing via keyboard for simplicity
        )
        self.display_entry.pack(fill=X, pady=20)

        # --- Buttons Grid ---
        self.button_frame = ttk.Frame(self.container)
        self.button_frame.pack(fill=BOTH, expand=YES)
        self.create_buttons()

    def create_buttons(self):
        # (Text, Row, Column, Bootstyle)
        buttons = [
            ('C', 0, 0, DANGER), ('/', 0, 1, INFO), ('*', 0, 2, INFO), ('-', 0, 3, INFO),
            ('7', 1, 0, SECONDARY), ('8', 1, 1, SECONDARY), ('9', 1, 2, SECONDARY), ('+', 1, 3, INFO),
            ('4', 2, 0, SECONDARY), ('5', 2, 1, SECONDARY), ('6', 2, 2, SECONDARY), ('=', 2, 3, SUCCESS),
            ('1', 3, 0, SECONDARY), ('2', 3, 1, SECONDARY), ('3', 3, 2, SECONDARY), 
            ('0', 4, 0, SECONDARY), ('.', 4, 1, SECONDARY)
        ]

        # Configure grid weights so buttons expand
        for i in range(4):
            self.button_frame.columnconfigure(i, weight=1)
        for i in range(5):
            self.button_frame.rowconfigure(i, weight=1)

        for (text, row, col, style) in buttons:
            btn = ttk.Button(
                self.button_frame, 
                text=text, 
                bootstyle=style,
                command=lambda t=text: self.on_button_click(t)
            )
            # Span the equals button or keep it standard
            if text == '=':
                btn.grid(row=row, column=col, rowspan=3, sticky="nsew", padx=2, pady=2)
            else:
                btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

    def on_button_click(self, char):
        if char == "C":
            self.display_var.set("")
        elif char == "=":
            self.calculate()
        else:
            # Append the character to the current display
            current = self.display_var.get()
            self.display_var.set(current + str(char))

    def calculate(self):
        try:
            # Basic sanitization: only allow math characters
            expression = self.display_var.get()
            # eval() processes the string as Python code
            result = eval(expression)
            self.display_var.set(str(result))
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            self.display_var.set("")
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            self.display_var.set("")

if __name__ == "__main__":
    app = CalculatorApp()
    app.root.mainloop()