import cv2
import numpy as np
from sharpenImage import sharp_image
from textdetection import get_adhaar_details
from textdetection import get_pan_details
document_name = input("Enter the name of the document : ")
document_type = input("Please select the document type :  \n1.AADHAR \n2.PAN \n Selection - ")
path = "images/" + document_name

def preprocessing(image):
    imgGrey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGrey, (7, 7), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)
    return imgCanny

def getContors(image):
    contours,hierarchy = cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 6000:
            cv2.drawContours(img, cnt, -1, (255, 0, 0), 3)
            perimeter = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)
            objCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            return x,y,w,h

def getContors_aadhar(image):
    contours,hierarchy = cv2.findContours(image,1,2)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 2000 and area < 8000:
            cv2.drawContours(img, cnt, -1, (255, 0, 0), 3)
            perimeter = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)
            objCor = len(approx)
            # x,y,w,h = cv2.boundingRect(approx)
    x = 380
    y = 200
    w = 90
    h = 102

    return x, y, w, h

if __name__ == "__main__":
    image = cv2.imread(path)
    img = cv2.imread(path)
    sharp_img = sharp_image(image)
    processed_img = preprocessing(sharp_img)
    # Image sharpening-
    if document_type == "1":
        x,y,w,h = getContors(processed_img)
        ROI = sharp_img[y:y + h, x:x + w]
        NAME,DOB,SEX,aadhar_no = get_adhaar_details(image)
        print("Name of the person is : " + NAME)
        print("DOB is : " + DOB)
        print("SEX is : " + SEX)
        print("Aadhar Number is : " + aadhar_no)

    if document_type == "2":
        x,y,w,h = getContors_aadhar(processed_img)
        ROI = sharp_img[y:y + h, x:x + w]
        Name, Fathers_name, DOB, pan_no = get_pan_details(image)
        print("Name of the person is : " + Name)
        print("Fathers Name is : " + Fathers_name)
        print("DOB is : " + DOB)
        print("PAN Number is : " + pan_no)
    cv2.imshow("normal", ROI)
    cv2.waitKey()


