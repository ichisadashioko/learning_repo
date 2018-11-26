import cv2
import numpy as np

img = cv2.imread('shiroha.png')

kernel = np.ones((4,4),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

cv2.imshow('original',img)
cv2.imshow('filtered',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()