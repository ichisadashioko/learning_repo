import cv2
import numpy as np

img = cv2.imread('shiroha.png',0)
# img = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(img,kernel,iterations=1)
dilation = cv2.dilate(img,kernel,iterations=1)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel) # erosion followed by dilation
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel) # dilation followed by erosion
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel) # difference between dilation and erosion of an image
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel) # difference between input image and Opening of the image
blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel) # difference between input image and Closing of the image

cv2.imshow('original',img)
cv2.imshow('erosion',erosion)
cv2.imshow('dilation',dilation)
cv2.imshow('opening',opening)
cv2.imshow('closing',closing)
cv2.imshow('gradient',gradient)
cv2.imshow('top hat',tophat)
cv2.imshow('black hat',blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()