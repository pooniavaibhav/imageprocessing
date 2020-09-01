import cv2
import numpy as np

#A matrix filled with zeroes i.e.black
img = np.zeros((512,512))

# To add a colour functionality we need three channels.
img = np.zeros((512,512,3))
print(img.shape)

#The colon represents whole of the image to be converted to blue
#img[:]=255,0,0

#If we use some value it will work like when we did resize of image i.e.the dimension inside the
#square bracket will change to blue.
#img[100:200,100:200] = 255,0,0

#Drawing a line in image
#We give strating point, end point of the line an det the end the color.
cv2.line(img,(0,0),(300,300),(0,255,0))

#Building rectange
cv2.rectangle(img,(200,300),(400,600),(0,0,255))

#If you want to fill your rectangle with a color use a parameter FILLED.
cv2.rectangle(img,(200,300),(400,600),(0,0,255),cv2.FILLED)

#Draw a circle
cv2.circle(img,(400,50),30,(255,100,100))

#write a text in image:
cv2.putText(img,"Made by code",(200,300),cv2.FONT_ITALIC,1,(150,150,250))

cv2.imshow("Output",img)
cv2.waitKey(0)