import _thread
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter
from firebase import firebase
import sqlite3, pymysql
import smtplib
import random
import requests
import subprocess
global retry, mail


def delete():
    mail.delete(1.0, END)


def log(ev):
    global clearlabel
    clearlabel = Label(root, text="Clear", bg="black", fg="white")
    clearlabel.place(x=480, y=430)


def log1(ev):
    global proceedlabel
    proceedlabel = Label(root, text="Click to Proceed", bg="black", fg="white")
    proceedlabel.place(x=480, y=430)


def logo1(ev):
    proceedlabel.destroy()


def logo(ev):
    clearlabel.destroy()


def delete1():
    confirmpassword.delete(0, END)


def check(eve):
    global error, flag
    if str(password.get()) is not str(confirmpassword.get()):
        error = Label(newframe, text="Password Don't Match", fg="red", bg="black")
        error.place(x=710, y=401)
        flag = 1
        confirm(confirmpassword)
    if str(password.get()) == str(confirmpassword.get()):
        if flag == 1:
            error.destroy()
        pasget = str(password.get())
        result = conn.get('Python/Counter/', '')
        list = str(result).split(':')
        list1 = list[1].split('}')
        counter = int(list1[0])
        mailfetch = str(mailget).split('\n')
        f = open("Information.txt", 'a')
        f.write(pasget)
        f.close()
        if mailget.__contains__(".com"):
            data = {
                'Email': mailfetch[0],
                'Otp': 'null',
                'Password': pasget,
                'Phone': 'null'
            }
            conn.put('/Python/User/', counter, data)
            # con.execute("UPDATE USER SET PASSWORD ='" + pasget + "' WHERE MAIL='" + mailget + "'")
            # con.commit()
            messagebox._show("Success", "Congratulations , your Account is created successfuly")
            res = messagebox.askyesno("Link", "Do you want to link your Phone Number")

            if res is True:
                _thread.start_new_thread(threadcall, ())
            else:
                ans = messagebox.askyesno("PyVM - Face Recognition", "Do you want to Add your Face Unlock ?")
                if ans:
                    messagebox.showwarning("PyVM - Face Recognition", "1] Press Return key to Register your Face\n"
                                                                      "2] Face recognition is still in beta\n"
                                                                      "3] Physical Password is more secure than "
                                                                      "the Face Unlock\n"
                                                                      "4] Add the face unlock at your own "
                                                                      "security risk\n"
                                                                      "5] If you want to terminate the process "
                                                                      "press 'Q'\n"
                                                                      "6] Remember to keep your face in good"
                                                                      " lighting condition\n"
                                                                      "7] You can add Only one Face for an Account")
                    root.destroy()
                    subprocess.call(["Python", "insert image into DB.py"])
                else:
                    root.destroy()
                    subprocess.call(["Python", "main_GUI.py"])

        else:
            data = {
                'Email': 'null',
                'Otp': 'null',
                'Password': pasget,
                'Phone': phon
            }
            conn.put('/Python/User/', counter, data)
            # con.execute("UPDATE USER SET PASSWORD ='" + pasget + "' WHERE PHONE='" + phon + "'")
            # con.commit()
            messagebox._show("Success", "Congratulations , your Account is created successfuly")
            res = messagebox.askyesno("Link", "Do you want to link your Mail id")
            if res is True:
                _thread.start_new_thread(threadcall, ())
            else:
                ans = messagebox.askyesno("PyVM - Face Recognition", "Do you want to Add your Face Unlock ?")
                if ans:
                    messagebox.showwarning("PyVM - Face Recognition", "1] Press Return key to Register your Face\n"
                                                                      "2] Face recognition is still in beta\n"
                                                                      "3] Physical Password is more secure than "
                                                                      "the Face Unlock\n"
                                                                      "4] Add the face unlock at your own "
                                                                      "security risk\n"
                                                                      "5] If you want to terminate the process "
                                                                      "press 'Q'\n"
                                                                      "6] Remember to keep your face in good"
                                                                      " lighting condition\n"
                                                                      "7] You can add Only one Face for an Account")
                    root.destroy()
                    subprocess.call(["Python", "insert image into DB.py"])
                else:
                    root.destroy()
                    subprocess.call(["Python", "main_GUI.py"])


def threadcall():
    subprocess.call(["python", "connect.py"])


def chfocus(eve):
    confirmpassword.configure(show="*")
    confirmpassword.delete(0, END)
    
    clear1.place(x=664, y=403)
    next1.place(x=678, y=401)
    confirmpassword.bind('<Return>', check)


def confirm(event):
    confirmpassword.configure(state=NORMAL, background="white", fg="black", )
    confirmpassword.place(x=480, y=400)
    confirmpassword.bind('<FocusIn>', chfocus)


