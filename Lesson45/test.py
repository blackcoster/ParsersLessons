import unittest

class TestAddition(unittest.TestCase):

    def setUp(self):
        print('Идет подготовка щас будет тест')
    def tearDown(self):
        print('Тест проведен, закрываемся')
    def test_add(self):
        self.assertEqual(2+2,4)
    def test_min(self):
        self.assertEqual(2-2,0)

if __name__ == '__main__':
    unittest.main()