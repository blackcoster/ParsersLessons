from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(
    executable_path='chromedriver',
    options=chrome_options
)

driver.get('https://pythonscraping.com/pages/javascript/ajaxDemo.html')
try:
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'loadedButton')))
finally:
    print(driver.find_element(By.ID,'content').text)
    driver.close()

# ID
# CLASS_NAME
# CSS_SELECTOR
# LINK_TEXT (By.LINK_TEXT,' Нажмите ')
# PARTIAL_LINK_TEXT (By.PARTIAL_LINK_TEXT,'Нажмите')
# <a href = 'www.wbcjwc.ru'> Нажмите </a>
# TAG_NAME  (By.TAG_NAME,'div')