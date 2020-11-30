from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter
import sqlite3
import smtplib
import subprocess

from firebase import firebase

global retry
retry = True
while retry:
    try:
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
    except :
        retry = messagebox.askretrycancel("Error", "OOPS!, you are not connected to internet Please,try again later")
        print(retry)
    else:
        retry = False
        # con = sqlite3.connect("UserData")
        authentication = firebase.FirebaseAuthentication('lFTDGhEV8Qy9PxYiA4mMJXWM3sJbTCAq7bTlB8FG',
                                                         'missionprojects2020@gmail.com')
        conn = firebase.FirebaseApplication("https://programming-aa2cb.firebaseio.com/", authentication)
        rootconnect = Tk()
        w, h = rootconnect.winfo_screenwidth(), rootconnect.winfo_screenheight()
        rootconnect.geometry("%dx%d+0+0" % (w, h))
        rootconnect.title("Connection")

        img = Image.open("icemountain.jpg")
        image = ImageTk.PhotoImage(img)
        frame = Label(rootconnect, image=image)
        frame.Image = image
        r = open("information.txt", 'r')
        getmailfromsignup = str(r.readline())
        getpasswordfromsignup = str(r.readline())
        r.close()
        print(getpasswordfromsignup)
        mail1 = Text(frame, height=1, width=27, bd=0, bg="black", insertwidth=1, font=('calibri', 16))
        if getmailfromsignup.__contains__("@"):
            mail1.insert(1.0, 'Enter Your phone Number')
        else:
            mail1.insert(1.0, 'Enter Your User ID')
        mail1.configure(foreground="white")

        click = Button(rootconnect, font=('calibri', 10), bg="black", fg="white", text="x", bd=0)
        nextbutton = Button(rootconnect, font=('calibri', 10), text="→", bg="gray", fg="white")


        def enter1(event):
            if getmailfromsignup.__contains__("@"):
                try:
                    get = int(mail1.get(1.0, END))
                except ValueError:
                    messagebox.showwarning("Error", "Enter Valid Mobile Number")
                else:
                    if mail1.get(1.0, END).__len__() - 1 == 10:
                        phone = mail1.get(1.0, END)
                        result = conn.get('Python/Counter/', '')
                        list = str(result).split(':')
                        list1 = list[1].split('}')
                        counter = int(list1[0])
                        fetchmail = str(phone).split('\n')
                        data = {
                            'Email': getmailfromsignup,
                            'Otp': 'null',
                            'Password': getpasswordfromsignup,
                            'Phone': fetchmail[0]
                        }
                        conn.put('/Python/User/', counter, data)
                        # con.execute("UPDATE USER SET PHONE = '" + phone + "' WHERE MAIL = '" + getmailfromsignup + "'")
                        # con.commit()
                        messagebox.showinfo("Success", "Your phone Number is successfully linked with your main ID")

                        ans = messagebox.askyesno("PyVM - Face Recognition", "Do you want to Add your Face Unlock ?")
                        if ans:
                            messagebox.showwarning("PyVM - Face Recognition",
                                                   "1] Press Return key to Register your Face\n"
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
                            rootconnect.destroy()
                            subprocess.call(["Python", "insert image into DB.py"])
                        else:
                            rootconnect.destroy()
                            subprocess.call(["Python", "main_GUI.py"])
                    else:
                        messagebox.showerror("Error", "OOPS! Enter valid 10 digit Mobile Number")
            try:
                getmail = int(getmailfromsignup)
            except:
                pass
            else:
                if mail1.get(1.0, END).__contains__("@"):
                    mailget = mail1.get(1.0, END)
                    fetchmail = str(mailget).split('\n')
                    data = {
                        'Email': fetchmail[0],
                        'Otp': 'null',
                        'Password': getpasswordfromsignup,
                        'Phone': getmailfromsignup
                    }
                    conn.put('/Python/User/', counter, data)
                    # con.execute("UPDATE USER SET MAIL = '"+ mailget +"'  WHERE PHONE = '"+ getmailfromsignup +"'")
                    # con.commit()
                    messagebox.showinfo("Success", "Your Mail ID is successfully linked with your Phone Number")

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
                        rootconnect.destroy()
                        subprocess.call(["Python", "insert image into DB.py"])
                    else:
                        rootconnect.destroy()
                        subprocess.call(["Python", "main_GUI.py"])
                else:
                    messagebox.showerror("Error", "OOPS! Enter valid Email Address")

        def delete1():
            mail1.delete(1.0, END)


        def log1(ev):
            global lab
            lab = Label(rootconnect, text="Clear", bg="black", fg="white")
            lab.place(x=480, y=430)


        def log11(ev):
            global lab1
            lab1 = Label(rootconnect, text="Click to Proceed", bg="black", fg="white")
            lab1.place(x=480, y=430)


        def logo11(ev):
            lab1.destroy()


        def logo1(ev):
            lab.destroy()


        def placeholder(event):
            mail1.configure(state=NORMAL, background="white", fg="black", highlightcolor="yellow")
            lb = Label(rootconnect, text="Enter username or Phone Number →", fg="white", bg="black",
                       font=("Times New Roman", 10))
            click.configure(bg="white", fg="black")
            nextbutton.configure(bg="gray", fg="white")
            mail1.delete(1.0, END)

            blur = img.filter(ImageFilter.BLUR)
            bl = ImageTk.PhotoImage(blur)
            frame.configure(image=bl)
            frame.image = bl
            click.bind("<Enter>", log1)
            click.bind("<Leave>", logo1)
            click.configure(command=delete1)
            nextbutton.bind("<Enter>", log11)
            nextbutton.bind("<Leave>", logo11)
            nextbutton.configure(command=enter1)
            mail1.bind("<Return>", enter1)
            lb.place(x=481, y=432)


        mail1.bind("<FocusIn>", placeholder)
        frame.pack(fill='both', expand=TRUE)

        mail1.place(x=480, y=450)
        click.place(x=740, y=453)
        nextbutton.place(x=756, y=453)
        # lb.place(x=540,y=500)
        rootconnect.mainloop()
