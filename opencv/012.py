import cv2
import numpy as np

img = cv2.imread('shiroha.png',0)
rows, cols = img.shape[:2]
print 'rows %s' % rows