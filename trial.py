import cv2
import sqlite3
from tkinter import *

con = sqlite3.connect("face_recognition")
cur = con.cursor()
con.execute('CREATE TABLE IF NOT EXISTS registered_faces(user varchar(50), image BLOB);')


def cv():
    name = user.get()

    def update_db():
        face = open("img.jpg", 'rb')
        img = face.read()
        print(img)
        cur.execute("INSERT INTO registered_faces values(?,?);", (name, img))
        con.commit()

    def add_face():
        cv2.imwrite("img.jpg", frame)
        root.destroy()
        cv2.destroyAllWindows()
        update_db()

    video = cv2.VideoCapture(0)
    while True:
        ret, frame = video.read()
        cv2.imshow("Face registration", frame)

        b = cv2.waitKey(1)
        if b == ord('\r'):
            add_face()
            break
        if b & 0xFF == ord('q'):
            break


root = Tk()

user_lbl = Label(root, text="Enter your Username : ")
user_lbl.grid(row=0, column=0)

user = Entry(root)
user.grid(row=0, column=1)

but = Button(root, text="Add Face", command=cv)
but.grid(row=1, column=0)

root.mainloop()
