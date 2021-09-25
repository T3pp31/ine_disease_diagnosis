import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

#学習用データが足りない時に使う
def dilution_img(input_img):
	
	#画像のサイズ
	img_size = input_img.shape
	filter_one = np.ones([3,3])

	#回転用
	mat_1 = cv2.getRotationMatrix2D(tuple(np.array(input_img.shape[:2])/2),23,1)
	mat_2 = cv2.getRotationMatrix2D(tuple(np.array(input_img.shape[:2])/2),144,0.8)

	fake_method_array = np.array([
		lambda image: cv2.warpAffine(image,mat_1,image.shape[:2]),
		lambda image: cv2.warpAffine(image,mat_2,image.shape[:2]),
		lambda image: cv2.threshold(image,100,255,cv2.THRESH_TOZERO)[1],
		lambda image: cv2.GaussianBlur(image,(5,5),0),
		lambda image: cv2.resize(cv2.resize(image,(img_size[1])//5,img_size[1],img_size[0])),
		lambda image: cv2.erode(image,filter_one),
		lambda image: cv2.flip(image,1)
	])

	images=[]

	for method in fake_method_array:
		faked_img = method(input_img)
		images.append(faked_img)

	return images

#画像読み込み	
target_img = cv2.imread('example.jpg')
#画像水増し
fake_images = dilution_img(target_img)

if not os.path.exists('dilution_img'):
	os.mkdir('dilution_img')

for number,img in enumerate(fake_images):
	cv.imwrite('dilution_img/'+ str(number)+'.jpg',img)
