import cv2
import numpy as np

img = cv2.imread('shiroha.png')

roi = img[100:300,100:300]

cv2.imshow('img',img)
cv2.imshow('ROI',roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
