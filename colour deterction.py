import cv2
import numpy as np
def callback(x):
    pass
img = cv2.imread("images/car2.jpg")
cv2.namedWindow('image')
imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.createTrackbar('hue max','image',255,255,callback)
cv2.createTrackbar('hue min','image',11,179,callback)
cv2.createTrackbar('sat max','image',255,255,callback)
cv2.createTrackbar('sat min','image',68,255,callback)
cv2.createTrackbar('val max','image',255,255,callback)
cv2.createTrackbar('val min','image',114,255,callback)
while (1):
    h_max = cv2.getTrackbarPos('hue max','image')
    h_min = cv2.getTrackbarPos('hue min','image')
    s_max = cv2.getTrackbarPos('sat max','image')
    s_min = cv2.getTrackbarPos('sat min','image')
    v_max = cv2.getTrackbarPos('val max','image')
    v_min = cv2.getTrackbarPos('val min','image')
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imghsv,lower,upper)
    result = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('original',img)
    cv2.imshow('hsv',imghsv)
    cv2.imshow('mask',mask)
    cv2.imshow('result',result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()