from tkinter import *
import webbrowser
import subprocess
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import _thread
import os
import datetime
import calendar
from tkinter import colorchooser


def this_pc():
    os.system("explorer.exe /e,::{20D04FE0-3AEA-1069-A2D8-08002B30309D}")


def notepad_thread():
    subprocess.call(["Python", "Notepad.py"])


def open_notepad():
    _thread.start_new_thread(notepad_thread, ())


def calc_thread():
    subprocess.call(["Python", "calculator.py"])


def open_calc():
    _thread.start_new_thread(calc_thread, ())


def java_thread():
    subprocess.call(["Python", "java_editor.py"])


def open_java():
    _thread.start_new_thread(java_thread, ())


def c_thread():
    subprocess.call(["Python", "C_Editor.py"])


def open_c():
    _thread.start_new_thread(c_thread, ())


def media_thread():
    subprocess.call(["Python", "Media_Player.py"])


def open_media():
    _thread.start_new_thread(media_thread, ())


def yt_thread():
    webbrowser.open_new_tab("https://www.youtube.com")


def open_yt():
    _thread.start_new_thread(yt_thread, ())


def google_thread():
    webbrowser.open_new_tab("https://www.google.com")


def open_google():
    _thread.start_new_thread(media_thread, ())


def clk_thread():
    subprocess.call(["Python", "clock.py"])


def open_clk():
    _thread.start_new_thread(clk_thread, ())


def game_thread():
    subprocess.call(["Python", "Game.py"])


def open_games():
    _thread.start_new_thread(game_thread, ())


def face_recognition_setup():
    subprocess.call(["Python", "insert image into DB.py"])


def thread_face():
    _thread.start_new_thread(face_recognition_setup, ())


def change_bg():
    pic_name = askopenfilename(defaultextension=".png", filetypes=(["PNG Files", ".png"], ["JPG Files", ".jpg"],
                                                                   ["JPEG Files", ".jpeg"]))
    if ".png" in pic_name:
        png = PhotoImage(file=pic_name)
        wall.config(image=png)
        wall.image = png
    else:
        jpeg = Image.open(pic_name)
        jpeg_img = ImageTk.PhotoImage(jpeg)
        wall.config(image=jpeg_img)
        wall.image = jpeg_img


def ico_col():
    clr = colorchooser.askcolor(title="Choose a Color for Icon")
    pc.config(activebackground=clr[1])
    b.config(activebackground=clr[1])
    b1.config(activebackground=clr[1])
    b2.config(activebackground=clr[1])
    b3.config(activebackground=clr[1])
    b4.config(activebackground=clr[1])
    b5.config(activebackground=clr[1])
    b6.config(activebackground=clr[1])
    b7.config(activebackground=clr[1])
    b8.config(activebackground=clr[1])
    b9.config(activebackground=clr[1])


def ico_size():
    size = Toplevel(root)
    head = LabelFrame(text="Icon Size")
    head.place(x=3, y=3)

    def ico_width():
        pw.config(width=width.get())
        pc.config(width=width.get())
        b.config(width=width.get())
        b1.config(width=width.get())
        b2 .config(width=width.get())
        b3.config(width=width.get())
        b4.config(width=width.get())
        b5.config(width=width.get())
        b6.config(width=width.get())
        b7.config(width=width.get())
        b8.config(width=width.get())
        b9.config(width=width.get())

    def ico_height():
        pc.config(height=height.get())
        b.config(height=height.get())
        b1.config(height=height.get())
        b2.config(height=height.get())
        b3.config(height=height.get())
        b4.config(height=height.get())
        b5.config(height=height.get())
        b6.config(height=height.get())
        b7.config(height=height.get())
        b8.config(height=height.get())
        b9.config(height=height.get())

    width_lbl = Label(size, text="Width : ")
    width_lbl.place(x=3, y=11)
    width = Spinbox(size, from_=71, to=251, command=ico_width, textvariable=w)
    width.place(x=53, y=11)
    w.set(width.get())
    height_lbl = Label(size, text="Height : ")
    height_lbl.place(x=3, y=51)
    height = Spinbox(size, from_=71, to=251, command=ico_height, textvariable=h)
    height.place(x=53, y=51)
    h.set(height.get())
    size.mainloop()


