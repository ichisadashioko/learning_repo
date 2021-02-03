import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        out.write(frame)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

# release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
