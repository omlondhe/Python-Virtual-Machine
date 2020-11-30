from tkinter import *
import math
global inc


def call(event):
    s1=str(entry.get())
    if event == "=":
        entry.delete(0, len(entry.get()))
        entry.insert(0, eval(s1))
    elif event == "√":
        entry.delete(0, len(entry.get()))
        entry.insert(0,math.sqrt(float(s1)))
    elif event == "pow":
        en = float(entry.get())
        entry.delete(0, END)
        entry.insert(0, math.pow(en, 2))

    elif event == "1/":
        en = float(entry.get())
        entry.delete(0, END)
        entry.insert(0, 1/en)
    elif event == "x":
        en = int(entry.get().__len__())
        entry.delete(en-1,END)

    elif event == "ce":
        if entry.cget('state') == DISABLED:
            entry.config(state=NORMAL)
        else:
            entry.config(state=DISABLED)
    elif event == "+/-":
        en = entry.get()
        if en[0].isnumeric():
            en1 = entry.get()
            entry.delete(0,END)
            entry.insert(0,'-')
            entry.insert(1,en1)
        if en[0].__contains__("-"):
            entry.delete(0,1)
    else:
        s1 = s1 + event
        entry.delete(0,len(entry.get()))
        entry.insert(0,s1)


def delete(event):
    entry.delete(0, END)


base = Tk()
base.geometry("320x500")
base.title("Calculator")
entry=Entry(base,font="Arial 30 italic",bd=2,relief=GROOVE,width=14, justify=RIGHT)
btn=Button(base,text="%",font="Arial 9 bold",height=3,width=9,command=lambda :call('%'),bd=3)
btn1=Button(base,text="√x",height=3,width=9,bd=3,command=lambda :call('√'))
btn2=Button(base,text="x2",height=3,width=9,command=lambda :call('pow'),bd=3)
btn3=Button(base,text="1/x",height=3,width=9,command=lambda :call('1/'),bd=3)
btn4=Button(base,text="CE",height=3,width=9,command=lambda :call('ce'),bd=3)
btn5=Button(base,text="C",height=3,width=9,command=lambda :delete('c'),bd=3)
btn6=Button(base,text="x",height=3,width=9,command=lambda :call('x'),bd=3)
btn7=Button(base,text="÷ ",height=3,width=9,command=lambda :call('/ '),bd=3)
btn8=Button(base,text="7",height=3,width=9,command=lambda :call('7'),bd=3)
btn9=Button(base,text="8",height=3,width=9,command=lambda :call('8'),bd=3)
btn10=Button(base,text="9",height=3,width=9,command=lambda :call('9'),bd=3)
btn11=Button(base,text="X",height=3,width=9,command=lambda :call('*'),bd=3)
btn12=Button(base,text="4",height=3,width=9,command=lambda :call('4'),bd=3)
btn13=Button(base,text="5",height=3,width=9,command=lambda :call('5'),bd=3)
btn14=Button(base,text="6",height=3,width=9,command=lambda :call('6'),bd=3)
btn15=Button(base,text="-",height=3,width=9,command=lambda :call('-'),bd=3)
btn16=Button(base,text="1",height=3,width=9,command=lambda :call('1'),bd=3)
btn17=Button(base,text="2",height=3,width=9,command=lambda :call('2'),bd=3)
btn18=Button(base,text="3",height=3,width=9,command=lambda :call('3'),bd=3)
btn19=Button(base,text="+",height=3,width=9,command=lambda :call('+'),bd=3)
btn20=Button(base,text="+/-",height=3,width=9,command=lambda :call('+/-'),bd=3)
btn21=Button(base,text="0",height=3,width=9,command=lambda :call('0'),bd=3)
btn22=Button(base,text=".",height=3,width=9,command=lambda :call('.'),bd=3)
btn23=Button(base,text="=",height=3,width=9,command=lambda :call('='),bd=3)

entry.place(x=3,y=30)
btn.place(x=9,y=150)
btn1.place(x=84,y=150)
btn2.place(x=160,y=150)
btn3.place(x=235,y=150)
btn4.place(x=9,y=208)
btn5.place(x=84,y=208)
btn6.place(x=160,y=208)
btn7.place(x=235,y=208)
btn8.place(x=9,y=266)
btn9.place(x=84,y=266)
btn10.place(x=160,y=266)
btn11.place(x=235,y=266)
btn12.place(x=9,y=324)
btn13.place(x=84,y=324)
btn14.place(x=160,y=324)
btn15.place(x=235,y=324)
btn16.place(x=9,y=382)
btn17.place(x=84,y=382)
btn18.place(x=160,y=382)
btn19.place(x=235,y=382)
btn20.place(x=9,y=440)
btn21.place(x=84,y=440)
btn22.place(x=160,y=440)
btn23.place(x=235,y=440)
base.mainloop()

