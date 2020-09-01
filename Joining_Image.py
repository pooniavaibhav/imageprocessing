import cv2
import numpy as np

img = cv2.imread("./images/img.jpg")
hor = np.hstack((img,img))
ver = np.vstack((img,img))

cv2.imshow("Image",ver)
cv2.waitKey(0)