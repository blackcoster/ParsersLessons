# pip install Pillow
from PIL import Image,ImageFilter

img = Image.open('kart.jpg')
blurryKitten = img.filter(ImageFilter.GaussianBlur)
blurryKitten.save('blurred_kit.jpeg')

# blurryKitten.show()