def bg_col():
    root.config(background=colorchooser.askcolor(title="Choose a Color for Background")[1])


def tool_col():
    toolbar.config(background=colorchooser.askcolor(title="Choose a Color")[1])


def ico_bg():
    clr = colorchooser.askcolor(title="Choose a Color for Icon")
    pc.config(background=clr[1])
    b.config(background=clr[1])
    b1.config(background=clr[1])
    b2.config(background=clr[1])
    b3.config(background=clr[1])
    b4.config(background=clr[1])
    b5.config(background=clr[1])
    b6.config(background=clr[1])
    b7.config(background=clr[1])
    b8.config(background=clr[1])
    b9.config(background=clr[1])
    scrollable_frame.config(background=clr[1])
    pw.config(background=clr[1])
    f.config(background=clr[1])


def system_off():

    def switch_user():
        root.destroy()
        subprocess.call(["Python", "login.py"])

    def close_vm():
        root.destroy()

    def turn_off():
        os.system("shutdown /s /t 1")

    def lock_button():
        os.system("rundll32.exe user32.dll,LockWorkStation")

    off_screen = Toplevel(root)
    off_screen.geometry("400x120")
    ask_off = Label(off_screen, text="Which operation do you want to perform ?", font=("Ariel", 15))
    ask_off.place(x=9, y=3)
    user = Button(off_screen, text="Switch User", command=switch_user)
    user.place(x=21, y=57)
    close = Button(off_screen, text="Close VM", command=close_vm)
    close.place(x=121, y=57)
    toff = Button(off_screen, text="Turn Off", command=turn_off)
    toff.place(x=221, y=57)
    lock = Button(off_screen, text="Lock", command=lock_button)
    lock.place(x=321, y=57)
    off_screen.mainloop()


def check_mode():

    def dark_mode():
        scrollbar.config(background="black", troughcolor="black")
        root.config(background="black")
        f.config(background="black")
        scrollbar.config(background="black")
        pw.config(background="black")
        toolbar.config(background="black")
        dt.config(background="black")
        pc.config(background="black", activebackground="black")
        b.config(background="black", activebackground="black")
        b1.config(background="black", activebackground="black")
        b2.config(background="black", activebackground="black")
        b3.config(background="black", activebackground="black")
        b4.config(background="black", activebackground="black")
        b5.config(background="black", activebackground="black")
        b6.config(background="black", activebackground="black")
        b7.config(background="black", activebackground="black")
        b8.config(background="black", activebackground="black")
        b9.config(background="black", activebackground="black")

    def light_mode():
        scrollbar.config(bg="white", troughcolor="white")
        root.config(background="white")
        f.config(background="white")
        pw.config(background="white")
        scrollbar.config(background="white")
        toolbar.config(background="white")
        dt.config(background="white")
        pc.config(background="white", activebackground="white")
        b.config(background="white", activebackground="white")
        b1.config(background="white", activebackground="white")
        b2.config(background="white", activebackground="white")
        b3.config(background="white", activebackground="white")
        b4.config(background="white", activebackground="white")
        b5.config(background="white", activebackground="white")
        b6.config(background="white", activebackground="white")
        b7.config(background="white", activebackground="white")
        b8.config(background="white", activebackground="white")
        b9.config(background="white", activebackground="white")

    if dark_mode_val.get() == 1:
        dark_mode()
        dark_mode_val.set(1)
    else:
        light_mode()
        dark_mode_val.set(0)


def right(event):
    m1.tk_popup(event.x_root, event.y_root, 0)


def on_enter(event):
    day = datetime.date.today().weekday()
    dt.configure(text="Date : " + str(datetime.date.today()) + " [" + calendar.day_name[day] + "] ",
                 bg=toolbar.cget("background"))
    if toolbar.cget("background") == "black":
        dt.configure(fg="white")


