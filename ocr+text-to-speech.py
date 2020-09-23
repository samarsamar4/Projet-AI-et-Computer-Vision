# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:04:25 2019

@author: Administrator
"""

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2

#tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'
# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# load the example image and convert it to grayscale
image = cv2.imread('receipt1.jpg')
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Image", gray)n j

# Simple image to string
#txt = str(((pytesseract.image_to_string(Image.open('arabic.png'),lang='ara')))) 
txt=pytesseract.image_to_string(image)
print(txt)

# French text image to string
#print(pytesseract.image_to_string(Image.open('image3.png'), lang='arabic'))

from gtts import gTTS 
import os 

speech = gTTS(text = txt, lang = 'en', slow = False)
speech.save("voice.mp3")
os.system("start voice.mp3")
