#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
recognizer = cv2.face.createEigenFaceRecognizer()
recognizer.load("TrainingData.xml")
def main():
	face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
	webcam = cv2.VideoCapture(0)
	while True:
		_, frame = webcam.read()
		frame_pretobranco = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		rosto = face_cascade.detectMultiScale(frame_pretobranco, 1.3 , 7)
		for (x, y, w, h) in rosto:
			cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
			rosto = cv2.resize(frame_pretobranco[y:y+h, x:x+w], (50,50))
			print(recognizer.predict(rosto))
			if (recognizer.predict(rosto)[0] == 1) and (recognizer.predict(rosto)[1] < 1100):
				cv2.putText(frame, "papa", (x + 50,y + h + 5 ), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1, cv2.LINE_AA )
			if (recognizer.predict(rosto)[0] == 2) and (recognizer.predict(rosto)[1] < 1100) :
				cv2.putText(frame, "heteroTop", (x + 86,y + h + 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1, cv2.LINE_AA )
			print(recognizer.predict(rosto))
			
		cv2.imshow("Reconhecimento", frame)
		if(cv2.waitKey(1) & 0xFF == ord('q')):
			break
	webcam.release()
	cv2.destroyAllWindows()
	return 0



if __name__ == "__main__":
	main()
