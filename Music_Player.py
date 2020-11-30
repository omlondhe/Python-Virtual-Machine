import os
from tkinter import *
from pygame import mixer
import sqlite3
from mutagen.mp3 import MP3
import time
from tkinter.messagebox import showinfo, showwarning, showerror


song = "No song Playing Now"


def volume_setter(n):
    mixer.init()
    mixer.music.set_volume(int(n) / 10)


ls = []
for k in os.listdir("mp3s"):
    ls.append(k)


def shuffle(sh):
    print(sh)
    for shuffling in ls:
        mixer.init()
        mixer.music.load("mp3s\\" + shuffling)
        song_played = MP3("mp3s\\" + shuffling)
        song_len = song_played.info.length
        mixer.music.play()
        time.sleep(song_len + 2)


def search_song():
    searched_song = search.get().capitalize()

    def pp(even):
        s = lb.curselection()
        if even.widget.cget("text") == "Play":
            mixer.init()
            mixer.music.load("mp3s\\" + lst[s[0]])
            mixer.music.play()
            play_button.config(text="Pause")
        elif even.widget.cget("text") == "Pause":
            mixer.music.pause()
            play_button.config(text="Play ")
        elif even.widget.cget("text") == "Play ":
            mixer.music.unpause()
            play_button.config(text="Pause")

    def stp():
        mixer.music.stop()
        play_button.config(text="Play")

    tl = Toplevel(root)
    tl.geometry("871x611")
    tl.title("Search Results")
    s_lbl = Label(tl, text="Search Results", font="ariel 35")
    s_lbl.place(x=0, y=0)

    play_button = Button(tl, text="Play", font="lucida 15")
    play_button.place(x=3, y=71)
    play_button.bind("<Button-1>", pp)

    st_but = Button(tl, text="Stop", font="lucida 15", command=stp)
    st_but.place(x=91, y=71)

    vols = Scale(tl, from_=0, to=10, orient=HORIZONTAL, width=11, label="Volume", length=200,
                 troughcolor="light green",
                 command=volume_setter)
    vols.set(5)
    vols.place(x=621, y=51)

    s_l_scroll = Scrollbar(tl)
    s_l_scroll.pack(side=RIGHT, fill=Y)
    lb = Listbox(tl, width=91, selectmode=SINGLE, font="lucida 12", height=25, yscrollcommand=s_l_scroll.set)
    lb.place(x=7, y=121)

    lst = []
    counter = 0
    for no in range(0, len(ls)):
        if searched_song in ls[counter]:
            lst.append(ls[counter])
            lb.insert(END, ls[counter])
        counter = counter + 1

    s_l_scroll.config(command=lb.yview)
    tl.mainloop()


def songs(e):
    print(e)

    def pp(even):
        s = lb.curselection()
        if even.widget.cget("text") == "Play":
            mixer.init()
            mixer.music.load("mp3s\\" + ls[s[0]])
            mixer.music.play()
            play_button.config(text="Pause")
        elif even.widget.cget("text") == "Pause":
            mixer.music.pause()
            play_button.config(text="Play ")
        elif even.widget.cget("text") == "Play ":
            mixer.music.unpause()
            play_button.config(text="Pause")

    def stp():
        mixer.music.stop()
        play_button.config(text="Play")

    tl = Toplevel(root)
    tl.geometry("871x611")
    tl.title("All Songs")
    s_lbl = Label(tl, text="All Songs", font="ariel 35")
    s_lbl.place(x=0, y=0)

    play_button = Button(tl, text="Play", font="lucida 15")
    play_button.place(x=3, y=71)
    play_button.bind("<Button-1>", pp)

    st_but = Button(tl, text="Stop", font="lucida 15", command=stp)
    st_but.place(x=91, y=71)

    vols = Scale(tl, from_=0, to=10, orient=HORIZONTAL, width=11, label="Volume", length=200,
                 troughcolor="light green",
                 command=volume_setter)
    vols.set(5)
    vols.place(x=621, y=51)

    s_l_scroll = Scrollbar(tl)
    s_l_scroll.pack(side=RIGHT, fill=Y)
    lb = Listbox(tl, width=91, selectmode=SINGLE, font="lucida 12", height=25, yscrollcommand=s_l_scroll.set)
    lb.place(x=7, y=121)
    s_l_scroll.config(command=lb.yview)

    for j in ls:
        lb.insert(END, j)


