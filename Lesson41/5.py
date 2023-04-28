from PIL import Image
import pytesseract



def cleanFile(filePath,newFilePath):
    image = Image.open(filePath)
    image = image.point(lambda x:0 if x<143 else 255)
    image.save(newFilePath)
    return image

image = cleanFile('i.jpg','textCleaned.png')
# image = Image.open('i.jpg')
print(pytesseract.image_to_string(image))
print(pytesseract.image_to_data(image))
