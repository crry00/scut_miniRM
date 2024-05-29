import cv2
import numpy as np


def empty(a):
    pass
cv2.namedWindow("track")
cv2.resizeWindow("track",640,240)

cv2.createTrackbar("Hue Min","track",160,179,empty)
cv2.createTrackbar("Hue Max","track",179,179,empty)
cv2.createTrackbar("Sat Min","track",80,255,empty)
cv2.createTrackbar("Sat Max","track",255,255,empty)
cv2.createTrackbar("Val Min","track",15,255,empty)
cv2.createTrackbar("Val Max","track",255,255,empty)

cap=cv2.VideoCapture(0)
cap.set(3,640)#宽度设置
cap.set(4,480)#高度设置
cap.set(10,150)

cap.set(cv2.CAP_PROP_EXPOSURE,-8)#曝光设置
cap.set(cv2.CAP_PROP_CONTRAST, 50)

while True:
    _,img=cap.read()
    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue Min","track")
    h_max=cv2.getTrackbarPos("Hue Max","track")
    s_min=cv2.getTrackbarPos("Sat Min","track")
    s_max=cv2.getTrackbarPos("Sat Max","track")
    v_min=cv2.getTrackbarPos("Val Min","track")
    v_max=cv2.getTrackbarPos("Val Max","track")
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imghsv,lower,upper)
    imgsize=cv2.resize(img,(400,300))
    masksize = cv2.resize(mask, (400, 300))

    cv2.imshow("2",masksize)
    cv2.imshow("1", imgsize)

    cv2.waitKey(1)