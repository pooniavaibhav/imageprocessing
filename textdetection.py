import cv2
import pytesseract
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def get_adhaar_details(img):

    #pytesserect only accepts RGB values and open cv is BGR so will convert to RGB

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    all = []
    name = []
    DOB = []
    SEX = []
    AdharNo = []
    ## Detecting Words
    hImg,wImg,_ = img.shape
    #conf ='-psm 7 -oem 1 -hocr'
    boxes = pytesseract.image_to_data(img)
    for x,b in enumerate(boxes.splitlines()):
        if x != 0:
            b =b.split()
            if len(b)==12:
                #x,y,w,h =int(b[6]),int(b[7]),int(b[8]),int(b[9])
                if (b[2] == '3') and (b[5] == '1') and (b[4] == '4'):
                    name.append(b[11])
                if (b[2] == '3') and (b[5] == '2') and (b[4] == '4'):
                    name.append(b[11])
                if (b[2] == '3') and (b[5] == '3') and (b[4] == '4'):
                    name.append(b[11])
                if (b[2] == '3') and (b[5] == '4') and (b[4] == '4'):
                    name.append(b[11])
                if (b[2] == '3') and (b[5] == '5') and (b[4] == '4'):
                    name.append(b[11])
                #DOB
                if (b[2] == '4') and (b[5] == '5') and (b[4] == '1'):
                    DOB.append(b[11])
                #SEX
                if (b[2] == '4') and (b[5] == '3') and (b[4] == '2'):
                    SEX.append(b[11])
                # Aadhar No -
                if (b[2] == '5') and (b[3] == '3') and (b[4] == '1'):
                    AdharNo.append(b[11])
                if (b[2] == '5') and (b[3] == '2') and (b[4] == '1'):
                    AdharNo.append(b[11])
                if (b[2] == '5') and (b[3] == '1') and (b[4] == '1'):
                    AdharNo.append(b[11])
            NAME = ''
            aadhar_no=''

            for i in name:
                if i == 0:
                    NAME = i
                else:
                    NAME = NAME + ' ' + i

            for i in AdharNo:
                if i == 0:
                    aadhar_no = i
                else:
                    aadhar_no = aadhar_no + ' ' + i

    return NAME, DOB[0], SEX[0], aadhar_no

def get_pan_details(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ## Detecting Words
    hImg, wImg, _ = img.shape
    # conf ='-psm 7 -oem 1 -hocr'
    boxes = pytesseract.image_to_data(img)
    name = []
    fathers_name = []
    DOB=[]
    pan_no=[]
    for x,b in enumerate(boxes.splitlines()):
        if x != 0:
            b =b.split()
            if len(b)==12:
                if (b[2] == '2') and (b[5] == '1') and (b[4] == '2'):
                    name.append(b[11])
                if (b[2] == '2') and (b[5] == '2') and (b[4] == '2'):
                    name.append(b[11])
                if (b[2] == '2') and (b[5] == '3') and (b[4] == '2'):
                    name.append(b[11])
                if (b[2] == '2') and (b[5] == '1') and (b[4] == '3'):
                    fathers_name.append(b[11])
                if (b[2] == '2') and (b[5] == '2') and (b[4] == '3'):
                    fathers_name.append(b[11])
                if (b[2] == '2') and (b[5] == '1') and (b[4] == '4'):
                    DOB.append(b[11])
                if (b[2] == '4') and (b[5] == '1') and (b[4] == '1'):
                    pan_no.append(b[11])
    Name = ""
    Fathers_name = ""

    for i in name:
            if i == 0:
                Name = i
            else:
                Name = Name + ' ' + i

    for i in fathers_name:
            if i == 0:
                Fathers_name = i
            else:
                Fathers_name = Fathers_name + ' ' + i

    return Name,Fathers_name,DOB[0], pan_no[0]

# if __name__ == "__main__":
#     img = cv2.imread("images/pancard.jpg")
#     a,b,c,d = get_pan_details(img)
#     print(a,b,c,d)