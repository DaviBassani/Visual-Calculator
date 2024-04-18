import customtkinter as ctk
from tkinter import font
from functools import partial

def create_button(parent, text, command, row, column, color='#000000', rowspan=1, columnspan=1):
    """Helper function to create a button with specified properties."""
    custom_font = ctk.CTkFont(family="Arial", size=14, weight="bold")
    btn = ctk.CTkButton(parent, text=text, command=command, fg_color=color, font=custom_font, width=100, height=60)
    btn.grid(row=row, column=column, sticky='nsew', padx=2, pady=2, rowspan=rowspan, columnspan=columnspan)
    return btn

def enter_number(number):
    """Append a number or decimal point to the current expression."""
    current = equation.get()
    number = str(number)  # Ensure number is a string
    if current == "0":
        equation.set(number)
    else:
        equation.set(current + number)

def set_operation(operator):
    """Set the operation for calculation."""
    current = equation.get()
    if current and current[-1] in "+-*/":
        current = current[:-1]
    equation.set(current + operator)

def clear():
    """Clear the current expression."""
    equation.set("0")

def calculate():
    """Evaluate the expression and handle errors."""
    try:
        result = eval(equation.get())
        equation.set(str(result))
    except ZeroDivisionError:
        equation.set("Error! Division by zero.")
    except Exception:
        equation.set("Unknown Error!")

# Create the main window
window = ctk.CTk()
window.title('Calculadora')
window.geometry('300x400')

# Grid configuration for equal distribution
for i in range(5):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# Entry widget for displaying equations and results
equation = ctk.StringVar(value="0")
entry = ctk.CTkEntry(window, textvariable=equation, width=280, height=50, corner_radius=10)
entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

# Buttons for the calculator
create_button(window, "C", clear, 1, 0, "#FF6666")
create_button(window, "/", partial(set_operation, '/'), 1, 1)
create_button(window, "x", partial(set_operation, '*'), 1, 2)
create_button(window, "-", partial(set_operation, '-'), 1, 3)
create_button(window, "+", partial(set_operation, '+'), 2, 3)
numbers = [(7, 2, 0), (8, 2, 1), (9, 2, 2),
           (4, 3, 0), (5, 3, 1), (6, 3, 2),
           (1, 4, 0), (2, 4, 1), (3, 4, 2),
           (0, 5, 1)]
for num, r, c in numbers:
    create_button(window, str(num), partial(enter_number, num), r, c, "#303030")
create_button(window, ".", lambda: enter_number('.'), 5, 0, "#040338")
create_button(window, "=", calculate, 4, 3, "#00CC66", rowspan=2)

window.mainloop()
