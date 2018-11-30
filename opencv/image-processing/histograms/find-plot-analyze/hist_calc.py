import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('rem.png',0)
hist = cv2.calcHist([img],[0],None,[256],[0,256])

# plt.imshow(img,cmap='gray')
# plt.show()

# print type(hist)

# hist,bins = np.histogram(img.ravel(),256,[0,256])

# Plotting histograms

# Using Matplotlib

plt.hist(img.ravel(),256,[0,256])
plt.show()

# BGR plot

img = cv2.imread('2083.png')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256]) # set the x limits of current axes
plt.show()

# Using OpenCV

# not done
