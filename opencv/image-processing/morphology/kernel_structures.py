import cv2
import numpy as np

img = cv2.imread('shiroha.png',0)
img = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
tp = (7,7)
kernel = np.ones(tp,np.uint8)

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT,tp)

ellipse_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,tp)

cross_kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,tp)

e1 = cv2.erode(img,kernel,iterations=1)
e2 = cv2.erode(img,rect_kernel,iterations=1)
e3 = cv2.erode(img,ellipse_kernel,iterations=1)
e4 = cv2.erode(img,cross_kernel,iterations=1)

cv2.imshow('original',img)
cv2.imshow('erosion_full_kernel',e1)
cv2.imshow('erosion_rect_kernel',e2)
cv2.imshow('erosion_ellipse_kernel',e3)
cv2.imshow('erosion_cross_kernel',e4)

cv2.waitKey(0)
cv2.destroyAllWindows()