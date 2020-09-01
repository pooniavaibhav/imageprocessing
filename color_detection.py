import cv2
import numpy as np
#img = cv2.imread("./images/img.jpg")

#We want to detect a colour in image.First we convert it into HSV space-
#HSV is hue saturation and value model.HSV is a cylindrical color model that remaps the
# RGB primary colors into dimensions that are easier for humans to understand.
# Hue specifies the angle of the color on the RGB color circle. A 0° hue results in red, 120°
# results in green, and 240° results in blue. Saturation controls the amount of color used.
#imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def empty(a):
    pass

#creating a track bar-
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)
cv2.createTrackbar("Hue Min","Trackbars",15,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",31,179,empty)
cv2.createTrackbar("Saturation Min","Trackbars",41,255,empty)
cv2.createTrackbar("Saturation Max","Trackbars",255,255,empty)
cv2.createTrackbar("Value Min","Trackbars",76,255,empty)
cv2.createTrackbar("Value Max","Trackbars",117,255,empty)

while True:
    img = cv2.imread("./images/img.jpg")
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Saturation Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Saturation Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Value Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Value Max", "Trackbars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResults = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("output",imgResults)
    cv2.imshow("Mask", mask)
    cv2.waitKey(1)