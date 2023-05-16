import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options

class Test(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.get('https://pythonscraping.com/pages/javascript/draggableDemo.html')
        kub = self.driver.find_element(By.ID, 'draggable')
        zona = self.driver.find_element(By.ID, 'div2')

        action = ActionChains(self.driver)
        action.drag_and_drop(kub, zona)
        action.perform()
        self.answer = self.driver.find_element(By.ID, 'message').text

    def tearDown(self):
        self.driver.close()

    def test_drag(self):

        right_answer = 'You are definitely not a bot!'

        self.assertEqual(self.answer,right_answer)



