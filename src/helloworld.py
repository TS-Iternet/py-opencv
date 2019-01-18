import numpy as np
import cv2

img = cv2.imread('1.jpg',0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
print(img.shape)
print(img.size)
print(img.dtype)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyWindow("image")
elif k == ord('s'):
    cv2.imwrite('messingray.png',img)
    cv2.destroyAllWindows()
