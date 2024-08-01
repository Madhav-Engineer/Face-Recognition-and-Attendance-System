import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'imageattendence'
images = []
classNames = []
myList = os.listdir(path)
print(myList)

# Remove extensions from filenames
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')  # imread loads an image from the specified path
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])  # separating extension
print(classNames)

# Function to find encodings
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # convert to RGB
        encode = face_recognition.face_encodings(img)
        if encode:  # Ensure that face encodings are not empty
            encodeList.append(encode[0])
    return encodeList

# Function to mark attendance with timestamp
def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()  # return each line in the file as a list item
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            time_now = datetime.now()
            tString = time_now.strftime('%H:%M:%S')
            dString = time_now.strftime('%d/%m/%Y')
            f.writelines(f'\n{name},{tString},{dString}')

encodeListKnown = findEncodings(images)
print('Encoding Complete')

# For webcam capture
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()  # returns true if the frame is available
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)  # reducing size of image showing in webcam for speeding the process
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)  # converting to RGB

    facesCurFrame = face_recognition.face_locations(imgS)  # find location of faces in current frame
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)  # find the encodings of faces shown in webcam

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):  # grab one face location from facesCurFrame list & grab encoding of encodeFace from encodesCurFrame
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)  # check matching
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)  # find face distance
        
        if len(faceDis) > 0:  # Ensure faceDis is not empty
            print(faceDis)  # show number of distances, where n = number of images, lowest distance is the match
            matchIndex = np.argmin(faceDis)
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4  # regain the size of webcam image

                # For creating rectangle around the recognized face
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 250, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)  # for displaying the name inside bounding box
                markAttendance(name)

    cv2.imshow('webcam', img)
    if cv2.waitKey(10) & 0xFF == 27:  # 27 is the ASCII code for the ESC key
        break

cap.release()
cv2.destroyAllWindows()
