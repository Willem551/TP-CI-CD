import unittest

class simpleMath:
    @staticmethod
    def addition(a, b):
       return a + b
    
    
class test_simple_math(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(simpleMath.addition(2, 3), 5)
        self.assertEqual(simpleMath.addition(1, 6), 7)
        self.assertEqual(simpleMath.addition(3, 5), 8)

        
class simpleMath:
    @staticmethod
    def soustraction(a, b):
       return a - b
    
    
class test_simple_math(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(simpleMath.soustraction(3,2), 1)
        self.assertEqual(simpleMath.soustraction(7, 1), 6)
        self.assertEqual(simpleMath.soustraction(5, 3), 2)
    
if __name__ == '__main__':
    unittest.main()
