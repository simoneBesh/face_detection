import cv2

img = cv2.imread("4f.jpg")

gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray, 1.1, 3)
print(faces)
print(len(faces))
facelength = len(faces)
count = 0

for (x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
       cropImage = img[y:y+h, x:x+w]
       singleFace = 'face' + str(facelength-count) + '.jpg'
       cv2.imwrite(singleFace, cropImage)
       count = count + 1
       print(count)
             
cv2.imshow('img',img)
cv2.waitKey(0)



