import cv2
import face_recognition
import numpy as np
import sqlite3
import subprocess

con = sqlite3.connect("face_recognition")
cur = con.cursor()

known_face_encodings = []
count = 1

r = open("information.txt", 'r')
getmailfromsignup = str(r.readline()).rsplit('@')[0]
print(getmailfromsignup)
r.close()

try:
    c = cur.execute("SELECT * FROM registered_faces WHERE user=(?);", (getmailfromsignup,))
    for i in c:
        stored_image = open("image.jpg", 'wb')
        stored_image.write(i[1])
        img = face_recognition.load_image_file("image.jpg")
        known_img = face_recognition.face_encodings(img)[0]
        known_face_encodings.append(known_img)

    # Initialize some variables
    face_locations = []
    face_encodings = []
    process_this_frame = True

    video = cv2.VideoCapture(0)
    while True:
        ret, frame = video.read()
        # cv2.imshow("", frame)
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    video.release()
                    cv2.destroyAllWindows()
                    subprocess.call(["Python", "main_GUI.py"])

        process_this_frame = not process_this_frame
        cv2.imshow("", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
except:
    pass
