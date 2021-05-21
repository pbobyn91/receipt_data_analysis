import cv2
import pytesseract
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def read_img(fileName):
    img = cv2.imread(fileName)
    text = pytesseract.image_to_string(img)
    return text

if __name__ == '__main__':
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    
    # opens up a in the "./img" directory so the user can choose the file via gui more options 
    # can be added like file extention filters and such but that can be added later /shrug 
    filename = askopenfilename(
        initialdir= os.getcwd()+'/img',
        title= "Please select an image",) # show an "Open" dialog box and return the path to the selected file
    
    data = read_img(filename)
    print(data)
