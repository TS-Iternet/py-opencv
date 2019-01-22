import numpy as np
import cv2

## Note:It can't save Video
cap = cv2.VideoCapture('2.mov')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret,frame = cap.read()
    if(ret is True):
        frame = cv2.flip(frame,0)
        out.write(frame)
        
        cv2.imshow('frame',frame)
    if(cv2.waitKey(1)&0xff == ord('q')):
       break

cap.release()
out.release()
cv2.destroyAllWindows()
