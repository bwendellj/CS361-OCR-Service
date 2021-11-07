from flask import Flask, render_template, request
import os
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Wendell\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)
path = os.getcwd()
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
UPLOAD_FOLDER = os.path.join(path, 'uploads\\')

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def file_allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def ocr(filename):
    '''This is the base function which takes a filename and outputs the text found in that location's picture file'''
    text = pytesseract.image_to_string(Image.open(filename))
    return text

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.j2', message = 'No file selected')
        file = request.files['file']

        if file.filename == '':
            return render_template('index.j2', msg='No File Found')
        
        if file and file_allowed(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            extracted = ocr(file)
            return render_template('index.j2', msg='OCR Complete', extracted=extracted, img_src= UPLOAD_FOLDER + file.filename)
    else:
        return render_template('index.j2')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 1234)) 
    app.run(port=port, debug=True) 
