# /utils/preprocessing.py
import numpy as np
import cv2

def preprocess_input(x):
    x = x.astype('float32')
    x = x / 255.0
    x = x - 0.5
    x = x * 2.0
    return x
