from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://okmarket.ru/")

a = driver.find_element(By.CLASS_NAME, "ass-prod-card__link")


