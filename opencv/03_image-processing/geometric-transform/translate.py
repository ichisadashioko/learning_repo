import cv2
import numpy as np

img = cv2.imread('shiroha.png',0)
rows,cols = img.shape

# shift image by (x,y) (pixels)
# matrix format
# M = [
#   [1, 0, x],
#   [0, 1, y]
# ]
M = np.float32([[1,0,100],[0,1,50]])
# output image size format (width,height)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('original',img)
cv2.imshow('translated',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()