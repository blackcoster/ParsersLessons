import unittest
from circle import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):


    def test_area(self):
        self.assertEqual(circle_area(3),pi*3**2)
        self.assertEqual(circle_area(0),0)
        self.assertEqual(circle_area(1), pi )
        self.assertEqual(circle_area(2.5), pi * 2.5 ** 2)

        # with self.assertRaises(ValueError):
        #     circle_area(-2)

    def test_values(self):
        self.assertRaises(ValueError,circle_area,-2)

    def test_types(self):
        self.assertRaises(TypeError,circle_area,5+5j)
        self.assertRaises(TypeError, circle_area, 'five')
        self.assertRaises(TypeError, circle_area, [42,6])
        self.assertRaises(TypeError, circle_area, '5')

if __name__ =='__main__':
    unittest.main()