import cv2
import numpy as np

img = cv2.imread('0.png',0)
img = cv2.resize(img,None,fx=3,fy=3,interpolation=cv2.INTER_CUBIC)

equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) # stacking images side-by-side

cv2.imshow('img',res)
cv2.waitKey(0)
cv2.destroyAllWindows()