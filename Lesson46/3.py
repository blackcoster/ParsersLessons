from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://pythonscraping.com/pages/javascript/draggableDemo.html')

kub = driver.find_element(By.ID,'draggable')
zona = driver.find_element(By.ID,'div2')

action = ActionChains(driver)
action.drag_and_drop(kub,zona)
action.perform()

print(driver.find_element(By.ID,'message').text)