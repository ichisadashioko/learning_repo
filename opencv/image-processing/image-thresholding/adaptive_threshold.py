import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudoku.png',0)
img = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
# img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow('original',img)
cv2.imshow('Global Thresholding (v = 17)',th1)
cv2.imshow('Adaptive Mean Thresholding',th2)
cv2.imshow('Adaptive Gaussian Thresholding',th3)

cv2.waitKey(0)
cv2.destroyAllWindows()