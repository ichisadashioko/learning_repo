# read, show, and write image

import sys
import datetime
import numpy as np

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('shiroha.png', 0)

height, width = img.shape[:2]

# cv2.imwrite('shiroha00.png', img)

plt.imshow(img)
plt.show()


cv2.imshow('shiroha.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()