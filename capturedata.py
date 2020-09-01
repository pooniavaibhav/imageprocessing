"""
Reading file-
"""
import cv2

#import image
img = cv2.imread("images/index.jpg")
cv2.imshow("Output",img)
cv2.waitKey(0)

#import video
#we create a capture object
cap = cv2.VideoCapture("video.mp4")
#now video is a series of images so we will use loop to run video
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    #the below code will make the video to terminate if we press q.
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

# use webcam
# 0 will tell the code to run the default webcam.
cap = cv2.VideoCapture(0)
#we set the width and height for video
cap.set(3, 640)
cap.set(4, 480)
#adjust brightness
cap.set(10,0)
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