def play_song(event):
    mixer.init()
    mixer.music.load("mp3s\\" + event.widget.cget("text"))
    mixer.music.play()
    global song
    song = event.widget.cget("text")

    f3 = LabelFrame(root, text="Now Playing", font="ariel 15", padx=7, pady=11, width=100)
    f3.place(x=0, y=501, width=700)
    lbl = Label(f3, text=song, font="lucida 11")
    lbl.pack(anchor=NW)

    def pause(even):
        p = even.widget.cget("text")
        if p == "Pause":
            mixer.music.pause()
            pl_pz.config(text="Play")

        elif p == "Play":
            mixer.music.unpause()
            pl_pz.config(text="Pause")

    def stop_song():
        mixer.music.stop()
        pl_pz.config(text="Play")

    pl_pz = Button(f3, text="Pause")
    pl_pz.pack(side=LEFT, padx=5)
    pl_pz.bind("<Button-1>", pause)

    st_but = Button(f3, text="Stop", command=stop_song)
    st_but.pack(side=LEFT, padx=5)


def drk():
    showwarning("PyPlayer-Dark Mode", "This feature is in development and you can use it as Beta feature")
    inv.set(1)
    invar = IntVar()
    invar.set(1)
    root.config(bg="black")
    f1.config(fg="white", bg="black")
    all_songs.config(fg="white", bg="black")
    playlist.config(fg="white", bg="black")
    playing.config(fg="white", bg="black")
    dm.config(fg="white", bg="black")
    f2.config(bg="black", fg="white")


def now():
    s = song
    tl = Toplevel(root)
    tl.title("PyMusic Player - Now Playing")

    Label(tl, text=s, font="lucida 15").pack(side=TOP)

    def pause(even):
        p = even.widget.cget("text")
        if p == "Pause":
            mixer.music.pause()
            pl_pz.config(text="Play ")

        elif p == "Play ":
            mixer.music.unpause()
            pl_pz.config(text="Pause")

    def stp():
        mixer.music.stop()
        pl_pz.config(text="Play")

    pl_pz = Button(tl, text="Pause", padx=10, pady=7)
    pl_pz.pack(side=LEFT, padx=7, pady=7)
    pl_pz.bind("<Button-1>", pause)

    st_but = Button(tl, text="Stop", font="lucida 13", command=stp)
    st_but.pack(side=LEFT, padx=7, pady=7)

    vol_play = Scale(tl, from_=0, to=10, orient=HORIZONTAL, width=11, label="Volume", length=200,
                     troughcolor="light green",
                     command=volume_setter)
    vol.set(5)
    vol_play.pack(side=RIGHT)

    tl.mainloop()


