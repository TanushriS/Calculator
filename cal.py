import tkinter as tk

class Calculator:
    def __init__(self, window):
        self.window = window
        self.window.title("My Calculator")
        window.geometry("545x600")
        window.configure(bg="#fccafc")  

        # Title Label
        title_label = tk.Label(self.window, text="My Calculator", bg="#fccafc", fg="#000000", font=("Helvetica", 28))
        title_label.grid(row=0, column=0, columnspan=4, pady=20)

        # Updated Entry Box
        self.entry = tk.Entry(self.window, width=50, borderwidth=5, font=("Helvetica", 30), bg="#FFFFFF", fg="#000000")
        self.entry.grid(row=1, column=0, columnspan=4, padx=20, pady=20)

        # Button configuration
        button_config = {
            'bg': '#4a9ecf', 
            'fg': '#FFFFFF', 
            'font': ('Helvetica', 20),
            'padx': 20,
            'pady': 20
        }

        # Button creation function
        def create_button(text, row, column, command):
            button = tk.Button(self.window, text=text, command=command, **button_config)
            button.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)
            return button

        # Create buttons
        create_button("1", 2, 0, lambda: self.click_button("1"))
        create_button("2", 2, 1, lambda: self.click_button("2"))
        create_button("3", 2, 2, lambda: self.click_button("3"))
        create_button("+", 2, 3, lambda: self.click_button("+"))

        create_button("4", 3, 0, lambda: self.click_button("4"))
        create_button("5", 3, 1, lambda: self.click_button("5"))
        create_button("6", 3, 2, lambda: self.click_button("6"))
        create_button("-", 3, 3, lambda: self.click_button("-"))

        create_button("7", 4, 0, lambda: self.click_button("7"))
        create_button("8", 4, 1, lambda: self.click_button("8"))
        create_button("9", 4, 2, lambda: self.click_button("9"))
        create_button("*", 4, 3, lambda: self.click_button("*"))

        create_button("0", 5, 0, lambda: self.click_button("0"))
        create_button(".", 5, 1, lambda: self.click_button("."))
        create_button("=", 5, 2, lambda: self.click_button("="))
        create_button("/", 5, 3, lambda: self.click_button("/"))

        # Clear button
        clear_button = tk.Button(self.window, text="Clear", command=self.clear, bg="#FF5722", fg="#FFFFFF", font=("Helvetica", 20), padx=20, pady=20)
        clear_button.grid(row=6, column=0, columnspan=4, pady=20)

        # Configure grid weights for responsive design
        for i in range(7):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(i, weight=1)

    def click_button(self, button):
        if button == '=':
            try:
                result = str(eval(self.entry.get()))  # eval will evaluate the text like 2*2,3+6
                self.entry.delete(0, tk.END)  # index of the last of widget
                self.entry.insert(tk.END, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, button)

    def clear(self):
        self.entry.delete(0, tk.END)

window = tk.Tk()
calculator = Calculator (window)
window.mainloop()