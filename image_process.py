import keras
import sys,os
import numpy as np
from keras.models import load_model

def examine_ine(image,model,ine_list):
	imsize=(200,200)
	exam_pic = image
