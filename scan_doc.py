import numpy as np
import pandas as pd
import cv2
import PIL
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
import spacy


img_cv = cv2.imread("./Selected/052.jpeg")
cv2.imshow("business Card", img_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()



img_pl = PIL.Image.open("./Selected/052.jpeg")
type(img_pl)
type(img_cv)

print(pytesseract.image_to_string(img_pl))
