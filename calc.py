import customtkinter as ctk
from tkinter import StringVar
from functools import partial

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Calculadora')
        self.master.geometry('300x400')

        # Grid configuration for equal distribution
        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)

        # Entry widget for displaying equations and results
        self.equation = StringVar(value="0")
        self.entry = ctk.CTkEntry(self.master, textvariable=self.equation, width=280, height=50, corner_radius=10)
        self.entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Buttons for the calculator
        self.create_button("C", self.clear, 1, 0, "#FF6666")
        operators = [("/", 1, 1), ("*", 1, 2), ("-", 1, 3), ("+", 2, 3)]
        for op, r, c in operators:
            self.create_button(op, partial(self.set_operation, op), r, c)

        numbers = [(7, 2, 0), (8, 2, 1), (9, 2, 2),
                   (4, 3, 0), (5, 3, 1), (6, 3, 2),
                   (1, 4, 0), (2, 4, 1), (3, 4, 2),
                   (0, 5, 1)]
        for num, r, c in numbers:
            self.create_button(str(num), partial(self.enter_number, num), r, c, "#303030")

        self.create_button(".", lambda: self.enter_number('.'), 5, 0, "#040338")
        self.create_button("=", self.calculate, 4, 3, "#00CC66", rowspan=2)

    def create_button(self, text, command, row, column, color='#000000', rowspan=1, columnspan=1):
        """Helper function to create a button with specified properties."""
        custom_font = ctk.CTkFont(family="Arial", size=14, weight="bold")
        btn = ctk.CTkButton(self.master, text=text, command=command, fg_color=color, font=custom_font, width=100, height=60)
        btn.grid(row=row, column=column, sticky='nsew', padx=2, pady=2, rowspan=rowspan, columnspan=columnspan)

    def enter_number(self, number):
        """Append a number or decimal point to the current expression."""
        current = self.equation.get()
        number = str(number)  # Ensure number is a string
        if current == "0":
            self.equation.set(number)
        else:
            self.equation.set(current + number)

    def set_operation(self, operator):
        """Set the operation for calculation."""
        current = self.equation.get()
        if current and current[-1] in "+-*/":
            current = current[:-1]
        self.equation.set(current + operator)

    def clear(self):
        """Clear the current expression."""
        self.equation.set("0")

    def calculate(self):
        """Evaluate the expression and handle errors."""
        try:
            result = eval(self.equation.get())
            self.equation.set(str(result))
        except ZeroDivisionError:
            self.equation.set("Error! Division by zero.")
        except Exception:
            self.equation.set("Unknown Error!")

if __name__ == "__main__":
    root = ctk.CTk()
    app = CalculatorApp(root)
    root.mainloop()
