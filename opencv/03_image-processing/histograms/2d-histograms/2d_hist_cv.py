import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('haze-closeup.png')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# channels = [0,1] # because we need to process both H and S plane
# bins = [180,256] # 180 for H plane and 256 for S plane
# range = [0,180,0,256] Hue value lies between 0 and 180 & Saturation lies between 0 and 256

hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

cv2.imshow('img',img)
cv2.imshow('hist',hist)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(hist,interpolation='nearest')
plt.show()
