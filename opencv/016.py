import cv2
import numpy as np

img = cv2.imread('shiroha.png',1)

z = np.zeros(img.shape[:2],int)

print z