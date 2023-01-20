from tkinter import *
from googletrans import Translator


def translate():
    msg = texteg.get('1.0','end-1c')
    translator = Translator()
    output = translator.translate(text=msg, src='en', dest='th')                         
    # print("output")
    textth.insert('end',output.text)

def clear():
    texteg.delete(1.0,'end')
    textth.delete(1.0,'end')

#windows
windows = Tk()
windows.title("google Translate (En-TH) ")
windows.geometry("530x330")
windows.maxsize(530,330)
windows.minsize(530,330)


#winget
label = Label (text="Englist - Thai", font = ('Arial',25,'bold'))
label.place(x=160, y=20)

#กล่องข้อความภาษาอังกฤษ 
texteg = Text(windows,width=30,height=10)
texteg.place(x=10,y=70)

#กล่องข้อความภาษาไทย
textth = Text(windows,width=30,height=10)
textth.place(x=270,y=70)

#widget_button
translate_btn = Button(windows,text=('translate'),command=translate)
translate_btn.place(x=210,y=260)

clear_btn = Button(windows,text=('Clear'),command=clear)
clear_btn.place(x=275,y=260)






windows.mainloop()
