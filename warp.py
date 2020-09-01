#Word perspective of an image to gwt its bird eye view.

import cv2
import numpy as np

img = cv2.imread("./images/king.jpg")

#Giving four corners of image
pts1 = np.float32([[4,3],[224,2],[2,284],[218,282]])

width,height = 250,350

#we have to define which corner is where
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

#transform matrix for perspective
matrix = cv2.getPerspectiveTransform(pts1,pts2)

#outputimage
imgOutput = cv2.warpPerspective(img,matrix,(width,height))



cv2.imshow("Output",imgOutput)

cv2.waitKey(0)