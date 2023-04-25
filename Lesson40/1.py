from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
import time

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
print(driver.page_source)
driver.close()