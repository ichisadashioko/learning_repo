import cv2
import numpy as np

img = cv2.imread('shiroha.png',0)
img = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
edges = cv2.Canny(img,100,200)

cv2.imshow('original',img)
cv2.imshow('canny',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
