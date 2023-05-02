from PIL import Image
import time
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from mss import mss

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.labirint.ru/books/848248')
time.sleep(2)
box = driver.find_element(By.CLASS_NAME,'fotorama__stage__shaft')
box.click()
time.sleep(1)

box.click()
time.sleep(2)
with mss() as sct:
    filename = sct.shot(mon = 1,output=f'kartinka0.png')
    print(filename)
time.sleep(1)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = Image.open(f'kartinka0.png')
string = pytesseract.image_to_data(image,lang='rus')
print(string)