def password1(event):
    global confirmpassword
    password.configure(show='*')
    confirmpassword = Entry(newframe, bd=0, bg="black", insertwidth=1, font=('calibri', 16))
    confirmpassword.insert(0, 'Confirm Password')
    confirmpassword.configure(foreground="white", state=DISABLED)
    password.configure(state=NORMAL, background="white", fg="black", highlightcolor="yellow", show="*")

    clear1.configure(bg="white", fg="black")
    next1.configure(bg="gray", fg="white")
    password.delete(0, END)
    password.bind('<Return>', confirm)
    # blur1 = img1.filter(ImageFilter.BLUR)
    # b2 = ImageTk.PhotoImage(blur1)
    # nframe.configure(image=b2)
    # nframe.image = b2

    clear1.configure(command=delete1)
    # pas.bind('<Return>', )


def focus(event):
    password.place(x=480, y=350)
    global getotp
    flag = None
    getotp = int(otp.get())
    # cur = con.execute("SELECT * FROM USER")
    result = conn.get('Python/Counter/', '')
    list = str(result).split(':')
    list1 = list[1].split('}')
    counter = int(list1[0])
    count = counter
    mailfetch = str(mailget).split('\n')
    while counter > 0:
        fetchall = conn.get('/Python/User/' + str(counter) + '/', '')
        if int(fetchall['Otp']) == getotp or str(getotp).isnumeric():
                flag = 1
                break
        counter -= 1
    # for i in cur:
    #     if i[1] == getotp and str(getotp).isnumeric():
    #         flag = 1
    #         break
    if flag == 1:
        password.configure(state=NORMAL, fg="black", bg="white")
        password.bind("<FocusIn>", password1)
        if mailget.__contains__(".com"):
            data = {
                'Email': mailfetch[0],
                'Otp': 'null',
                'Password': 'null',
                'Phone': 'null'
            }
            conn.put('/Python/User/', count, data)
            # con.execute("UPDATE USER SET OTP=NULL WHERE MAIL='" + mailget + "'")
            # con.commit()
        else:
            data = {
                'Email': 'null',
                'Otp': 'null',
                'Password': 'null',
                'Phone': phon
            }
            conn.put('/Python/User/',count,data)
            # con.execute("UPDATE USER SET OTP=NULL WHERE PHONE='" + phon + "'")
            # con.commit()
    else:
        if mailget.__contains__(".com"):
            conn.delete('/Python/User/','"'+str(count)+'"')
            conn.put('/Python/Counter/',{'Count':count-1})
            # con.execute("DELETE FROM USER WHERE MAIL = '" + mailget + "'")
            # con.commit()
        else:
            conn.delete('/Python/User/', '"' + str(count) + '"')
            conn.put('/Python/Counter/', {'Count': count - 1})
             # con.execute("DELETE FROM USER WHERE  PHONE = '" + phon + "'")
             # con.commit()
        messagebox.showwarning("OTP Warning", "You must provide Valid OTP in order to continue process")
        a = os.getpid()
        subprocess.Popen('taskkill /F /PID {0}'.format(a),shell=True)
        subprocess.call(["python", "signup.py"])


def otpdef(event):
    otp.delete(0, END)
    blur2 = img1.filter(ImageFilter.BLUR)
    b3 = ImageTk.PhotoImage(blur2)
    newframe.configure(image=b3)
    newframe.image = b3
    otp.configure(fg="black", bg="white")
    otp.bind('<Return>', focus)


def lab():
    subprocess.call(["python", "login.py"])


