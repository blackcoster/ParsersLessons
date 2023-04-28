import pytesseract
from pytesseract import Output
from PIL import Image
import  numpy as np
def regulator(x):
    if x > 143:
        x = 255
    else:
        x = 0

def cleanFile(filePath,threshold):
    image = Image.open(filePath)
    image = image.point(lambda x:0 if x < threshold else 255)
    return image

def getConfindence(image):
    data = pytesseract.image_to_data(image,output_type=Output.DICT)
    text = data['text']
    confidences = []
    numChars = []

    for i in range(len(text)):
        if data['conf'][i] > -1:
            confidences.append(data['conf'][i])
            numChars.append(len(text[i]))

    return np.average(confidences,weights=numChars),sum(numChars)
tlist = [85,110,38,125]
filePath = 'hz2.jpg'
start = 80
step = 5
end = 200

for threshold in range(start,end,step):
    image = cleanFile(filePath,threshold)
    scores = getConfindence(image)
    print(f'граница - {threshold}, уверенность - {scores[0]}, символов распознано - {scores[1]}' )



#
# def cleanFile(filePath,newFilePath,t):
#     image = Image.open(filePath)
#     image = image.point(lambda x:0 if x<t else 255)
#     image.save(newFilePath)
#     return image
#
# for t in tlist:
#     image = cleanFile('hz2.jpg','textCleaned.png',t)
#     # image = Image.open('i.jpg')
#     print(pytesseract.image_to_string(image))
#     print('next')

