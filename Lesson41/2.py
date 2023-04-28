import pytesseract
from PIL import Image

image = Image.open('pol.jpg')
text = pytesseract.image_to_string(image)
boxes = pytesseract.image_to_boxes(image)
data = pytesseract.image_to_data(image)
print(data)

# print(pytesseract.image_to_string(Image.open('text.png')))



