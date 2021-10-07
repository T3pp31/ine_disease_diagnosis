import keras
import sys,os
import numpy as np
from keras.models import load_model
from PIL import Image
import cv2
def examine_ine(image,model,ine_list):
	imsize=(200,200)

	img = Image.open(image)
	img=img.convert('RGB')

	img=img.resize(imsize)

	img = np.asarray(img)
	img=img/255.0

	model = load_model(model)

	prd = model.predict(np.array([img]))
	print(prd)
	prelabel = np.argmax(prd, axis=1)

	if prelabel == 0:
		print(">>> healthy")
	elif prelabel == 1:
		print(">>> unhealthy")

	return prelabel

