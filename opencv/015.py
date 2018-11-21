# contour features
# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bad_square.png',0)
ret,thresh = cv2.threshold(img,127,255,0)
im2,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

# image moments
cnt = contours[0]
M = cv2.moments(cnt)
print M

# centroid
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print 'centroid is [%d,%d]' % (cx, cy)

# contour area
# cv2.contourArea() or M['m00']
area = cv2.contourArea(cnt)
print 'area: %f' % area
print 'M[\'m00\'] = %f' % M['m00']

# contour perimeter (arc length)
perimeter = cv2.arcLength(cnt,True)
print 'perimeter = %f' % perimeter

# contour approximation
# Douglas-Peucker algorithm
# https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
print approx
cv2.imshow('img',cv2.drawContours(img,approx,-1,(0,255,0),3))


cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(img)
# plt.show()

# print cv2.RETR_EXTERNAL # (0)
# print cv2.RETR_LIST # (1)
# print cv2.RETR_CCOMP # (2)
# print cv2.RETR_TREE # (3)
# print cv2.RETR_FLOODFILL # (4)

# print cv2.CHAIN_APPROX_NONE # (1)
# print cv2.CHAIN_APPROX_SIMPLE # (2)
# print cv2.CHAIN_APPROX_TC89_KCOS # (3)
# print cv2.CHAIN_APPROX_TC89_L1 # (4)