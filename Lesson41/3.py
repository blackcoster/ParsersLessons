from PIL import Image
import pytesseract
from pytesseract import Output

image = Image.open('i.jpg')
data = pytesseract.image_to_data(image,output_type=Output.DICT)
print(data)
data = pytesseract.image_to_string(image,output_type=Output.BYTES)
print(data)