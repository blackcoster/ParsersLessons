import random
from urllib.parse import unquote
from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest
import re

class TestWiki(unittest.TestCase):


    def test_pageProperties(self):
        self.url = 'http://en.wikipedia.org/wiki/Monty_Python'

        for i in range(1,10):
            self.bs = BeautifulSoup(urlopen(self.url),'html.parser')
            titles = self.titleMatchesURL()

            self.assertEqual(titles[0],titles[1])
            self.assertTrue(self.contentExists())
            self.url = self.getNextLink()
        print('Done')

    def titleMatchesURL(self):
        pageTitle = self.bs.find('h1').get_text()
        urlTitle = self.url[self.url.index('/wiki/')+6:]
        urlTitle = urlTitle.replace('_',' ')
        urlTitle = unquote(urlTitle)
        return [pageTitle.lower(),urlTitle.lower()]

    def contentExists(self):
        content = self.bs.find('div',{'id':'mw-content-text'})
        if content is not None:
            return True
        return False

    def getNextLink(self):
        links = self.bs.find('div',{'id':'bodyContent'}).find_all('a',href = re.compile('^(/wiki/)((?!:).)*$'))
        randomLink = random.choice(links)
        return f'http://en.wikipedia.org{randomLink.attrs["href"]}'


if __name__=='__main__':
    unittest.main()