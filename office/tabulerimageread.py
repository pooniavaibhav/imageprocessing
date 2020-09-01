import cv2
import numpy as np
import pytesseract
from office.sort_contor import sort_contours
import pandas as pd

#getting greyscale image so using 0 as parameter
img = cv2.imread("/home/webhav/Documents/image_processing/img_processing/images/tabulardata.jpeg",0)

#thresholding the image to a binary image
thresh,img_bin = cv2.threshold(img,128,255,cv2.THRESH_BINARY |cv2.THRESH_OTSU)

#inverting image becasue there is too much white area to see details properly.
img_bin = cv2.bitwise_not(img_bin)


# Length(width) of kernel as 100th of total width
kernel_len = np.array(img).shape[1]//100

# Defining a vertical kernel to detect all vertical lines of image
ver_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_len))

# Defining a horizontal kernel to detect all horizontal lines of image
hor_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_len, 1))

#Use vertical kernel to detect and save the vertical lines in a jpg
image_1 = cv2.erode(img_bin, ver_kernel, iterations=3)
vertical_lines = cv2.dilate(image_1, ver_kernel, iterations=3)

#Use horizontal kernel to detect and save the horizontal lines in a jpg
image_2 = cv2.erode(img_bin, hor_kernel, iterations=3)
horizontal_lines = cv2.dilate(image_2, hor_kernel, iterations=3)

# Combine horizontal and vertical lines in a new third image, with both having same weight.
img_vh = cv2.addWeighted(vertical_lines, 0.5, horizontal_lines, 0.5, 0.0)



# A kernel of 2x2
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

#Eroding and thesholding the image
img_vh = cv2.erode(~img_vh, kernel, iterations=2)
thresh, img_vh = cv2.threshold(img_vh,128,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

bitxor = cv2.bitwise_xor(img, img_vh)
bitnot = cv2.bitwise_not(bitxor)

# Detect contours for following box detection
contours, hierarchy = cv2.findContours(img_vh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Sort all the contours by top to bottom.
contours, boundingBoxes = sort_contours(contours, method="top-to-bottom")

#Creating a list of heights for all detected boxes
heights = [boundingBoxes[i][3] for i in range(len(boundingBoxes))]

#Get mean of heights
mean = np.mean(heights)

#Create list box to store all boxes in
box = []
# Get position (x,y), width and height for every contour and show the contour on image
for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    if (w<1000 and h<500):
        image = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        box.append([x,y,w,h])

#Creating two lists to define row and column in which cell is located
row=[]
column=[]
j=0
# Sorting the boxes to their respective row and column
for i in range(len(box)):

    if (i == 0):
        column.append(box[i])
        previous = box[i]

    else:
        if (box[i][1] <= previous[1] + mean / 2):
            column.append(box[i])
            previous = box[i]

            if (i == len(box) - 1):
                row.append(column)

        else:
            row.append(column)
            column = []
            previous = box[i]
            column.append(box[i])

#calculating maximum number of cells
countcol = 0
for i in range(len(row)):
    countcol = len(row[i])
    if countcol > countcol:
        countcol = countcol

#Retrieving the center of each column
center = [int(row[i][j][0]+row[i][j][2]/2) for j in range(len(row[i])) if row[0]]
center=np.array(center)
center.sort()

finalboxes = []
for i in range(len(row)):
    lis=[]
    for k in range(countcol):
        lis.append([])
    for j in range(len(row[i])):
        diff = abs(center-(row[i][j][0]+row[i][j][2]/4))
        minimum = min(diff)
        indexing = list(diff).index(minimum)
        lis[indexing].append(row[i][j])
    finalboxes.append(lis)

print(finalboxes)
outer = []
final_list=[]
this_dict = {}
dimension_list=[]
value_list=[]
for i in range(len(finalboxes)):
    for j in range(len(finalboxes[i])):
        inner = ''
        if (len(finalboxes[i][j]) == 0):
            outer.append(' ')
        else:
            for k in range(len(finalboxes[i][j])):
                y, x, w, h = finalboxes[i][j][k][0], finalboxes[i][j][k][1], finalboxes[i][j][k][2], \
                             finalboxes[i][j][k][3]
                finalimg = bitnot[x:x + h, y:y + w]
                kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 1))
                border = cv2.copyMakeBorder(finalimg, 2, 2, 2, 2, cv2.BORDER_CONSTANT, value=[255, 255])
                resizing = cv2.resize(border, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
                dilation = cv2.dilate(resizing, kernel, iterations=1)
                erosion = cv2.erode(dilation, kernel, iterations=2)
                out = pytesseract.image_to_string(erosion)
                final_list.append(out)
                temp_list1 = [x,y,w,h]
                dimension_list.append(temp_list1)
                temp_list2 = [out]
                value_list.append(temp_list2)
                if (len(out) == 0):
                    out = pytesseract.image_to_string(erosion, config='--psm 3')
                    final_list.append(out)
            outer.append(inner)
for i in range(len(dimension_list)):
    x = dimension_list[i][0]
    y = dimension_list[i][1]
    w = dimension_list[i][2]
    h = dimension_list[i][3]
    key = "boundingBox" + str(i)
    final = {"vertices": [{"x": x, "y": y}, {"x": x+w, "y": y}, {"x": x, "y": y+h}, {"x": x+w, "y": y+h}], "description":value_list[i]}
    this_dict[key] = final
print(this_dict)