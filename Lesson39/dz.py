from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(
    executable_path='chromedriver',
    options=chrome_options
)

driver.get('https://en.wikipedia.org/wiki/Main_Page')
header = driver.find_element(By.ID,'Welcome_to_Wikipedia')
print(header.text)
header = driver.find_element(By.CLASS_NAME,'mw-headline')
print(header.text)


driver.close()