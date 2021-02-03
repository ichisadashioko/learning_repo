import cv2
import numpy as np

img = cv2.imread('gradient.png',0)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('original',img)
cv2.imshow('BINARY',thresh1)
cv2.imshow('BINARY_INV',thresh2)
cv2.imshow('TRUNC',thresh3)
cv2.imshow('TOZERO',thresh4)
cv2.imshow('TOZERO_INV',thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()
