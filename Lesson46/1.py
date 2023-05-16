import textwrap
import unittest


c = False
a ='polina'

def calc(a):
    if type(a) == int:
        if a>=0:
            return 2023 - a
        else:
            return 'чзх'
    else:
        raise ValueError('ввести надо число')

class SimpleTest(unittest.TestCase):

    # def test_1(self):
    #     b = 'polina'
    #     self.assertEqual(a,b)
    # def testPass(self):
    #     self.assertTrue(c)
    # def testFail(self):
    #     self.assertFalse(c)

    # def test3(self):
    #     self.assertEqual(1, 3 - 1)

    # def test1(self):
    #     self.assertEqual(2, 3 - 1)

    # def test2(self):
    #     self.assertNotEqual(4,5)

    # def test4(self):
    #     self.assertEqual(1.1,3.3 - 2.2)

    # def test4(self):
    #     self.assertAlmostEqual(1.1,3.3 - 2.2,1)

    # def test5(self):
    #     self.assertNotAlmostEqual(1.1, 3.3-2.0,places=1)
    #
    # def test6(self):
    #     self.assertListEqual(
    #             [1,2,3],
    #             [1,2,3]
    #     )
    # def test7(self):
    #     self.assertDictEqual(
    #         {1:'A'},
    #             {1:'A'}
    #     )
    #
    #
    # def test8(self):
    #     self.assertCountEqual(
    #         [1,2,3,4],(2,1,3,4)
    #     )
    #
    # def test9(self):
    #     self.assertSequenceEqual(
    #         [1,2,3,4],(1,2,3,4)
    #     )
    # def test10(self):
    #     self.assertSetEqual(
    #         {1,2,4,3},{1,2,3,4}
    #     )
    # def test11(self):
    #     self.assertTupleEqual(
    #         (1,2),(1,2)
    #     )
    #
    # def test11(self):
    #     self.assertMultiLineEqual(
    #         textwrap.dedent('''Этодлинная
    #         строка'''),
    #         textwrap.dedent('''Этодлинная
    #         строка''')
    #     )
    #
    # def test12(self):
    #     self.assertIn(4,[3,3,3])
    # def test12(self):
    #     self.assertIn('4','1234')




    def testfunc(self):
        self.assertEqual(calc(2000),23)
        self.assertEqual(calc(2004), 19)
        self.assertEqual(calc(1990), 33)
        self.assertEqual(calc(-5),'чзх')

        self.assertRaises(ValueError,calc,'hdfcs')

# if round(1.1 - (3.3-2.2),1)==0:
#     print('yes')
# else:
#     print(1.1 - (3.3-2.2))


