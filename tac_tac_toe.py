from tkinter import *
from tkinter.messagebox import askyesno, showinfo, showerror, showwarning


count = 1
p1_score = 0
p2_score = 0
draw = 0


def start(event):
    print(event)
    ayn = askyesno("TIC TAC TOE", "Do you want to Start the game ? ")
    if ayn == YES:
        root.geometry("250x450")
        save()
    else:
        pass


def save():
    def click(event):
        click1(event)

    player1 = p1.get().capitalize()
    player2 = p2.get().capitalize()
    l1.destroy()
    l2.destroy()
    p1.destroy()
    l3.destroy()
    p2.destroy()
    save_info.destroy()

    def score():
        live_score = Label(root, text="Live Score : ", font="lucida 11")
        live_score.place(x=5, y=40)
        p1_name = Label(root, text=f"{player1} :", font="lucida 11")
        p1_name.place(x=5, y=65)
        score1 = Label(root, font="lucida 10", text=p1_score)
        score1.place(x=100, y=65)
        p2_name = Label(root, text=f"{player2} :", font="lucida 11")
        p2_name.place(x=5, y=90)
        score2 = Label(root, font="lucida 10", text=p2_score)
        score2.place(x=100, y=90)
        tie = Label(root, text="Match Draw :", font="lucida 11")
        tie.place(x=5, y=115)
        tie_score = Label(root, font="lucida 10", text=draw)
        tie_score.place(x=100, y=115)

    score()
    box1 = Button(root, padx=30, pady=22, bd=4, relief=GROOVE, text="  ")
    box1.place(x=12, y=148)
    box1.bind("<Double-1>", click)
    box1.bind("<Key>", click)
    box2 = Button(root, padx=30, pady=22, bd=4, relief=GROOVE, text="  ")
    box2.place(x=89, y=148)
    box2.bind("<Double-1>", click)
    box2.bind("<Key>", click)
    box3 = Button(root, padx=30, pady=22, bd=4, relief=GROOVE, text="  ")
    box3.place(x=166, y=148)
    box3.bind("<Double-1>", click)
    box3.bind("<Key>", click)
    box4 = Button(root, padx=30, pady=22, bd=4, relief=GROOVE, text="  ")
    box4.place(x=12, y=218)
    box4.bind("<Double-1>", click)
    box4.bind("<Key>", click)
    box5 = Button(root, padx=30, pady=22, bd=4, relief=GROOVE, text="  ")
    box5.place(x=89, y=218)
    box5.bind("<Double-1>", click)
    box5.bind("<Key>", click)
    box6 = Button(root, padx=30, pady=22, bd=4, relief=GROOVE, text="  ")
    box6.place(x=166, y=218)
    box6.bind("<Double-1>", click)
    box6.bind("<Key>", click)
    box7 = Button(root, padx=30, pady=22, bd=4, relief=GROOVE, text="  ")
    box7.place(x=12, y=288)
    box7.bind("<Double-1>", click)
    box7.bind("<Key>", click)
    box8 = Button(root, padx=30, pady=22, bd=4, relief=GROOVE, text="  ")
    box8.place(x=89, y=288)
    box8.bind("<Double-1>", click)
    box8.bind("<Key>", click)
    box9 = Button(root, padx=30, pady=22, bd=4, relief=GROOVE, text="  ")
    box9.place(x=166, y=288)
    box9.bind("<Double-1>", click)
    box9.bind("<Key>", click)
    reset = Button(root, padx=15, pady=7, bd=3, relief=RAISED, text="Reset")
    reset.place(x=110, y=375)
    reset.bind("<Button-1>", click)
    reset.bind("<Key>", click)
    quit_game = Button(root, padx=15, pady=7, bd=3, relief=RAISED, text="Quit")
    quit_game.place(x=180, y=375)
    quit_game.bind("<Button-1>", click)
    quit_game.bind("<Key>", click)

    def click1(event):
        global count, p1_score, p2_score, draw
        txt = event.widget.cget("text")
        if txt == "Reset":
            ayn = askyesno("TIC TAC TOE", "Do you want to reset the values ? ")
            if ayn == YES:
                box1.config(text="  ", padx=30, pady=22)
                box2.config(text="  ", padx=30, pady=22)
                box3.config(text="  ", padx=30, pady=22)
                box4.config(text="  ", padx=30, pady=22)
                box5.config(text="  ", padx=30, pady=22)
                box6.config(text="  ", padx=30, pady=22)
                box7.config(text="  ", padx=30, pady=22)
                box8.config(text="  ", padx=30, pady=22)
                box9.config(text="  ", padx=30, pady=22)
            else:
                pass
        elif txt == "Quit":
            showwarning("TIC TAC TOE", "By doing this operation the game will be exited")
            showinfo("TIC TAC TOE", "The score is :                                                    \n\n"
                     f"{player1} : {p1_score}                                                            \n"
                     f"{player2} : {p2_score}                                                            \n"
                     f"Ties      : {draw}                                                                  ")
            if p1_score == p2_score:
                showinfo("TIC TAC TOE", f"It is tie Between {player1} and {player2}                        ")
            elif p1_score < p2_score:
                showinfo("TIC TAC TOE", f"{player2} Won                                                    ")
            elif p1_score > p2_score:
                showinfo("TIC TAC TOE", f"{player1} Won                                                    ")
            root.quit()
            exit()
        elif txt == "  ":
            if count % 2 != 0:
                event.widget.config(text="O", padx=29)
                count = count + 1
            else:
                event.widget.config(text="X", padx=30)
                count = count + 1
        elif txt == "O" or txt == "X":
            showerror("TIC TAC TOE", "You cannot click on Pre-existing Values")

        if box1.cget("text") == box2.cget("text") == box3.cget("text") == "O" or \
                box1.cget("text") == box4.cget("text") == box7.cget("text") == "O" or \
                box2.cget("text") == box5.cget("text") == box8.cget("text") == "O" or \
                box3.cget("text") == box6.cget("text") == box9.cget("text") == "O" or \
                box4.cget("text") == box8.cget("text") == box9.cget("text") == "O" or \
                box1.cget("text") == box5.cget("text") == box9.cget("text") == "O" or \
                box4.cget("text") == box5.cget("text") == box6.cget("text") == "O" or \
                box3.cget("text") == box5.cget("text") == box7.cget("text") == "O":
            p1_score = p1_score + 1
            score()
            showinfo("TIC TAC TOE", f"Congratulations {player1}, You Won !!!")
        elif box1.cget("text") == box2.cget("text") == box3.cget("text") == "X" or \
                box1.cget("text") == box4.cget("text") == box7.cget("text") == "X" or \
                box2.cget("text") == box5.cget("text") == box8.cget("text") == "X" or \
                box3.cget("text") == box6.cget("text") == box9.cget("text") == "X" or \
                box4.cget("text") == box8.cget("text") == box9.cget("text") == "X" or \
                box1.cget("text") == box5.cget("text") == box9.cget("text") == "X" or \
                box4.cget("text") == box5.cget("text") == box6.cget("text") == "X" or \
                box3.cget("text") == box5.cget("text") == box7.cget("text") == "X":
            p2_score = p2_score + 1
            score()
            showinfo("TIC TAC TOE", f"Congratulations {player2}, You Won !!!")
        elif box1.cget("text") != "  " and box2.cget("text") != "  " and box3.cget("text") != "  " and \
                box4.cget("text") != "  " and box5.cget("text") != "  " and box6.cget("text") != "  " and \
                box7.cget("text") != "  " and box8.cget("text") != "  " and box9.cget("text") != " ":
            draw = draw + 1
            score()
            showinfo("TIC TAC TOE", f"Oh ! no it's a Tie between {player1} and {player2} !!!              ")


root = Tk()
root.title("Tic Tac Toe")
root.geometry("300x225")

Label(root, text="TIC TAC TOE", font="lucida 21 bold").place(x=0, y=0)

l1 = Label(root, text="Enter Player names: ", font="lucida 11")
l1.place(x=5, y=50)
l2 = Label(root, text="Player 1 : ", font="lucida 11")
l2.place(x=5, y=75)
p1 = Entry(root, font="lucida 10")
p1.place(x=75, y=75)
l3 = Label(root, text="Player 2 : ", font="lucida 11")
l3.place(x=5, y=100)
p2 = Entry(root, font="lucida 10")
p2.place(x=75, y=100)

save_info = Button(root, text="Save", padx=10, pady=4, bd=2, relief=RIDGE)
save_info.place(x=5, y=140)
save_info.bind("<Button-1>", start)


root.mainloop()
