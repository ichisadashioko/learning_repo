import cv2
import numpy as np

img = cv2.imread('sudoku.png', 1)
img = cv2.resize(img,None,fx=3,fy=3,interpolation=cv2.INTER_CUBIC)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,0,75,apertureSize=3)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,80,minLineLength,maxLineGap)

for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),1)

print len(lines)

cv2.imshow('edges',edges)
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()