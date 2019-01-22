import cv2
import numpy as np

#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)


def draw_circle(event,x,y,flags,param):
    #mouse left button double click
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print('left button down')
        cv2.circle(img,(x,y),100,(255,0,0),-1)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    #press ESC exit
    if cv2.waitKey(20)&0xff == 27:
        break

cv2.destroyAllWindows()
