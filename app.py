from flask import Flask, render_template, request
import os
from img_to_text import ocr

app = Flask(__name__)
path = os.getcwd()

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
UPLOAD_FOLDER = os.path.join(path, 'uploads\\')

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def file_allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template("index.j2")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 1234)) 
    app.run(port=port, debug=True) 
