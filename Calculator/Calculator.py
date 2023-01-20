from tkinter import *
calculator = Tk()
calculator.title("Calculator")

#เเสดงผล
display = Entry(font=('arial',30,'bold'), fg="white", bg = "#DA56F7" )
display.grid(columnspan=4)


btn7 = Button(font=('arial',30,'bold'), text="7", fg="black", padx=30, pady=15).grid(row=1, column=0)
btn8 = Button(font=('arial',30,'bold'), text="8", fg="black", padx=30, pady=15).grid(row=1, column=1)
btn9 = Button(font=('arial',30,'bold'), text="9", fg="black", padx=30, pady=15).grid(row=1, column=2)
btnC = Button(font=('arial',30,'bold'), text="C", fg="black", padx=30, pady=15).grid(row=1, column=3)
btn4 = Button(font=('arial',30,'bold'), text="4", fg="black", padx=30, pady=15).grid(row=2, column=0)
btn5 = Button(font=('arial',30,'bold'), text="5", fg="black", padx=30, pady=15).grid(row=2, column=1)
btn6 = Button(font=('arial',30,'bold'), text="6", fg="black", padx=30, pady=15).grid(row=2, column=2)
btnplus = Button(font=('arial',30,'bold'), text="+", fg="black", padx=30, pady=15).grid(row=2, column=3)
btn1 = Button(font=('arial',30,'bold'), text="1", fg="black", padx=30, pady=15).grid(row=3, column=0)
btn2 = Button(font=('arial',30,'bold'), text="2", fg="black", padx=30, pady=15).grid(row=3, column=1)
btn3 = Button(font=('arial',30,'bold'), text="3", fg="black", padx=30, pady=15).grid(row=3, column=2)
btnsubtract = Button(font=('arial',30,'bold'), text="-", fg="black", padx=30, pady=15).grid(row=3, column=3)
btndot = Button(font=('arial',30,'bold'), text=".", fg="black", padx=30, pady=15).grid(row=4, column=0)
btn0 = Button(font=('arial',30,'bold'), text="0", fg="black", padx=30, pady=15).grid(row=4, column=1)
btnmultiply = Button(font=('arial',30,'bold'), text="*", fg="black", padx=30, pady=15).grid(row=4, column=2)
btndivide = Button(font=('arial',30,'bold'), text="÷", fg="black", padx=30, pady=15).grid(row=4, column=3)
btnopen = Button(font=('arial',30,'bold'), text="(", fg="black", padx=30, pady=15).grid(row=5, column=0)
btnclose = Button(font=('arial',30,'bold'), text=")", fg="black", padx=30, pady=15).grid(row=5, column=1)
btnequal = Button(font=('arial',30,'bold'), text="=", fg="red", padx=90, pady=10).grid(row=5, column=2,columnspan=3)
calculator.mainloop()
