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

# モデルの読み込み，重み付け
	model = load_model('model1.h5')
	model.load_weights('model1.h5')
# 予測結果の出力
	prd = model.predict(np.array([img]))
	prelabel=np.argmax(prd)
	print(prd)
	print(prelabel)





	return prd

