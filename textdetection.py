import cv2
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd='C:\\Users\\Khushi\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'


def read_image(path, file_name):
    img = cv2.imread(path)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    # DETECTING WORDS
    hImg, wImg,_ = img.shape
    boxes = (pytesseract.image_to_data(img))
    detected_text = ""
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            if len(b)==12:
                x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9])
                cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,225),1)
                cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
                detected_text = detected_text + str(b[11]) + " "
    saving_file_name = file_name.split('.')[0] + "_result.png"
    res_file_path = os.path.join("static", saving_file_name)
    cv2.imwrite(res_file_path, img)
    return detected_text
