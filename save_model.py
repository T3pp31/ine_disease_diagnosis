import glob
import numpy as np
import pandas as pd

#kerasのload_imgには手動でpillowを入れる必要がある
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow.keras.applications.inception_v3 import InceptionV3,preprocessing_input
from tensorflow.keras.models import Model
from tensorflor.keras.layers import Dense
from sklearn.model_selection import train_test_split

x_size = 299
y_size = 299
kind_label = []
healty_img = []

ine_list = ['healthy','unhealthy']

f = open('ine_list.txt','w')
for x in ine_list:
	f.write(str(x)+'\n')
f.close()

#データのロードセット
for ine_healthy in ine_list:
	file_list = glob.glob()
