import cv2
import numpy as np

img = cv2.imread('haze-closeup.png')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

h = hsv[:,:,0]
s = hsv[:,:,1]

hist,xbins,ybins = np.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]])

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()