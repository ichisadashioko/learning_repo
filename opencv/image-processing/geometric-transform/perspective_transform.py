import cv2
import numpy as np

img = cv2.imread('rectangles.png')
height,width,ch = img.shape
# 4 points from the source image
src_pts = np.float32([[64,128],[448,128],[176,464],[336,464]])
# 4 points from the destination image
dst_pts = np.float32([[0,0],[width,0],[0,height],[width,height]])

# draw points on the image
for pt in src_pts:
    x = pt[0]
    y = pt[1]
    cv2.circle(img,(x,y),2,(0,255,0),5)

M = cv2.getPerspectiveTransform(src_pts,dst_pts)

dst = cv2.warpPerspective(img,M,(width,height))

cv2.imshow('original',img)
cv2.imshow('transformed',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()