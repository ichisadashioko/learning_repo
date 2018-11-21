# how to find HSV color range for cv2.inRange()

import numpy as np
import cv2

green = np.uint8([[[0,255,0]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print hsv_green
# output [[[ 60 255 255]]]

# lower_bound = [H-10,100,100]
# upper_bound = [H+10,255,255]

# In this example
# lower_green = [50,100,100]
# upper_green = [70,255,255]