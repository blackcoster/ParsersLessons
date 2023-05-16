from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://pythonscraping.com')

driver.get_screenshot_as_file('test.png')