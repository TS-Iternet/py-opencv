import cv2
import time

print('Press ESC to exit')
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
imgWindow = cv2.namedWindow('FaceDetect',cv2.WINDOW_NORMAL)

def detect_face():
    capInput = cv2.VideoCapture('2.mov')

    nextCaptureTime = time.time()
    faces = []
    if not capInput.isOpened():
        print('Capture failed because of camera')
    while(1):
        ret,img = capInput.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        if nextCaptureTime < time.time():
            nextCaptureTime = time.time() + 0.1
            faces = faceCascade.detectMultiScale(gray,1.3,5)
        print(faces)
        for i in faces:
            for x,y,w,h in i:
                img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('FaceDetect',img)
        if cv2.waitKey(1) & 0xff == 27:
            break

    capInput.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    detect_face()
