import cv2
import os
import numpy as np
import time

def obtenerModelo(method,facesData,labels):
	if method == 'EigenFaces': emotion_recognizer = cv2.face.EigenFaceRecognizer_create() #This method is for face recognition using EigenFaces algorithm that is based on the PCA (Principal Component Analysis) technique.
	if method == 'FisherFaces': emotion_recognizer = cv2.face.FisherFaceRecognizer_create()#This method is for face recognition using FisherFaces algorithm that is based on the LDA (Linear Discriminant Analysis) technique.
	if method == 'LBPH': emotion_recognizer = cv2.face.LBPHFaceRecognizer_create()#This method is for face recognition using Local Binary Patterns Histograms (LBPH) algorithm that is based on the Histogram of Oriented Gradients (HOG) technique.

	# Entrenando el reconocedor de rostros
	print("Entrenando ( "+method+" )...")
	inicio = time.time()
	emotion_recognizer.train(facesData, np.array(labels))
	tiempoEntrenamiento = time.time()-inicio
	print("Tiempo de entrenamiento ( "+method+" ): ", tiempoEntrenamiento)

	# Almacenando el modelo obtenido
	emotion_recognizer.write("EmotionRecognition/Models/modelo"+method+".xml")

dataPath = 'EmotionRecognition/Data' 
emotionsList = os.listdir(dataPath)
print('Lista de personas: ', emotionsList)

labels = []
facesData = []
label = 0

for nameDir in emotionsList:
	emotionsPath = dataPath + '/' + nameDir

	for fileName in os.listdir(emotionsPath):
		#print('Rostros: ', nameDir + '/' + fileName)
		labels.append(label)
		facesData.append(cv2.imread(emotionsPath+'/'+fileName,0))
		#image = cv2.imread(emotionsPath+'/'+fileName,0)
		#cv2.imshow('image',image)
		#cv2.waitKey(10)
	label = label + 1

obtenerModelo('EigenFaces',facesData,labels)
obtenerModelo('FisherFaces',facesData,labels)
obtenerModelo('LBPH',facesData,labels)
