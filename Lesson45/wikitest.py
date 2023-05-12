from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest

class TestWikipedia(unittest.TestCase):
    bs = None

    #ЭТО ВЫПОЛНИТСЯ ПЕРЕД КАЖДЫМ ТЕСТОМ ТО ЕСТЬ 2 РАЗА
    # def setUp(self):
    #     url = 'http://en.wikipedia.org/wiki/Monty_Python'
    #     self.bs = BeautifulSoup(urlopen(url),'html.parser')

    # ЭТО ВЫПОЛНИТСЯ 1 РАЗ - СТАТИЧЕСКИЙ МЕТОД
    def setUpClass():
        url = 'http://en.wikipedia.org/wiki/Monty_Python'
        TestWikipedia.bs = BeautifulSoup(urlopen(url),'html.parser')

    def test_title(self):
        pageTitle = self.bs.find('h1').get_text()
        self.assertEqual('Monty Python',pageTitle)

    def test_content(self):
        content = self.bs.find('div',{'id':'mw-content-text'})
        self.assertIsNotNone(content)

if __name__ == '__main__':
    unittest.main()

