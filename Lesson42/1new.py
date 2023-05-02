import requests
import pytesseract

#pip install Pillow
from PIL import Image

url = 'https://m.media-amazon.com/images/I/513fa2dRpYL.jpg'
image = requests.get(url,'lxml')
with open ('image.jpg','wb') as file:
    file.write(image.content)


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = Image.open('image.jpg')
string = pytesseract.image_to_data(image)
print(string)