from selenium import webdriver
from  selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                 "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36)")

driver = webdriver.Chrome(options=opts)

driver.get('https://pythonscraping.com/pages/recaptcha/humansonly.html')

time.sleep(2)
username = driver.find_element(By.NAME,'name')
color = driver.find_element(By.NAME,'color')

username.click()
username.send_keys('Пётр')
time.sleep(2)
color.click()
color.send_keys('синий')

time.sleep(2)

iframe = driver.find_element(By.CSS_SELECTOR,'body > form > div > div > div > iframe')
checkbox = driver.find_element(By.CLASS_NAME,'recaptcha-checkbox-checkmark').click()
# checkbox = driver.find_element(By.XPATH,'//*[@class = "')
# driver.find_element(By.CSS_SELECTOR("div[class=recaptcha-checkbox-checkmark]")).click()

