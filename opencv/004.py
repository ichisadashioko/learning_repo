# scaling image
import cv2
import numpy as np

img = cv2.imread('shiroha.png')

# INTER_AREA for shrinking
# INTER_CUBIC (slow) and INTER_LINEAR for zooming

# res = cv2.resize(img, None, fx=2, fy=2, interpolation= cv2.INTER_CUBIC)

# OR

height, width = img.shape[:2]
res_cubic = cv2.resize(img, (2*width, 2*height), interpolation = cv2.INTER_CUBIC)
# res = cv2.resize(img, (int(0.5*width), int(0.5*height)), interpolation = cv2.INTER_AREA)
res_linear = cv2.resize(img, (2*width, 2*height), interpolation = cv2.INTER_LINEAR)

cv2.imshow('original', img)
# cv2.imshow('resized', res)

cv2.imshow('res_cubic', res_cubic)
cv2.imshow('res_linear', res_linear)

cv2.waitKey(0)
cv2.destroyAllWindows()