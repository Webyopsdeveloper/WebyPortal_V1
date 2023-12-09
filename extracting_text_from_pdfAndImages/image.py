
from PIL import Image
import pytesseract
import cv2
import numpy as np
from pytesseract import Output
import os

def image_to_tet(image_path):
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
    image = Image.open(image_path)
    image = image.resize((300,150))
    custom_config = r'-l eng --oem 3 --psm 6' 
   
    text = pytesseract.image_to_string(image,config=custom_config)
    print(text) 

    
    filename = filename = r"C:\Users\admin\Desktop\vacha\work\may\reading_pdf_images_script\demo.txt"

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(text) 

image_path = "images/sample1.jpg" 
image_to_tet(image_path)
    
