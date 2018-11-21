import cv2
import numpy as np

def nothing(x):
    pass

# cv2.imshow('Threshold')

# def create_track_bar():cv2.namedWindow('Threshold')
cv2.createTrackbar('LowH','Threshold',0,179,nothing)
cv2.createTrackbar('HighH','Threshold',179,179,nothing)

cv2.createTrackbar('LowS','Threshold',0,255,nothing)
cv2.createTrackbar('HighS','Threshold',30,255,nothing)

print 'something'

cv2.createTrackbar('LowV','Threshold',180,255,nothing)
cv2.createTrackbar('HighV','Threshold',255,255,nothing)

cv2.createTrackbar('Shadow Param','Threshold',85,255,nothing)

# create_track_bar()
cv2.waitKey(0)
cv2.destroyAllWindows()