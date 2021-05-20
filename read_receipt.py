import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def read_img(img):
    img = cv2.imread(f'img/{img}')
    text = pytesseract.image_to_string(img)
    return text


if __name__ == '__main__':
    receipt = input("Enter receipt you want read: ")
    data = read_img(receipt)
    print(data)
