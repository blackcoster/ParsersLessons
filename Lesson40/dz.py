from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
import time
import csv

def waitForLoad(driver):
    elem = driver.find_element(By.TAG_NAME,'html')
    count = 0
    while True:
        count+=1
        if count > 20:
            print('Time out')
            return time.sleep(0.5)
        try:
            elem == driver.find_element(By.TAG_NAME,'html')
        except StaleElementReferenceException:
            return




chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='chromedriver', options=chrome_options)
driver.get('https://pythonscraping.com/pages/javascript/redirectDemo1.html')
waitForLoad(driver)
csvFile = open('test.csv','w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(driver.page_source)
finally:
    csvFile.close()
print(driver.page_source)
driver.close()



import csv

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome('chromedriver',options=options)

driver.get('https://www.kinopoisk.ru/media/article/4007668/')
print(driver.title)

# contents = driver.find_elements(By.CLASS_NAME,'stk-reset')
# contents_text = [content.text for content in contents]
# print(contents_text)
#
# images = driver.find_elements(By.CLASS_NAME,'stk-image')
# images_url  = [im.get_attribute('src') for im in images]
# print(images_url)

film_page_url = driver.find_element(By.CLASS_NAME,'film-object-card-film-poster__image-wrap')
print(film_page_url.get_attribute('href'))
film_page_url.click()

film_page = driver.find_elements(By.CLASS_NAME,'styles_rowDark__ucbcz')
film_info = [info.text for info in film_page]

csvFile = open('test.csv','w',encoding='utf-8')
writer = csv.writer(csvFile)

for row in film_info:
    print(row.replace('\n',' - '))
    writer.writerow(row.replace('\n',' - '))
