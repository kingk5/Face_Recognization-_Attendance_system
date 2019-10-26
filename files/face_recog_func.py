import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time import time
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.decomposition import PCA
from sklearn.svm import SVC
import cv2
import os


#data read

def datapreprocessing():

    faces = []
    faceID = []
    
    
    for path,subdirnames,filenames in os.walk('H:/work/opencv/another/Training'):
        for filename in filenames:
            if filename.startswith("."):
                print("skipping system file")
                continue
            id = os.path.basename(path)
            img_path=os.path.join(path,filename)
            print("img_path",img_path)
            print("id",id)
            test_img = cv2.imread(img_path)
            #test_img = cv2.resize(test_img, (1000,700))
            if test_img is None:
                print("image not loaded properly")
                continue
            faces_rect,gray_img=face_detection(test_img)
            if len(faces_rect)!=1:
                continue
            (x,y,w,h) = faces_rect[0]
            roi_gray = gray_img[y:y+w,x:x+h]

            faces.append(roi_gray)
            faceID.append(int(id))

    return faces,faceID


def test_img_preprocessing(img):
    
    test_img = cv2.imread(img,0)
    
    #test_img = cv2.resize(test_img, (1000,700))

    return test_img

def model_train(faces, faceID):
    face_recogniser=cv2.face.LBPHFaceRecognizer_create();
    face_recogniser.train(faces,np.array(faceID))
    #face_recogniser.save('recognizer/trainningData.yml')
    return face_recogniser
    
def face_detection(img):
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_haar_cascade = cv2.CascadeClassifier('H:/work/opencv/pca/Haarcascade/haarcascade_frontalface_default.xml')
    faces = face_haar_cascade.detectMultiScale(img,scaleFactor=1.3,minNeighbors=5)
    
    return faces,gray_img
