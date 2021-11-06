import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Wendell\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def ocr(filename):
    '''This is the base function which takes a filename and outputs the text found in that location's picture file'''
    text = pytesseract.image_to_string(Image.open(filename))
    return text

# print(ocr('sample_2.jpg'))