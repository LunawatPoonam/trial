import cv2
from cv2 import COLOR_BGR2GRAY
img= cv2.imread("4f.jpg")

gray=cv2.cvtColor(img, COLOR_BGR2GRAY)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faces=face_cascade.detectMultiScale(gray,1.1,5)
print(len(faces))

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)
cv2.imshow("image",img)
cv2.waitKey(0)