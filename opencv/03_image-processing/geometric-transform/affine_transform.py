import cv2
import numpy as np

img = cv2.imread('rectangles.png')
height,width,ch = img.shape
# three points from the source image
src_pts = np.float32([[32,32],[128,32],[32,128]])
# three points from the destination image
dst_pts = np.float32([[8,64],[128,16],[48,64]])

# draw points on the image
for pt in src_pts:
    x = pt[0]
    y = pt[1]
    cv2.circle(img,(x,y),2,(0,255,0),5)

M = cv2.getAffineTransform(src_pts,dst_pts)

dst = cv2.warpAffine(img,M,(width,height))

cv2.imshow('original',img)
cv2.imshow('transformed',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
