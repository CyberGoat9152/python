#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
webcam = cv2.VideoCapture(0)
identidade = input("digite o id da pessoa: ")
cont = 0
while True:
    ret, frame = webcam.read()
    frame_pretobranco = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rosto = face_cascade.detectMultiScale(frame_pretobranco, 1.3 , 7)
    for (x, y, w, h) in rosto:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.imwrite("data/data."+identidade+"."+str(cont)+".jpg",cv2.resize(frame_pretobranco[y:y+h, x:x+w], (50,50)))
        print("{} imagens salvas".format(cont+1))
        cont += 1
    cv2.imshow("cria base", frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
    elif(cont >= 500):
        break
webcam.release()
cv2.destroyAllWindows()
