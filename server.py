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

