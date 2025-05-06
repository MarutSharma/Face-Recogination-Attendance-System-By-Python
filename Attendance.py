from copyreg import dispatch_table
import pickle

import cv2
import os
import csv
import time
from datetime import datetime 
from sklearn.neighbors import KNeighborsClassifier

from win32com.client import Dispatch
def speak(str1):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('data\haarcascade_frontalface_default.xml')

with open('data/names.pkl', 'rb') as f:
    LABELS = pickle.load(f)
    with open('data/faces_data.pkl', 'rb') as f:
        FACES = pickle.load(f)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

imgBackground=cv2.imread("background.png")
COL_NAME = {'Name': [], 'Date': [], 'Time': []}

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        crop_img = frame[y:y + h, x:x + w, :]
        resize_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
        output = knn.predict(resize_img)
        ts=time.time()
        date=datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
        timestamp = datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        exist=os.path.isfile("Attendance/Attendance_"+date+".csv")
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y - 40), (x + w, y), (0, 255, 0), -1)
        cv2.putText(frame, str(output[0]), (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
        attendance = [str(output[0]), str(timestamp)]
        imgBackground[162:162 + 480, 55:55 + 640] = frame
    cv2.imshow('Video', imgBackground)
    k = cv2.waitKey(1)
    if k==ord('o' or 'O'):
        speak("Attendance is marked !")
        time.sleep(5)        
        if exist:
            with open("Attendance/Attendance_"+date+".csv", '+a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(attendance)
                csvfile.close()
        else:
            with open("Attendance/Attendance_"+date+".csv", '+a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(COL_NAME)
                writer.writerow(attendance)
                csvfile.close()
    if k == ord('q' or 'Q'):
        break
video.release()
cv2.destroyAllWindows()
