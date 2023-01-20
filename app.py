from tkinter import *
import tkinter.messagebox

window = Tk()
window.title("Arm")
window.geometry("500x300")
def showmsg():
    Label(text=txt.get() , fg="pink").pack()

def NewWindow():
    window2 = Tk()
    window2 = (NewWindow)
    window.geometry("500x300")
def showAbout():
    tkinter.messagebox.showwarning("เกี่ยวกับผู้พัฒนา","ผู้พัฒนา นาย เกียรติศักดิ์ วชิรศิริกุล www.vk.com")
def exit():
    confirm = tkinter.messagebox.askquestion("ยืนยัน","คุณต้องการออกโปรเเกรม?")
    if(confirm == "yes"):
        window.destroy()

#เมนูย่อย
MenuItem = Menu()
MenuItem.add_command(label="New window",command=NewWindow)
MenuItem.add_command(label="open File")
MenuItem.add_command(label="About",command=showAbout)
MenuItem.add_command(label="Exit",command=exit)
#เมนูหลัก
MyMenu=Menu()
MyMenu.add_cascade(label="File",menu=MenuItem)
MyMenu.add_cascade(label="Edit")
MyMenu.add_cascade(label="About")
window.config(menu=MyMenu)


txt = StringVar()
mytext = Entry(window,textvariable=txt).pack()
print(txt)


Button(window,text="บันทึก" ,fg="green",command=showmsg).place(x=480,y=50)
window.mainloop()