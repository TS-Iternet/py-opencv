import cv2

imagepath = r'./fans.jpg'

face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')

image = cv2.imread(imagepath)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,scaleFactor=1.10,minNeighbors=5,minSize=(3,3))

print('发现{0}个人脸!'.format(len(faces)))

for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('faces',image)
cv2.waitKey(0)

cv2.destroyAllWindows()
