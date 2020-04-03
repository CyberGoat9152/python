#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
recognizer = cv2.face.createEigenFaceRecognizer()
recognizer.load("TrainingData.xml")

lid = {
	1:'arthur'
}




def main():
	face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
	webcam = cv2.VideoCapture(0)
	while True:
		_, frame = webcam.read()
		frame_pretobranco = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		rosto = face_cascade.detectMultiScale(frame_pretobranco, 1.3 , 7)
		for (x, y, w, h) in rosto:
			cv2.rectangle(frame, (x,y), (x+w,y+h), (225,105,65), 2)
			rosto = cv2.resize(frame_pretobranco[y:y+h, x:x+w], (50,50))
			pred = recognizer.predict(rosto)
			print(pred)
			if (pred[1] < 2300):
				cv2.putText(frame, lid[pred[0]], (x + 50,y + h + 25 ), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (225, 105, 65), 1, cv2.LINE_AA )
		cv2.imshow("Reconhecimento", frame)
		if(cv2.waitKey(1) & 0xFF == ord('q')):
			break
	webcam.release()
	cv2.destroyAllWindows()
	return 0



if __name__ == "__main__":
	main()
