from flask import Flask, render_template,request
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import load_model
import numpy as np
from image_process import examine_ine
from datetime import datetime
import os 
import cv2
import pandas as pd
from PIL import Image

app=Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def upload_file():
	if request.method=='GET':
		return render_template('index.html')

	if request.method=="POST":
		#uploadファイルの保存
		f=request.files['file']
		filepath='./static/'+datetime.now().strftime("%Y%m%d%H%M%S")+'.png'
		f.save(filepath)



		#健康を調べる関数の実行
		result = examine_ine(filepath)
		print(result)
		print('result')



		return render_template('index.html',filepath=filepath,
		result=result)

if __name__=='__main__':
	app.debug=True
	app.run(host='0.0.0.0',port=5000)
