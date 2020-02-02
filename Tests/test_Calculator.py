import unittest
from Calculator.Calculator import Calculator

class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(self.calculator, Calculator)

    def addition_test(self):
        calculator = Calculator()
        result = calculator.add(2,2)
        self.assertEqual(4,result)






if __name__ == '__main__':
    unittest.main()