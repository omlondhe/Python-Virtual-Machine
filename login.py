from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter, ImageDraw
from firebase import firebase
import sqlite3
import re
import _thread
import subprocess

con = sqlite3.connect("UserData")
authentication = firebase.FirebaseAuthentication('lFTDGhEV8Qy9PxYiA4mMJXWM3sJbTCAq7bTlB8FG',
                                                 'missionprojects2020@gmail.com')
conn = firebase.FirebaseApplication("https://programming-aa2cb.firebaseio.com/", authentication)
root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Login form")

img = Image.open("beach3.jpg")
imag = ImageTk.PhotoImage(img)
frame = Label(root, image=imag)


def label(event):
    _thread.start_new_thread(lab1, ())


def lab1():
    subprocess.call(["python", "signup.py"])


NoAccLabel = Label(root, bg="black", fg="white", font=('calibri', 11))
NoAccLabel.config(text="No Account.Create Here")
NoAccLabel.bind('<Button-1>', label)


def delete1():
    password.delete(0, END)


def confirm(event):
    # curs = con.execute("SELECT * FROM USER")
    getpassword = password.get()
    flag = 0
    res = conn.get('Python/Counter/', '')
    ls = str(res).split(':')
    listing = ls[1].split('}')
    Counter = int(listing[0])
    # count = counter
    while Counter > 0:
        fetch = conn.get('/Python/User/' + str(Counter) + '/', '')
        if str(fetch['Password']) == getpassword:
            flag = 1
            break
        Counter -= 1

    if flag == 1:
        root.destroy()
        subprocess.call(["Python", "main_GUI.py"])
    else:
        messagebox.showinfo("OOPS", "sorry,your username and password don't match")
    clear.place(x=664, y=352)
    next1.place(x=678, y=352)


def passworddata(event):
    clear.configure(bg="white", fg="black")
    next1.configure(bg="gray", fg="white")
    password.delete(0, END)
    password.config(bg="white", fg="black", show="*")
    password.bind('<Return>', confirm)

    clear.configure(command=delete1)
    # pas.bind('<Return>', )


def enter(event):
    global password, img1, newframe, clear, next1
    flag = 0
    # cursor = con.execute("SELECT * FROM USER")
    res = conn.get('Python/Counter/', '')
    listing = str(res).split(':')
    ls = listing[1].split('}')
    Counter = int(ls[0])
    while Counter > 0:
        fetchall = conn.get('/Python/User/' + str(Counter) + '/', '')
        for k in range(0, namelist.__len__()):
            m = re.sub(" ^ \s + | \s + $ ", "", namelist[k].cget('text'))

            i0 = re.sub("^\s+|\s+$", "", str(fetchall['Email']))

            i3 = re.sub("^\s+|\s+$", "", str(fetchall['Phone']))

            if i0 == m or i3 == m:
                flag = 1
                r = open("information.txt", 'w')
                r.write(m)
                r.close()
                break
        Counter -= 1
    # for i in cursor:
    #     print(i)
    #     for k in range(0, namelist.__len__()):
    #         m = re.sub(" ^ \s + | \s + $ ","", namelist[k].cget('text'))
    #
    #         i0 = re.sub("^\s+|\s+$","",str(i[0]))
    #
    #         i3 = re.sub("^\s+|\s+$", "", str(i[3]))
    #
    #         if i0 == m or i3 == m:
    #             flag = 1
    #             break

    if flag == 1:
        img1 = Image.open("beach1.jpg")
        image2 = ImageTk.PhotoImage(img1)
        root1 = Toplevel(root)
        w1, h1 = root.winfo_screenwidth(), root1.winfo_screenheight()
        root1.geometry("%dx%d+0+0" % (w1, h1))
        newframe = Label(root1, image=image2)
        newframe.image = image2

        blur1 = img1.filter(ImageFilter.BLUR)
        bl1 = ImageTk.PhotoImage(blur1)
        frame.image = bl1

        password = Entry(newframe, bd=0, bg="black", insertwidth=1, font=('calibri', 16))
        password.insert(0, 'Enter Password')
        password.configure(foreground="white", state=NORMAL)
        password.bind("<FocusIn>", passworddata)

        clear = Button(newframe, font=('calibri', 10), bg="black", fg="white", text="x", bd=0)
        next1 = Button(newframe, font=('calibri', 10), text="→", bg="gray", fg="white")

        newframe.pack(fill='both', expand=True)
        password.place(x=480, y=350)

        b = Button(root1, text="☻ Unlock Using Face", bd=0, fg="white", bg="black",
                   command=face_rec)
        b.place(x=480, y=421)


def face_rec():
    subprocess.call(["Python", "Face detection DB.py"])


def placeholder(event):

    blur = img.filter(ImageFilter.BLUR)
    bl = ImageTk.PhotoImage(blur)
    frame.configure(image=bl)
    frame.image = bl


y = 0
cur = con.execute("SELECT MAIL,PHONE FROM USER")
con.commit()
namelist = []
ycoordinate = 300
result = conn.get('Python/Counter/', '')
list = str(result).split(':')
list1 = list[1].split('}')
counter = int(list1[0])
count = counter
if count == 0:
    namelist.append("No User!!!")
while counter > 0:
    fetchall = conn.get('/Python/User/' + str(counter) + '/', '')
    if str(fetchall['Email']) is not None:
        namelist.append(fetchall['Email'])
    else:
        namelist.append(fetchall['Phone'])
    counter -= 1
# for i in cur:
#     print(type(i))
#     if i[0] is not None:
#         namelist.append(i[0])
#     else:
#         namelist.append(i[1])
for j in range(0, namelist.__len__()):
    m = re.sub("^\s+|\s+$", "", str(namelist[j]))
    ycoordinate = ycoordinate + 36
    namelist[j] = Label(root, fg="white", bg="black", text=m, font=("Calibri", 13), width=35, pady=5)
    namelist[j].place(x=450, y=ycoordinate)

    namelist[j].bind('<Button-1>', placeholder)
    namelist[j].bind('<Button-1>', enter)


frame.pack(fill='both', expand=TRUE)
NoAccLabel.place(x=540, y=550)
root.mainloop()
