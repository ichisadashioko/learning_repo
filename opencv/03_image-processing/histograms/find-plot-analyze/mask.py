import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('rem.png',0)

# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[0:720,640:1280] = 255 # format [y_start:y_end,x_start:x_end]
masked_img = cv2.bitwise_and(img,img,mask=mask)

# cv2.imshow('original',img)
# cv2.imshow('masked image',masked_img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221)
plt.imshow(img,'gray')
plt.subplot(222)
plt.imshow(mask,'gray')
plt.subplot(223)
plt.imshow(masked_img,'gray')
plt.subplot(224)
plt.plot(hist_full)
plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()
