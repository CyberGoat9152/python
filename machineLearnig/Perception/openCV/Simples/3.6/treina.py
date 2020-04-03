#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np
from PIL import Image
recognizer = cv2.face.createEigenFaceRecognizer()
path = "data"
def getImagesWithID(path):
    """
        recebe o nome da pasta onde as fotos estao e retorna uma tupla sendo:
            [0] -array ids
            [1] -vetor arrays faces            
    """
    faces = []
    IDs = []
    imagesPaths = [ os.path.join(path, f) for f in os.listdir(path) ]
    for imagespath in imagesPaths:
        faceImage = Image.open(imagespath).convert("L")
        facenp = np.array(faceImage, "uint8")
        ID = int(os.path.split(imagespath)[1].split(".")[1])
        faces.append(facenp)
        IDs.append(ID)
    return np.array(IDs), faces
IDs, faces = getImagesWithID(path)
recognizer.train(faces, IDs)
recognizer.save("TrainingData.xml")
