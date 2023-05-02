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
urls = []
i = 1
for _ in range(6):
    box.click()
    time.sleep(2)
    with mss() as sct:
        filename = sct.shot(mon = 1,output=f'kartinka{i}.png')
        print(filename)
        i+=1
    time.sleep(1)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
for i in range(1,7):
    image = Image.open(f'kartinka{i}.png')
    string = pytesseract.image_to_string(image,lang='rus')
    print(string)

