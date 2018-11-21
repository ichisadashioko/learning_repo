# contours

import cv2
import numpy as np
import copy

from matplotlib import pyplot as plt

im = cv2.imread('contours.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print len(contours)
print type(contours)

img = copy.copy(im)

img = cv2.drawContours(img, contours, -1, (0,255,0), 1)

cv2.imshow('original',im)
cv2.imshow('thresh',thresh)
cv2.imshow('im2',im2)
cv2.imshow('contours',img)

# plt.imshow(img)
# plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()