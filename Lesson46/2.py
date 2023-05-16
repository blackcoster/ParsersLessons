from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://pythonscraping.com/pages/files/form.html')
firstname = driver.find_element(By.NAME,'firstname')
lastname = driver.find_element(By.NAME,'lastname')
button = driver.find_element(By.ID,'submit')


# 1 способ
# firstname.send_keys('jbj')
# lastname.send_keys('Krupenina')
# button.click()

# 2 способ
actions = ActionChains(driver).click(firstname).send_keys('taya').click(lastname).send_keys('familia').click(button)
actions.perform()

answer = driver.find_element(By.TAG_NAME,'body').text
print(answer)