def enter(event):
    global password, img1, newframe, clear1, next1, otp, mailget, confirmpassword,mailfetch
    mailget = mail.get(1.0, END)
    f = open("Information.txt", 'w')
    f.write(mailget)
    f.close()
    flag = 0
    cursor = con.execute("SELECT * FROM USER")
    result = conn.get('Python/Counter/', '')
    print(result)
    list = str(result).split(':')
    list1 = list[1].split('}')
    counter = int(list1[0])

    while counter > 0:
        print("counter",counter)
        fetchall = conn.get('/Python/User/'+str(counter)+'/', '')
        mailfetch = str(mailget).split('\n')
        if fetchall['Email'].__contains__('@') or (fetchall['Phone'].__len__() -1 == 10 and fetchall['Phone'].isdigit() is True):
            print("mailfetch",str(fetchall['Email']), '\n', mailget)
            if str(fetchall['Email']) == str(mailfetch[0]) or str(fetchall['Phone']) == str(mailfetch[0]):
                print("Enter")
                flag = 1
                break
            else:
                flag = 0
        counter -= 1
    # for i in cursor:
    #     print(i)
    #     if str(i[0]) == mailget or str(i[3]) == mailget:
    #         print("enter")
    #         flag = 1
    #         break
    #     else:
    #         flag = 0

    if flag == 1:
        messagebox.showerror("Invalid Credentials", "User already exist")
        ans = messagebox.askyesno("Login", "Do you want to log in instead ?")
        if ans is True:
            root.destroy()
            subprocess.call(["Python", "login.py"])

    if flag == 0:

        msg = str(random.randint(123456, 987654))
        message = "OTP for your login is " + msg + " please enter otp for your " \
                                                   "authentication and further procedure"

        if mailget.__contains__(".com"):
            s.login('rathodajay1202@gmail.com', 'ajay2715122002')
            result = conn.get('Python/Counter/', '')
            print(result)
            list = str(result).split(':')
            list1 = list[1].split('}')
            counter = int(list1[0])
            counter += 1
            cnt = 'Counter/'
            result = conn.put('/Python/', cnt, {'Count':counter})
            email = mailget.split('\n')
            data = {
                'Email': email[0],
                'Otp': msg,
                'Password': 'null',
                'Phone': 'null'
            }

            conn.put('/Python/User/',counter,data)
            # con.execute("INSERT INTO USER(MAIL,OTP,PASSWORD) values('" + mailget + "','" + msg + "',NULL)")
            # con.commit()
            # result = conn.get('/Count/','')
            # print("result",result)
            #result.
            s.sendmail('rathodajay1202@gmail.com', mailget, message)
            s.quit()
        else:
            '''
            go to sms4india.com
            do new registration 
            then login in your account 
            click on the API column there u will get your apikey and secret key
            '''
            global phon

            URL = 'https://www.sms4india.com/api/v1/sendCampaign'

            # get request
            phon = mailget

            def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
                req_params = {
                    'apikey': '0FQ3SRUDOHEZAPFZM1BHA4IH6DOL0EUU',
                    'secret': 'TYLQ7H3DTCLOXRFX',
                    'usetype': useType,
                    'phone': phon,
                    'message': message,
                    'senderid': senderId
                }
                return requests.post(reqUrl, req_params)

            """
              Note:-
                    u just have to make some changes in these specific blocks 
                correctly copy paste your apikey (at XXXXXX) and secret key (at ZZZZZZZ) in specific blocks
                Type phone number of recepient (at 0000000)
                    don't make change in the 'stage' block 

            """
            # get response
            response = sendPostRequest(URL, '0FQ3SRUDOHEZAPFZM1BHA4IH6DOL0EUU', 'TYLQ7H3DTCLOXRFX', 'stage',
                                       '7972526888',
                                       'rathodajay1202@gmail.com', message)
            result = conn.get('Python/Counter/','')
            list = str(result).split(':')
            list1 = list[1].split('}')
            counter = int(list1[0])
            counter += 1
            cnt = 'Counter/'
            result = conn.put('/Python/', cnt, {'Count': counter})
            email = mailget.split('\n')
            data = {
                'Email': 'null',
                'Otp': msg,
                'Password': 'null',
                'Phone': phon
            }

            conn.put('/Python/User/', counter, data)
            # con.execute("INSERT INTO USER(PHONE,OTP,PASSWORD) values('" + phon + "','" + msg + "',NULL)")
            # con.commit()
            # print response if you want

        img1 = Image.open("tower.jpg")
        imag2 = ImageTk.PhotoImage(img1)
        root1 = Toplevel(root)
        w1, h1 = root.winfo_screenwidth(), root1.winfo_screenheight()
        root1.geometry("%dx%d+0+0" % (w1, h1))

        newframe = Label(root1, image=imag2)
        newframe.image = imag2

        password = Entry(newframe, bd=0, bg="black", insertwidth=1, font=('calibri', 16))
        password.insert(0, 'Enter Password')
        password.configure(foreground="white", state=DISABLED)

        otp = Entry(newframe, bd=0, bg="black", insertwidth=1, font=('calibri', 16))
        otp.insert(0, 'Enter OTP')
        otp.configure(foreground="white")
        otp.bind('<FocusIn>', otpdef)

        clear1 = Button(newframe, font=('calibri', 10), bg="black", fg="white", text="x", bd=0)
        next1 = Button(newframe, font=('calibri', 10), text="→", bg="gray", fg="white")
        clear1.bind("<Enter>", log)
        clear1.bind("<Leave>", logo)
        next1.bind("<Enter>", log1)
        next1.bind("<Leave>", logo1)
        newframe.pack(fill='both', expand=True)
        otp.place(x=480, y=300)


def show(eve):
    if eve == "gmail":
        mail.insert(INSERT, "gmail.com")
    if eve == "hotmail":
        mail.insert(INSERT, "hotmail.com")
    if eve == "yahoo":
        mail.insert(INSERT, "yahoo.com")
    if eve == "email":
        mail.insert(INSERT, "email.com")


