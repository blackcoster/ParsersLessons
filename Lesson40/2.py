from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='chromedriver',options=chrome_options)
driver.get('https://pythonscraping.com/pages/javascript/redirectDemo1.html')
try:
    bodyElement = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, '//body[contains(text(),"you are looking")]')))
    print(bodyElement.text)
except:
    print('Нету элемента')