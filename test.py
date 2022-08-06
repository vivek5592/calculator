# Python code to demonstrate working of unittest
import unittest
import main
  
class TestCalculatorMethods(unittest.TestCase):
      
    def setUp(self):
        pass
    
    def test_add(self):
        response = main.add(2,3)
        self.assertEqual(response, 5)
    
    def test_multiply(self):
        response = main.multiply(2,3)
        self.assertEqual(response, 6)
    
    def test_divide(self):
        response = main.devide(6, 2)
        self.assertEqual(response, 3)
    
    # Failed Tests

    def test_add_2(self):
        response = main.add(2,3)
        self.assertNotEqual(response, 5)
    
    def test_multiply_2(self):
        response = main.multiply(2,3)
        self.assertNotEqual(response, 6)
  
if __name__ == '__main__':
    unittest.main()