import numpy as np
import cv2
img = np.zeros((512,512,3))
#img[200:300,450:500] = 255,0,0
cv2.line(img,(0,0),(300,300),(0,255,0),3)
cv2.line(img,(0,100),(img.shape[1],img.shape[0]),(0,0,255),3)
cv2.rectangle(img,(20,50),(350,320),(255,0,0),3)
cv2.circle(img,(350,400),45,(0,255,16),cv2.FILLED)
cv2.putText(img,'vidyarth',(50,150),cv2.FONT_HERSHEY_COMPLEX,1,(25,56,12),3)
cv2.imshow('output',img)
cv2.waitKey(0)