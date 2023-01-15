import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

#os.startfile("C:\Program Files (x86)\Iriun Webcam\IriunWebcam.exe")

path = 'attendence'
images = []
classNames = []
mylist = os.listdir(path)
print(mylist)

for cl in mylist:
    curimg = cv2.imread(f'{path}/{cl}')
    images.append(curimg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findencodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendence(name):
    with open('Attendence.csv','r+') as f:
        myDatalist = f.readlines()
        nameList=[]
        # print(myDatalist)
        for line in myDatalist:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString},{now}')


encodeListknown = findencodings(images)
print(len(encodeListknown))

cap = cv2.VideoCapture(0)

THRESHOLD = 0.45

while True:
    sucess, img = cap.read()
    imgs = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

    facescurframe = face_recognition.face_locations(imgs)
    encodescurframe = face_recognition.face_encodings(imgs, facescurframe)

    for encodeface, faceloc in zip(encodescurframe, facescurframe):
        facedis = face_recognition.face_distance(encodeListknown, encodeface)
        matchIndex = np.argmin(facedis)
        matchDistance = facedis[matchIndex]

        if matchDistance < THRESHOLD:
            matchs = True
        else:
            matchs = False

        if matchs:
            name = classNames[matchIndex].upper()
            y1, x2, y2, x1 = faceloc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255.0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendence(name)

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)
