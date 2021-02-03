import cv2
import numpy as np

img = cv2.imread('shiroha.png')
img = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

blur = cv2.blur(img,(3,3))
gaussian = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)
bilateral = cv2.bilateralFilter(img,9,24,35)

cv2.imshow('original',img)
cv2.imshow('blur',blur)
cv2.imshow('gaussian',gaussian)
cv2.imshow('median',median)
cv2.imshow('bilateral',bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
