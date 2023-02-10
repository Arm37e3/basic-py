from tkinter import *

window = Tk()
window.geometry("530x330")
window.maxsize(530,330)
window.minsize(530,330)
window.title("Calculate")





display = Entry(font=('arial',16))

in1 = Text(window,width=10,height=1)
in1.place(x=250,y=70)
in2 = Text(window,width=10,height=1)
in2.place(x=250,y=90)
op = Text(window,width=10,height=1)
op.place(x=250,y=120)

btnmultiply = Button(window,width=1,height=1,font=('arial',7,'bold'),text='x',command=lambda:btn).place(x=290,y=160)
btnplus = Button (window,width=1,height=1,font=('arial',7,'bold'),text='+',command=lambda:btn).place(x=250,y=160)
btndivide = Button(window,width=1,height=1,font=('arial',7,'bold'), text="÷",command=lambda:btn).place(x=310,y=160)
btnsubtract = Button(window,width=1,height=1,font=('arial',7,'bold'), text="-",command=lambda:btn).place(x=270,y=160)


Button(window,text="คำนวณ",fg='green').place(x=230,y=200)
Button(window,text="Clear",fg='red').place(x=290,y=200)

window.mainloop()

