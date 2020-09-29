#! /usr/bin/env python
import os
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import pytesseract

# YOU WILL NEED TO INSTALL TESSERACT OCR FOR THIS AND THEN ENTER THE APPROPRIATE FILE PATH. INSTALLER IS LIKE ANY OTHER SOFTWARE, see link below
# https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v4.1.0-bibtag19.exe
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# SET THE DIRECTORY OF FOLDER WITH IMAGES
directory = r'C:\Users\evane\Desktop\Compute\Scripting\Text_Image_Scraper\images'

# LOOP THROUGH DIRECTORY
for filename in os.listdir(directory):

    # PRINT LIMIT LINE DISPLAY FILE NAME i use this for headers
    print('-----------------------------------')
    print(filename + '\n')

    # HANDLE IMAGE
    image = Image.open(os.path.join(directory, filename))

    # USE TESSERACT TO SCRAPE TEXT FROM IMAGE
    image_to_text = pytesseract.image_to_string(image, lang='eng')

    # I USE PRINT AS EXAMPLE, CAN OUTPUT TO FILE OR DO ANYTHING ELSE 
    print(image_to_text + '\n\n')
    
    #PRINT ANOTHER LIMIT LINE 
    print('-----------------------------------')


