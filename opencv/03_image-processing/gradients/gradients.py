import cv2
import numpy as np

img = cv2.imread('box.png',0)
img = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

cv2.imshow('original',img)
cv2.imshow('laplacian',laplacian)
cv2.imshow('Sobel X',sobelx)
cv2.imshow('Sobel Y',sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()
