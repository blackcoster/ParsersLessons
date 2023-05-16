from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.okmarket.ru/')

tovar = driver.find_element(By.CLASS_NAME,'assortment-slider__slide')
tovar.click()


print(driver.find_element(By.CLASS_NAME,'single-product__descr-text').text)