def play1(eve):
    print(eve)
    tl = Toplevel(root)
    tl.title("Playlist")
    tl.geometry("821x611")

    def m_play():
        tm = Toplevel(tl)
        tm.title("My Playlist")
        tm.geometry("300x251")
        con = sqlite3.connect("playlist")
        cur = con.cursor()
        tables = cur.execute("SELECT name FROM sqlite_master WHERE TYPE='table';")

        c = Label(tm, text="Your Playlists : ", font="lucida 17")
        c.place(x=3, y=21)

        t_lst = []
        for t in tables:
            t_lst.append(t[0])

        def options(op):
            p_ls = []
            playlist_songs = cur.execute(f"SELECT * FROM {op}")
            for opt in playlist_songs:
                p_ls.append(opt[0])

            for playlist_songs in p_ls:
                mixer.init()
                mixer.music.load("mp3s\\" + playlist_songs)
                song_played = MP3("mp3s\\" + playlist_songs)
                song_len = song_played.info.length
                mixer.music.play()

                t1 = Toplevel(tm)
                t1.title("Now Playing Playlist")
                Label(t1, text=playlist_songs, font="lucida 12").pack(side=TOP)

                def pause(even):
                    p1 = even.widget.cget("text")
                    if p1 == "Pause":
                        mixer.music.pause()
                        pl_pz.config(text="Play ")

                    elif p1 == "Play ":
                        mixer.music.unpause()
                        pl_pz.config(text="Pause")

                def stp():
                    mixer.music.stop()
                    t1.destroy()

                pl_pz = Button(t1, text="Pause", padx=10, pady=7)
                pl_pz.pack(side=LEFT, padx=7, pady=7)
                pl_pz.bind("<Button-1>", pause)

                st_but = Button(t1, text="Stop", font="lucida 13", command=stp)
                st_but.pack(side=LEFT, padx=7, pady=7)

                vol_play = Scale(t1, from_=0, to=10, orient=HORIZONTAL, width=11, label="Volume", length=200,
                                 troughcolor="light green",
                                 command=volume_setter)
                vol.set(5)
                vol_play.pack(side=RIGHT)

                t1.mainloop()

                time.sleep(song_len + 2)

        p = StringVar()
        p.set("Select Playlist")
        p_lists = OptionMenu(tm, p, *t_lst, command=options)
        p_lists.place(x=7, y=91)
        tm.mainloop()

    def create():
        def create_playlist():
            try:
                song_selected = lb.curselection()
                print(song_selected)

                con_create = sqlite3.connect("playlist")
                con_create.execute(f"CREATE TABLE {c_n.get()}(songs varchar(300));")
                con_create.commit()

                for nos in song_selected:
                    con_create.execute(f'''INSERT INTO {c_n.get()} VALUES('{ls[nos]}')''')
                    con_create.commit()

                con_create.close()
            except EXCEPTION as e:
                showerror("PyPlayer - Create Playlist", e)

        c = Label(tl, text="Create Playlist", font="lucida 17")
        c.place(x=3, y=121)

        lb = Label(tl, text="Select Songs : ", font="lucida 12")
        lb.place(x=7, y=161)

        s_l_scroll = Scrollbar(tl)
        s_l_scroll.pack(side=RIGHT, fill=Y)
        lb = Listbox(tl, width=91, height=11, yscrollcommand=s_l_scroll.set, selectmode=MULTIPLE)
        s_l_scroll.config(command=lb.yview)

        for j in ls:
            lb.insert(END, j)
        lb.place(x=51, y=191)

        c_p = Label(tl, text="Enter Playlist name : ", font="lucida 12")
        c_p.place(x=7, y=391)

        c_n = Entry(tl, font="lucida 12")
        c_n.place(x=171, y=391)

        c_b = Button(tl, text="Create", font="lucida 8", command=create_playlist)
        c_b.place(x=321, y=391)

    def edit():
        tm = Toplevel(tl)
        tm.title("Edit Playlist")
        tm.geometry("821x611")
        con = sqlite3.connect("playlist")
        cur = con.cursor()
        tables = cur.execute("SELECT name FROM sqlite_master WHERE TYPE='table';")

        c = Label(tm, text="Edit Playlist : ", font="lucida 17")
        c.place(x=3, y=21)

        t_lst = []
        for t in tables:
            t_lst.append(t[0])

        def edit_play(e_p):

            def add_s():
                Label(tm, text="Select Songs to Add", font="lucida 15").place(x=3, y=111)
                add_song.destroy()
                del_play.destroy()
                del_song.destroy()

                s_l_scroll = Scrollbar(tl)
                s_l_scroll.pack(side=RIGHT, fill=Y)
                lb = Listbox(tm, width=91, height=11, yscrollcommand=s_l_scroll.set, selectmode=MULTIPLE)
                s_l_scroll.config(command=lb.yview)

                for j in ls:
                    lb.insert(END, j)
                lb.place(x=11, y=151)

                def add_so():
                    try:
                        si = lb.curselection()
                        for s in si:
                            cur.execute(f"INSERT INTO {e_p} VALUES('{ls[s]}')")
                            con.commit()
                        showinfo("PyPlayer - Add Songs to Playlist", f"Songs added to Playlist : {e_p}")
                    except EXCEPTION as ex:
                        showerror("PyPlayer - Add Songs to Playlist", ex)
                ad = Button(tm, text="Add selected songs", font="lucida 11", command=add_so)
                ad.place(x=3, y=351)

            def del_s():
                playlist_s = cur.execute(f"SELECT * FROM {e_p}")
                Label(tm, text="Select Songs to Delete", font="lucida 15").place(x=3, y=111)
                add_song.destroy()
                del_play.destroy()
                del_song.destroy()

                s_l_scroll = Scrollbar(tl)
                s_l_scroll.pack(side=RIGHT, fill=Y)
                lb = Listbox(tm, width=91, height=11, yscrollcommand=s_l_scroll.set, selectmode=MULTIPLE)
                s_l_scroll.config(command=lb.yview)

                so_lst = []
                for j in playlist_s:
                    so_lst.append(j)
                    lb.insert(END, j)
                lb.place(x=11, y=151)

                def delete_s():
                    try:
                        si = lb.curselection()

                        for s in si:
                            cur.execute(f"DELETE FROM {e_p} WHERE SONGS='{so_lst[s][0]}'")
                            con.commit()
                        showinfo("PyPlayer - Delete Songs from Playlist", f"Songs deleted from playlist : {e_p}")
                    except EXCEPTION as exc:
                        showerror("PyPlayer - Delete Songs from Playlist", exc)
                delete = Button(tm, text="Delete selected songs", font="lucida 11", command=delete_s)
                delete.place(x=3, y=351)

            def del_t():
                try:
                    cur.execute(f"DROP TABLE {e_p}")
                    tm.destroy()
                    showinfo("PyPlayer - Delete Playlist", "Playlist Deleted")
                except EXCEPTION as exce:
                    showerror("PyPlayer - Delete Playlist", exce)

            add_song = Button(tm, text="Add songs", font="lucida 11", command=add_s)
            add_song.place(x=3, y=121)

            del_song = Button(tm, text="Delete songs", font="lucida 11", command=del_s)
            del_song.place(x=101, y=121)

            del_play = Button(tm, text="Delete Playlist", font="lucida 11", command=del_t)
            del_play.place(x=211, y=121)

        p = StringVar()
        p.set("Select Playlist")
        p_lists = OptionMenu(tm, p, *t_lst, command=edit_play)
        p_lists.place(x=7, y=71)

    title = Label(tl, text="Playlists", font="ariel 35 bold")
    title.place(x=0, y=0)

    edit_b = Button(tl, text="My Playlists", command=m_play)
    edit_b.place(x=3, y=71)

    create_b = Button(tl, text="Create Playlist", command=create)
    create_b.place(x=111, y=71)

    edit_b = Button(tl, text="Edit Playlist", command=edit)
    edit_b.place(x=221, y=71)

    tl.mainloop()


