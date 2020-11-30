from tkinter import *
from tkinter.messagebox import askquestion as ask_que
import subprocess
import os
import _thread


def open_music_player():
    question = ask_que("Media Player", "Do you want to use pyMusic Player ?")
    print(question)
    if question == "yes":
        def mp_thread(p, q):
            subprocess.call(["python", "Music_Player.py"])

        _thread.start_new_thread(mp_thread, (0, 1))
    else:
        os.system("explorer.exe shell:AppsFolder\\Microsoft.ZuneMusic_8wekyb3d8bbwe!Microsoft.ZuneMusic")


def open_video_player():
    def vp_thread(p, q):
        subprocess.call(["Python", "Video_player.py"])

    _thread.start_new_thread(vp_thread, (0, 1))


root = Tk()
root.title("Media Player")
root.geometry("700x300")

choose = Label(text="You want to listen music or watch Videos ?", font=("comic sans", 21))
choose.place(x=100, y=10)

music_logo = PhotoImage(file=r"music player.png", height=200, width=200)
music_player = Button(image=music_logo, bd=0, command=open_music_player)
music_player.place(x=100, y=51)
music_label = Label(text="Music Player", font=("comic sans", "15"))
music_label.place(x=150, y=250)

video_logo = PhotoImage(file=r"video player.png")
video_player = Button(image=video_logo, bd=0, command=open_video_player)
video_player.place(x=420, y=51)
video_label = Label(text="Video Player", font=("comic sans", "15"))
video_label.place(x=450, y=250)

root.mainloop()
