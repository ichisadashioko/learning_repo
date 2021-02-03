import cv2
import numpy as np

img = cv2.imread('sudoku.png',1)
img = cv2.resize(img,None,fx=3,fy=3,interpolation=cv2.INTER_CUBIC)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,0,80,apertureSize=3)
cv2.imshow('edges',edges)
lines = cv2.HoughLines(edges,1,np.pi/180,110)

# rho = x*cos(theta) + y*sin(theta)

for line in lines:
    for rho,theta in line:
        print('[rho,theta] = [%f,%f]' % (rho,theta))
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)

print len(lines)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
