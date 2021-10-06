from flask import Flask, render_template,request
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import load_model
import numpy as np
from image_process import examine_ine
from datetime import datetime
import os 
import cv2
import pandas as pd

app=Flask(__name__)

model = load_model('model1.h5')

ine_list=[]
with open('ine_list.txt') as f:
	ine_list=[s.strip() for s in f.readlines()]

print('== ine_list ==')
print(ine_list)

@app.route('/',methods=['GET', 'POST'])
def upload_file():
	if request.method=='GET':
		return render_template('index.html')

	if request.method=="POST":
		#uploadファイルの保存
		f=request.files['file']
		filepath='./static/'+datetime.now().strftime("%Y%m%d%H%M%S")+'.png'
		f.save(filepath)

		#画像の読み込みとリサイズ
		input_img=load_img(filepath,target_size=(200,200))

		#健康を調べる関数の実行
		result = examine_ine(input_img,model,ine_list)
		print('result')
		print(result)

		no1_ine=result[0,0]

		no1_ine_pred=result[0,1]

		return render_template('index.html',filepath=filepath,
		no1_ine=no1_ine,no1_ine_pred=no1_ine_pred)

if __name__=='__main__':
	app.debug=True
	app.run(host='localhost',port=5000)
