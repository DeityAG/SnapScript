from flask import Flask, render_template, request
from PIL import Image
import pytesseract
import re
import webbrowser

app = Flask(__name__)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def detect_and_open_link(text):
    try:
        
        url_pattern = re.compile(r'https?://\S+|www\.\S+')

        
        urls = re.findall(url_pattern, text)

        if urls:
            for url in urls:
                print(f"Opening link: {url}")
                
                webbrowser.open(url)
        else:
            print("No links found in the text.")
    except Exception as e:
        print(f"Error while detecting and opening link: {e}")

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if 'image' in request.files:
            image = request.files['image']
            img = Image.open(image)
            img.save('./static/image.png')
            text = pytesseract.image_to_string(img)
            detect_and_open_link(text)
            return render_template('result.html', text=text)
        return 'No image uploaded!'
    except Exception as e:
        return f"Error during image upload and processing: {e}"


@app.route('/create_note', methods=['POST'])
def create_note():
    try:
        text = request.form.get('text')
        
        return 'New note created successfully!'
    except Exception as e:
        return f"Error while creating a new note: {e}"

if __name__ == '__main__':
    app.run(debug=True)
