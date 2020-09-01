import cv2

#method to import image
img = cv2.imread("images/Image.jpg")

#method to read image as grey image-
#img = cv2.imread("index.jpg",0)

#method to convert your image to greyscale-
# in openCv the colour convention is BGR
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Resize your image with width and height
imgResize =cv2.resize(imgGray,(750,420))

#Cropping image(remember the height comes first we are not using cv2 function but direct
# python matrix function)

imgcroped = img[0:500,200:500]

cv2.imshow("Output",imgcroped)
cv2.waitKey(0)