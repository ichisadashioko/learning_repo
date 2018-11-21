# contours

import cv2
import numpy as np

im = cv2.imread('shiroha.png')
imgray = cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)