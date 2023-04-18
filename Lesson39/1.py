import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--headless') # для фонового режима
driver = webdriver.Chrome(
    executable_path='chromedriver',
    options=chrome_options
)
driver.get('https://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3)
print(driver.find_element(By.ID,'content').text)

driver.close()