def pc_enter(event):
    dt.configure(text="My Computer", bg=toolbar.cget("background"))
    if toolbar.cget("background") == "black":
        dt.configure(fg="white")


def b_enter(event):
    dt.configure(text="Notepad", bg=toolbar.cget("background"))
    if toolbar.cget("background") == "black":
        dt.configure(fg="white")


def b1_enter(event):
    dt.configure(text="Calculator", bg=toolbar.cget("background"))
    if toolbar.cget("background") == "black":
        dt.configure(fg="white")


def b2_enter(event):
    dt.configure(text="Java Editor", bg=toolbar.cget("background"))
    if toolbar.cget("background") == "black":
        dt.configure(fg="white")


def b3_enter(event):
    dt.configure(text="C Editor", bg=toolbar.cget("background"))
    if toolbar.cget("background") == "black":
        dt.configure(fg="white")


def b4_enter(event):
    dt.configure(text="Media Player", bg=toolbar.cget("background"))
    if toolbar.cget("background") == "black":
        dt.configure(fg="white")


def b5_enter(event):
    dt.configure(text="YouTube", bg=toolbar.cget("background"))
    if toolbar.cget("background") == "black":
        dt.configure(fg="white")


def b6_enter(event):
    dt.configure(text="Google", bg=toolbar.cget("background"))
    if toolbar.cget("background") == "black":
        dt.configure(fg="white")


def b7_enter(event):
    dt.configure(text="Clock", bg=toolbar.cget("background"))
    if toolbar.cget("background") == "black":
        dt.configure(fg="white")


def b8_enter(event):
    dt.configure(text="Games", bg=toolbar.cget("background"))
    if toolbar.cget("background") == "black":
        dt.configure(fg="white")


def b9_enter(event):
    dt.configure(text="Face Recognition", bg=toolbar.cget("background"))
    if toolbar.cget("background") == "black":
        dt.configure(fg="white")


def on_leave(enter):
    dt.configure(text='')


def time_thread():
    time_lbl.config(text=datetime.datetime.now().strftime("%H:%M:%S"))
    time_lbl.after(60, time_thread)


root = Tk()
root.config(background="black")
root.attributes("-fullscreen", True)
h = IntVar()
w = IntVar()
kill = FALSE

toolbar = Frame(root)
off_img = PhotoImage(file="iconfinder_059_CircledOff_183188.png")
off = Button(toolbar, image=off_img, command=system_off)
off.pack(side=LEFT)

time_lbl = Label(toolbar, text=datetime.datetime.now().strftime("%H:%M:%S"), bg="black", fg="white",
                 font="monotype 21 bold")
time_lbl.pack(side=RIGHT)
time_lbl.bind("<Enter>", on_enter)
time_lbl.bind("<Leave>", on_leave)
tth = _thread.start_new_thread(time_thread, ())

dt = Label(toolbar, text=None, font="lucida 11 bold")
dt.pack(side=LEFT)

toolbar.pack(side=BOTTOM, fill=X)

f = Frame(root)
f.pack(side=LEFT, fill=Y)
pw = Canvas(f, width=71)
scrollbar = Scrollbar(f, orient="vertical", command=pw.yview, width=11)
scrollable_frame = Frame(pw)

scrollable_frame.bind(
    "<Configure>",
    lambda e: pw.configure(
        scrollregion=pw.bbox("all")
    )
)

pw.create_window((0, 0), window=scrollable_frame, anchor="nw")

pw.configure(yscrollcommand=scrollbar.set)

pw.pack(side="left", fill="y", expand=True)
scrollbar.pack(side="right", fill="y")

pc_img = PhotoImage(file="pc.png")
pc = Button(scrollable_frame, image=pc_img, command=this_pc, activebackground="red", border=1, relief=SUNKEN, width=71,
            height=71)
