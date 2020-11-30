import datetime
from tkinter import *


def fun():
    dt = Label(root, text=datetime.date.today(), font=11)
    dt.grid(row=0, column=1)
    time = Label(root, text=datetime.datetime.now().strftime("%H:%M:%S"), bg="black", fg="white", borderwidth=5,
                 relief='sunken', font="monotype 42 bold")
    time.grid(row=7, column=1)
    time.after(100, fun)


root = Tk()
root.geometry()
root.title("Clock")

fun()
root.mainloop()
