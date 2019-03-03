import cv2,os
import numpy as np
from PIL import Image
import sqlite3

rec = cv2.createLBPHFaceRecognizer()
rec.load("recognizer\\trainingData..yml")
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
path = "dataSet"

def getProfile(id):
    conn = sqlite3.connect("faceBase1.db")
    cmd = "SElECT * FROM People WHERE ID="+str(id)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile


cam = cv2.VideoCapture(0);
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4) #creates a font

while(True):
    ret,img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)
        id, conf = rec.predict(gray[y:y+h,x:x+w])
        profile = getProfile(id)
        if(profile!=None):
            cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[1]),(x,y+h+30),font,255) #Draw the text
    cv2.imshow("Face", img)
    if(cv2.waitKey(1) == ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
