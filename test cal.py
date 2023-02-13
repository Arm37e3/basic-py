from tkinter import *
Calculator = Tk()
Calculator.title("Calculator")

content = ""
txt_input = StringVar(value="")

content2 = ""
txt_input2 = StringVar(value="")

content3 = ""
txt_input3 = StringVar(value="")
total = ""
operators = ""
def _plus():
    global txt_input, txt_input2, txt_input3,operators,total
   
    operators="+"
    total = display1.get()+operators+ display2.get()
    print(total)
    
    ans = eval(total)
    txt_input3.set(ans)
    
    
def _minus():
    global txt_input, txt_input2, txt_input3,operators,total
   
    operators="-"
    total = display1.get()+operators+ display2.get()
    print(total)
    
    ans = eval(total)
    txt_input3.set(ans)    
    
def _multiply():
    global txt_input, txt_input2, txt_input3,operators,total
   
    operators="*"
    total = display1.get()+operators+ display2.get()
    print(total)
    
    ans = eval(total)
    txt_input3.set(ans)     
    
def _divide():
    global txt_input, txt_input2, txt_input3,operators,total
   
    operators="/"
    total = display1.get()+operators+ display2.get()
    print(total)
    
    ans = eval(total)
    txt_input3.set(ans) 
    
    
display1 = Entry(font=('arial',30,'bold'),textvariable=txt_input, fg="white" , bg="pink" )
display1.grid(columnspan=4)
display2 = Entry(font=('arial',30,'bold'),textvariable=txt_input2, fg="white" , bg="red" )
display2.grid(columnspan=4)

display3 = Entry(font=('arial',30,'bold'),textvariable=txt_input3, fg="white" , bg="yellow" )
display3.grid(columnspan=4)

    
btn_p1 = Button(fg="black",font=("arial",30,"bold ") ,text="+",padx=30,pady=15,command=_plus).grid(row=3,column=1)
btn_p2 = Button(fg="black",font=("arial",30,"bold ") ,text="-",padx=30,pady=15,command=_minus).grid(row=3,column=2)
btn_p3 = Button(fg="black",font=("arial",30,"bold ") ,text="x",padx=30,pady=15,command=_multiply).grid(row=3,column=3)
btn_p4 = Button(fg="black",font=("arial",30,"bold ") ,text="/",padx=30,pady=15,command=_divide).grid(row=3,column=4)

Calculator.mainloop()
