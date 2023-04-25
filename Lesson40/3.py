import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import requests

def init__driver():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    return driver

def lookup(driver):
        driver.get('https://www.google.ru/')
        try:
            box = driver.find_element(By.NAME,'q')
            box.send_keys('Selenium')
            time.sleep(1)
            button = driver.find_element(By.NAME,'btnK')
            button.click()
            time.sleep(2)
            elem = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/div/div/span')
            elem.click()
            time.sleep(2)
        except TimeoutException:
            print('Не найдены')


def parse(url):
    r = requests.get(url)

driver = init__driver()
lookup(driver)
time.sleep(6)
driver.quit()

