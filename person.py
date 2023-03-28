import cv2 as cv
import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
#0 默认的是电脑自带的摄像头

cap = cv2.VideoCapture(0)
#cap.set函数中的3为帧的宽度、4为高度、10为亮度
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

faceCascade= cv2.CascadeClassifier("face.xml")

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in faces:
        # 打码：使用高斯噪声替换识别出来的人眼所对应的像素值
        img[y+10:y+h-10,x:x+w,0]=np.random.normal(size=(h-20,w))
        img[y+10:y+h-10,x:x+w,1]=np.random.normal(size=(h-20,w))
        img[y+10:y+h-10,x:x+w,2]=np.random.normal(size=(h-20,w))

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        text = "{}".format('Person')
        cv.putText(img, text, (x, y), cv.FONT_HERSHEY_COMPLEX, color=(255,0,0), fontScale=1)

    cv2.imshow("Result", img)
#按下`键后break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()