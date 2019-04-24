import numpy as np
import cv2

color = np.uint8([[[0,0,255]]]) # BGR format
hsv = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
print hsv
h = hsv[0][0][0]
lower_bound = [(h-10)%255,100,100]
upper_bound = [(h+10)%255,255,255]
print('lower_bound = %s' % lower_bound)
print('upper_bound = %s' % upper_bound)