import cv2
import imutils
import pytesseract
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# if Windows then set tesseract
from PIL import Image

if os.name == 'nt':
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def get_image(test=False):
    """
    This method gets the image from a GUI
    :return: Returns the image
    """
    if test:
        file_name = os.getcwd() + '/img/template.jpeg'
    else:
        # we don't want a full GUI, so keep the root window from appearing
        Tk().withdraw()

        # opens up a in the "./img" directory so the user can choose the file via gui more options
        # can be added like file extention filters and such but that can be added later /shrug
        # show an "Open" dialog box and return the path to the selected file
        file_name = askopenfilename(
            initialdir=os.getcwd() + '/img',
            title="Please select an image")

    return file_name


def read_img(file_name):
    """
    This method reads the image and converts the data to text
    :param file_name: The image to be read
    :return: Returns the text from the image
    """
    # Read in image and store the tmp image
    tmp_file = 'tmp.png'
    img = cv2.imread(file_name)

    # Clean up image so it is easier to read
    clean = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    clean = cv2.GaussianBlur(clean, (5, 5), 0)

    # Write cleaned image out to the tmp image
    cv2.imwrite(tmp_file, clean)

    # Open cleaned image and read txt
    img = Image.open(tmp_file)
    text = pytesseract.image_to_string(img)

    # Remove the tmp file
    os.remove(tmp_file)

    # return just the text
    return text


def parse_data(text):
    """
    This method will parse through the data and make a key, value dictionary pair.
    :param text: The text to be parsed
    :return: Returns the dictionary
    """
    return text


if __name__ == '__main__':
    receipt = get_image()
    data = read_img(receipt)
    items = parse_data(data)

    print(items)