def pop(event):
    global popup
    popup = Menu(root, tearoff=0, bg="black", fg="white", bd=0)
    popup.add_command(label="gmail.com", command=lambda: show("gmail"))
    popup.add_command(label="hotmail.com", command=lambda: show("hotmail"))
    popup.add_command(label="yahoo.com", command=lambda: show("yahoo"))
    popup.add_command(label="email.com", command=lambda: show("email"))
    try:
        popup.tk_popup(725, 540, 1)
    finally:
        popup.grab_release()


def entry(event):
    ls = mail.index(INSERT)
    if mail.get("%s-1c" % ls, ls) == "@":
        emailpopup.config(text="⌄", fg="black", bg="white")
        emailpopup.bind('<Enter>', pop)
        emailpopup.place(x=725, y=454)
    if mail.get(1.0).isalpha():
        try:
            mobilenumber.destroy()
        except:
            pass
    if not mail.get(1.0, END).__contains__("@"):
        try:
            emailpopup.destroy()
        except:
            pass
        else:
            pass
            # arr = Button(root, font=("Calibri", 10), bg="white", fg="black", bd=0)

    if mail.get(1.0).isdigit():
        mobilenumber.config(bg="white", fg="black")
        # num.bind("<Enter>", pop1)
        mobilenumber.place(x=453, y=453)


def placeholder(event):
    mail.configure(state=NORMAL, background="white", fg="black", highlightcolor="yellow")
    hintlabel = Label(root, text="Enter username or Phone Number →", fg="white", bg="black", font=("Times New Roman", 10))
    clear.configure(bg="white", fg="black")
    next.configure(bg="gray", fg="white")
    mail.delete(1.0, END)

    blur = img.filter(ImageFilter.BLUR)
    bl = ImageTk.PhotoImage(blur)
    frame.configure(image=bl)
    frame.image = bl
    clear.bind("<Enter>", log)
    clear.bind("<Leave>", logo)
    clear.configure(command=delete)
    next.bind("<Enter>", log1)
    next.bind("<Leave>", logo1)
    next.configure(command=enter)
    mail.bind("<KeyRelease>", entry)
    mail.bind("<Return>", enter)
    hintlabel.place(x=481, y=432)


if __name__ == '__main__':
    global mailget
    retry = True
    while (retry):
        try:
            s = smtplib.SMTP("smtp.gmail.com", 587)
            s.starttls()
        except:
            retry = messagebox.askretrycancel("Error",
                                              "OOPS!, you are not connected to internet Please,try again later")
            print(retry)
        else:
            retry = False

            con = sqlite3.connect("UserData")
            authentication = firebase.FirebaseAuthentication('lFTDGhEV8Qy9PxYiA4mMJXWM3sJbTCAq7bTlB8FG', 'missionprojects2020@gmail.com')
            conn = firebase.FirebaseApplication("https://programming-aa2cb.firebaseio.com/", authentication)
            #conn.post('/Python/', 'Users')
            # data = {
            #     'Count' : 0
            # }
            # cnt = 'Counter/'
            # conn.put('/Python/',cnt,{'Count':0})
            # print(result)
            #con = cur.cursor()
            query = "CREATE TABLE IF NOT EXISTS USER(MAIL VARCHAR2(25) PRIMARY KEY,OTP INT(6) " \
                    ",PASSWORD VARCHAR2(20),PHONE INTEGER(10))"
            con.execute(query)
            con.commit()
            root = Tk()
            root.title("Login form")
            w, h = root.winfo_screenwidth(), root.winfo_screenheight()
            root.geometry("%dx%d+0+0" % (w, h))

            img = Image.open("mountain.jpg")
            imag = ImageTk.PhotoImage(img)
            frame = Label(root, image=imag)
            frame.Image = imag

            mail = Text(frame, height=1, width=27, bd=0, bg="black", insertwidth=1, font=('calibri', 16))
            mail.insert(1.0, 'Enter user ID or phone Number')
            mail.configure(foreground="white")

            clear = Button(root, font=('calibri', 10), bg="black", fg="white", text="x", bd=0)
            next = Button(root, font=('calibri', 10), text="→", bg="gray", fg="white")
            emailpopup = Button(root, font=("Calibri", 10), bg="white", fg="black", bd=0)
            mobilenumber = Button(root, text="+91", font=("Times New Roman", 11), bg="black", fg="black", bd=0)

            mail.bind("<FocusIn>", placeholder)
            frame.pack(fill='both', expand=TRUE)

            mail.place(x=480, y=450)
            clear.place(x=740, y=453)
            next.place(x=756, y=453)
            # lb.place(x=540,y=500)
            root.mainloop()