pc.bind("<Enter>", pc_enter)
pc.bind("<Leave>", on_leave)
pc.pack()

notepad = PhotoImage(file="N.png")
b = Button(scrollable_frame, image=notepad, command=open_notepad, activebackground="red", border=1, relief=SUNKEN,
           width=71, height=71)
b.bind("<Enter>", b_enter)
b.bind("<Leave>", on_leave)
b.pack()

calc = PhotoImage(file="calculator.png")
b1 = Button(scrollable_frame, image=calc, command=open_calc, activebackground="red", border=1, relief=SUNKEN, width=71,
            height=71)
b1.bind("<Enter>", b1_enter)
b1.bind("<Leave>", on_leave)
b1.pack()

java = PhotoImage(file="java.png")
b2 = Button(scrollable_frame, image=java, command=open_java, activebackground="red", border=1, relief=SUNKEN, width=71,
            height=71)
b2.bind("<Enter>", b2_enter)
b2.bind("<Leave>", on_leave)
b2.pack()

c = PhotoImage(file="c.png")
b3 = Button(scrollable_frame, image=c, command=open_c, activebackground="red", border=1, relief=SUNKEN, width=71,
            height=71)
b3.bind("<Enter>", b3_enter)
b3.bind("<Leave>", on_leave)
b3.pack()

media = PhotoImage(file="media.png")
b4 = Button(scrollable_frame, image=media, command=open_media, activebackground="red", border=1, relief=SUNKEN,
            width=71, height=71)
b4.bind("<Enter>", b4_enter)
b4.bind("<Leave>", on_leave)
b4.pack()

yt = PhotoImage(file="yt.png")
b5 = Button(scrollable_frame, image=yt, command=open_yt, activebackground="red", border=1, relief=SUNKEN, width=71,
            height=71)
b5.bind("<Enter>", b5_enter)
b5.bind("<Leave>", on_leave)
b5.pack()

chrome = PhotoImage(file="chrome.png")
b6 = Button(scrollable_frame, image=chrome, command=open_google, activebackground="red", border=1, relief=SUNKEN,
            width=71, height=71)
b6.bind("<Enter>", b6_enter)
b6.bind("<Leave>", on_leave)
b6.pack()

clk = PhotoImage(file="clk.png")
b7 = Button(scrollable_frame, image=clk, command=open_clk, activebackground="red", border=1, relief=SUNKEN, width=71,
            height=71)
b7.bind("<Enter>", b7_enter)
b7.bind("<Leave>", on_leave)
b7.pack()

game = PhotoImage(file="game.png")
b8 = Button(scrollable_frame, image=game, command=open_games, activebackground="red", border=1, relief=SUNKEN,
            width=71, height=71)
b8.bind("<Enter>", b8_enter)
b8.bind("<Leave>", on_leave)
b8.pack()

face = PhotoImage(file="face.png")
b9 = Button(scrollable_frame, image=face, command=thread_face, activebackground="red", border=1, relief=SUNKEN,
            width=71, height=71)
b9.bind("<Enter>", b9_enter)
b9.bind("<Leave>", on_leave)
b9.pack()

pw.pack(side=LEFT, fill=Y)

m1 = Menu(root, tearoff=0)
m1.add_command(label="Change Background", command=change_bg)
m1.add_command(label="Background Layer", command=bg_col)
m1.add_separator()
m1.add_command(label="Icon Animations", command=ico_col)
m1.add_command(label="Icon Color", command=ico_bg)
m1.add_command(label="Icon Size", command=ico_size)
m1.add_separator()
dark_mode_val = IntVar()
m1.add_checkbutton(label="Dark Theme", var=dark_mode_val, command=check_mode)
m1.add_separator()
m1.add_command(label="Toolbar Color", command=tool_col)

wall_img = Image.open("py.jpg")
wall_def = ImageTk.PhotoImage(wall_img)
wall = Label(root, image=wall_def)
wall.pack(expand=1)

root.bind("<Button-3>", right)

mainloop()
root.mainloop()
