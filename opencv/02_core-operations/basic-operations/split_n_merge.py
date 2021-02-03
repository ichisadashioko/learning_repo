import cv2
import numpy as np

img = cv2.imread('shiroha.png')

# split channels of image
b,g,r = cv2.split(img)
# or b = img[:,:,0] # (all x, all y, b channel)
'''
Warning: cv2.split() is a costly operation (in terms of time). So do it only if you need it. Other wise go for Numpy indexing.
'''

no_red = img.copy()
no_red[:,:,2] = 0

no_blue = img.copy()
no_blue[:,:,0] = 0

no_green = img.copy()
no_green[:,:,1] = 0

cv2.imshow('original',img)
cv2.imshow('Blue',b)
cv2.imshow('Red',r)
cv2.imshow('Green',g)
cv2.imshow('none red', no_red)
cv2.imshow('none blue',no_blue)
cv2.imshow('none green',no_green)
cv2.waitKey(0)
cv2.destroyAllWindows()
