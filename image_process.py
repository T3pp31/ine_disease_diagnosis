import keras
import sys,os
import numpy as np
from keras.models import load_model
from PIL import Image


imsize=(200,200)
def examine_ine(image):

	classes=['healthy','unhealthy']

	imsize=(200,200)

	img=Image.open(image)
	img=img.convert('RGB')
	img=img.resize(imsize)


	img = np.asarray(img)

# モデルの読み込み，重み付け
	model = load_model('model1.h5')
# 予測結果の出力
	prd = model.predict(np.array([img]))
	prelabel=np.argmax(prd)
	print('prelabel',prelabel)
	prelabel=classes[prelabel]

	

	print('prd',prd)
	print('prelabel',prelabel)





	return prd*100

