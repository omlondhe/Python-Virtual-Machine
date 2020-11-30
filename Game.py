from tkinter import *
import subprocess
import _thread


def open_math_game():
    def math_thread(p, q):
        subprocess.call(["Python", "math_game.py"])

    _thread.start_new_thread(math_thread, (0, 1))


def open_ttt():
    def ttt_thread(p, q):
        subprocess.call(["Python", "tac_tac_toe.py"])

    _thread.start_new_thread(ttt_thread, (0, 1))


root = Tk()
root.title("Games")
root.geometry("700x300")

choose = Label(text="What do you want to Play ?", font=("comic sans", 21))
choose.place(x=100, y=10)

math_img = PhotoImage(file=r"math.png", height=200, width=200)
math = Button(image=math_img, bd=0, command=open_math_game)
math.place(x=100, y=51)
math_lbl = Label(text="Math Game", font=("comic sans", "15"))
math_lbl.place(x=150, y=250)

ttt = PhotoImage(file=r"ttt.png")
tttg = Button(image=ttt, bd=0, command=open_ttt)
tttg.place(x=420, y=51)
ttt_lbl = Label(text="Tic Tac Toe", font=("comic sans", "15"))
ttt_lbl.place(x=450, y=250)

root.mainloop()
