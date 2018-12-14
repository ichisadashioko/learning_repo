# CLAHE (Constrast Limited Adaptive Histogram Equalization)
import cv2
import numpy as np

img = cv2.imread('edelgard.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# create a CLAHE object (Arguments are optional)
clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
cl1 = clahe.apply(gray)

img2 = cv2.equalizeHist(gray)

cv2.imshow('original',img)
cv2.imshow('gray',gray)
cv2.imshow('CLAHE',cl1)
cv2.imshow('CV equalize',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()