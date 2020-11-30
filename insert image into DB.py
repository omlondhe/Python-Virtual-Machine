import cv2
import subprocess
import sqlite3

con = sqlite3.connect("face_recognition")
cur = con.cursor()
con.execute('CREATE TABLE IF NOT EXISTS registered_faces(user varchar(50), image BLOB);')


def cv():
    r = open("information.txt", 'r')
    getmailfromsignup = str(r.readline()).rsplit('@')[0]
    r.close()

    def update_db():
        face = open("img.jpg", 'rb')
        img = face.read()
        print(img)
        cur.execute("INSERT INTO registered_faces values(?,?);", (getmailfromsignup, img))
        con.commit()
        subprocess.call(["Python", "login.py"])

    def add_face():
        cv2.imwrite("img.jpg", frame)
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


cv()
