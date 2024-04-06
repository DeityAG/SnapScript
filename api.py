from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


image_path = r"C:\Users\Aditi Shrivastava\Desktop\hack\pic1.jpg"

try:
    
    text = pytesseract.image_to_string(Image.open(image_path))

    
    print("Extracted Text:")
    print(text)

except Exception as e:
    print("Error:", e)
