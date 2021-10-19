import keras
import sys,os
import numpy as np
from keras.models import load_model
from PIL import Image

def examine_ine(image):
	imsize=(200,200)

	img=Image.open(image)

	img=img.resize(imsize)

	img = np.asarray(img)
	img=img/255.0

	model = load_model('model1.h5')
	model.load_weights('model1.h5')
	prd = model.predict(np.array([img]))
	print(prd)
	prelabel = np.argmax(prd, axis=1)
	print(prelabel)

	if prelabel == 0:
		print(">>> healthy")
	elif prelabel == 1:
		print(">>> unhealthy")

	return prd

