import unittest
from simple_math import simpleMath

class test_simple_math(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(simple_math.addition(2,3),5)

if  name  =='  main  ' :    
unittest.main()  