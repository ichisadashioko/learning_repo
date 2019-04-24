import cv2
import numpy as np

img = cv2.imread('shiroha.png',0)
height,width = img.shape # only for gray image

# rotate image for an angle theta
# matrix format
# M = [
#   [cos(theta), -sin(theta)],
#   [sin(theta),  cos(theta)]
# ]

# rotate image with custom center of rotation
# matrix format
# M = [
#     [alpha, beta, (1-a)*center.x - beta*center.y],
#     [-beta, alpha, beta*center.x + (1-alpha)*center.y]
# ]
# alpha = scale*cos(theta)
# beta = scale*sin(theta)

M = cv2.getRotationMatrix2D((width/2,height/2),90,2)
dst = cv2.warpAffine(img,M,(width,height))

cv2.imshow('original',img)
cv2.imshow('rotated',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()