import numpy as np
import cv2
img = cv2.imread('images/cards.jpg')
width,height = 150,250
pt1 = np.float32([[198,115],[306,94],[231,291],[342,269]])
pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
img2 = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow('input',img)
cv2.imshow('output',img2)
cv2.waitKey(0)