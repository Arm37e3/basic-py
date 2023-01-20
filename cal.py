import tkinter as tk

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operator.get()
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    result_label.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Calculator")

num1_label = tk.Label(root, text="Number 1")
num1_label.grid(row=0, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

num2_label = tk.Label(root, text="Number 2")
num2_label.grid(row=1, column=0)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

operator = tk.StringVar()
operator.set("+")

addition_button = tk.Radiobutton(root, text="+", variable=operator, value="+")
addition_button.grid(row=2, column=0, sticky="w")

subtraction_button = tk.Radiobutton(root, text="-", variable=operator, value="-")
subtraction_button.grid(row=2, column=1, sticky="w")

multiplication_button = tk.Radiobutton(root, text="*", variable=operator, value="*")
multiplication_button.grid(row=2, column=2, sticky="w")

division_button = tk.Radiobutton(root, text="/", variable=operator, value="/")
division_button.grid(row=2, column=3, sticky="w")

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
