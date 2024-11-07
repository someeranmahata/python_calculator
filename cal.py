from tkinter import *

cal = Tk()
cal.geometry("355x330")
cal.title("Calculator")
cal.configure(bg = "black")


data = StringVar()
val = ""

display = Entry(textvariable=data ,bg = "powder blue",bd=10 ,font = "ariel 20",relief="sunken",justify="right")
display.grid(row =0,columnspan=4)

def clear():
    global val
    val = ""
    data.set(val)

def equals():
    try:
        a =eval(data.get())
        data.set(a)
    except:
        data.set("ERROR")

def buttonclick(number):
    global val
    val = val+str(number)
    data.set(val)

#making keys
b1 = Button(cal,text="9",command = lambda:buttonclick(9),font = "ariel 20 bold",bd = 12).grid(row = 1,column = 0)
b2 = Button(cal,text="8",command =lambda:buttonclick(8),font = "ariel 20 bold",bd = 12).grid(row = 1,column = 1)
b3 = Button(cal,text="7",command = lambda:buttonclick(7),font = "ariel 20 bold",bd = 12).grid(row = 1,column = 2)
b4 = Button(cal,text=" c ",command = clear,font = "ariel 20 bold",bd = 12).grid(row = 1,column = 3)

b1 = Button(cal,text="6",command =lambda:buttonclick(6),font = "ariel 20 bold",bd = 12).grid(row = 2,column = 0)
b2 = Button(cal,text="5",command = lambda:buttonclick(5),font = "ariel 20 bold",bd = 12).grid(row = 2,column = 1)
b3 = Button(cal,text="4",command = lambda:buttonclick(4),font = "ariel 20 bold",bd = 12).grid(row = 2,column = 2)
b4 = Button(cal,text=" - ",command = lambda:buttonclick('-'),font = "ariel 20 bold",bd = 12).grid(row = 2,column = 3)


b1 = Button(cal,text="3",command = lambda:buttonclick(3),font = "ariel 20 bold",bd = 12).grid(row = 3,column = 0)
b2 = Button(cal,text="2",command = lambda:buttonclick(2),font = "ariel 20 bold",bd = 12).grid(row = 3,column = 1)
b3 = Button(cal,text="1",command = lambda:buttonclick(1),font = "ariel 20 bold",bd = 12).grid(row = 3,column = 2)
b4 = Button(cal,text=" +",command =lambda:buttonclick('+'),font = "ariel 20 bold",bd = 12).grid(row = 3,column = 3)

b1 = Button(cal,text="0",command = lambda:buttonclick(0),font = "ariel 20 bold",bd = 12).grid(row = 4,column = 0)
b2 = Button(cal,text=" /",command = lambda:buttonclick('/'),font = "ariel 20 bold",bd = 12).grid(row = 4,column = 1)
b3 = Button(cal,text=" ",command = lambda:buttonclick(''),font = "ariel 20 bold",bd = 12).grid(row = 4,column = 2)
b4 = Button(cal,text=" =",command = equals,font = "ariel 20 bold",bd = 12,).grid(row =4,column = 3)

cal.mainloop()