root = Tk()
root.title("PyMusic Player")
root.minsize(451, 171)
root.geometry("821x611")

f1 = LabelFrame(root, text="Collections", font="ariel 15 bold", bd=0)
f1.place(x=3, y=11)

search = Entry(f1, font="lucida 12")
search.pack(anchor=NW, padx=7, pady=7)
sb = Button(f1, text="Search", command=search_song)
sb.pack(anchor=NE, padx=7, pady=3)

all_songs = Button(f1, text="Shuffle All", font="lucida 12", padx=11, bd=0)
all_songs.pack(anchor=NW, padx=7, pady=11)
all_songs.bind("<Button-1>", shuffle)

all_songs = Button(f1, text="All Songs", font="lucida 12", padx=11, bd=0)
all_songs.pack(anchor=NW, padx=7, pady=11)
all_songs.bind("<Button-1>", songs)

playlist = Button(f1, text="Playlist", font="lucida 12", padx=11, bd=0)
playlist.pack(anchor=NW, padx=7, pady=9)
playlist.bind("<Button-1>", play1)

playing = Button(f1, text="Now Playing", font="lucida 12", padx=11, bd=0, command=now)
playing.pack(anchor=NW, padx=7, pady=9)

inv = IntVar()
dm = Radiobutton(f1, text="Dark Mode", variable=inv, font="lucida 12", padx=11, bd=0, command=drk)
dm.pack(anchor=NW, padx=7, pady=9)

vol = Scale(f1, from_=0, to=10, orient=HORIZONTAL, width=11, label="Volume", length=200, troughcolor="light green",
            command=volume_setter)
vol.set(5)
vol.pack(anchor=NW)

f2 = LabelFrame(root, text="Songs", font="ariel 21 bold", bd=1, padx=10, pady=10)
f2.place(x=221, y=7)

for i in ls:
    b = Button(f2, text=i, font=", 11", padx=11, pady=7, bd=0)
    b.pack(anchor=NW)
    b.bind("<Button-1>", play_song)


root.mainloop()
