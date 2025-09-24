import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculator():
    # Create main window
    window = tk.Tk()
    window.title("Calculadora Simples")
    window.geometry("330x460")
    window.configure(bg='#f0f0f0')
    window.resizable(False, False)
    
    # Create display
    display_var = tk.StringVar()
    display_var.set("0")
    
    display = tk.Entry(window, textvariable=display_var, font=('Arial', 24), bd=10, 
                      insertwidth=4, width=14, justify='right', state='disabled')
    display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    
    # Variables to store calculation values
    first_number = [0]
    operation = [None]
    should_reset = [True]
    
    # Function to update display
    def add_digit(digit):
        if should_reset[0]:
            display_var.set("")
            should_reset[0] = False
        
        current = display_var.get()
        if current == "0" and digit != ".":
            current = ""
        
        # Prevent multiple decimal points
        if digit == "." and "." in current:
            return
            
        display_var.set(current + digit)
    
    # Function to clear display (C)
    def clear():
        display_var.set("0")
        first_number[0] = 0
        operation[0] = None
        should_reset[0] = True
        
    # Function to clear entry (CE)
    def clear_entry():
        display_var.set("0")
        should_reset[0] = True
    
    # Function to perform operation
    def set_operation(op):
        try:
            if operation[0] is not None:
                calculate()
            
            first_number[0] = float(display_var.get())
            operation[0] = op
            should_reset[0] = True
        except ValueError:
            display_var.set("Erro")
            should_reset[0] = True
    
    # Function to calculate result
    def calculate():
        if operation[0] is None:
            return
            
        try:
            second_number = float(display_var.get())
            result = 0
            
            if operation[0] == "+":
                result = first_number[0] + second_number
            elif operation[0] == "-":
                result = first_number[0] - second_number
            elif operation[0] == "*":
                result = first_number[0] * second_number
            elif operation[0] == "/":
                if second_number == 0:
                    messagebox.showerror("Erro", "Não é possível dividir por zero!")
                    clear()
                    return
                result = first_number[0] / second_number
            
            # Format result to avoid unnecessary decimal places
            if result == int(result):
                display_var.set(str(int(result)))
            else:
                display_var.set(str(result))
                
            operation[0] = None
            should_reset[0] = True
            
        except ValueError:
            display_var.set("Erro")
            should_reset[0] = True
    
    # Create buttons
    button_style = {'font': ('Arial', 14), 'width': 5, 'height': 2, 'bd': 3, 'relief': 'raised'}
    
    # Number buttons
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
        ('0', 4, 0), ('.', 4, 1)
    ]
    
    for (text, row, col) in buttons:
        button = tk.Button(window, text=text, bg='#ffffff', **button_style,
                          command=lambda t=text: add_digit(t))
        button.grid(row=row, column=col, padx=5, pady=5)
    
    # Operation buttons
    operations = [
        ('/', 1, 3), ('*', 2, 3), ('-', 3, 3), ('+', 4, 3)
    ]
    
    for (text, row, col) in operations:
        button = tk.Button(window, text=text, bg='#f0ad4e', **button_style,
                          command=lambda t=text: set_operation(t))
        button.grid(row=row, column=col, padx=5, pady=5)
    
    # Equal button
    equal_button = tk.Button(window, text='=', bg='#5cb85c', **button_style,
                            command=calculate)
    equal_button.grid(row=4, column=2, padx=5, pady=5)
    
    # Clear buttons
    clear_button = tk.Button(window, text='C', bg='#d9534f', **button_style,
                            command=clear)
    clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='we')
    
    # Clear Entry button
    clear_entry_button = tk.Button(window, text='CE', bg='#f0ad4e', **button_style,
                                  command=clear_entry)
    clear_entry_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky='we')
    
    # Start the main loop
    window.mainloop()
            
if __name__ == "__main__":
    calculator()
