import cv2
import numpy as np

img = cv2.imread('shiroha.png')

px = img[100,100]
print px

# accessing only blue pixel
blue = img[100,100,0]
print blue

# modify the pixel values
img[0,0] = [0,0,0]
'''
Warning: Numpy as a optimized library for fast array calculations. So simply accessing each and every pixel values and modifying it will be very slow and it is discouraged.
'''
# better pixel accessing and editing method

# accessing RED value
red = img.item(10,10,2)
print red

# modifying RED value
img.itemset((10,10,2),100)
print img.item(10,10,2)

img = cv2.resize(img,None,fx=3,fy=3,interpolation=cv2.INTER_CUBIC)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
