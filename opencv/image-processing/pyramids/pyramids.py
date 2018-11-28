import cv2
import numpy as np

img = cv2.imread('asuna.jpg')
height,width = img.shape[:2]

lower_reso = cv2.pyrDown(img)
# higher_reso = cv2.pyrUp(img)
pyrUp_lower_reso = cv2.pyrUp(lower_reso,dstsize=(width,height))

laplace = cv2.subtract(img,pyrUp_lower_reso)

cv2.imshow('original',img)

cv2.imshow('Low Resolution', lower_reso)
# cv2.imwrite('asuna_pyramid_down.png',lower_reso)

# cv2.imshow('Higher Resolution',higher_reso)

cv2.imshow('Pyramid Up low resolution', pyrUp_lower_reso)
# cv2.imwrite('asuna_pyramid_down_then_up.png',pyrUp_lower_reso)

cv2.imshow('Laplacian Pyramid',laplace)
# cv2.imwrite('asuna_laplacian_pyramid.png',laplace)

cv2.waitKey(0)
cv2.destroyAllWindows()