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

    def subtraction_test(self):
        calculator = Calculator()
        result = calculator.sub(2,2)
        self.assertEqual(0,result)

    def multiplication_test(self):
        calculator = Calculator()
        result = calculator.sub(2,2)
        self.assertEqual(4,result)

    def division_test(self):
        calculator = Calculator()
        result = calculator.mult(2,2)
        self.assertEqual(1, result)

    def square_root_test(self):
        calculator = Calculator()
        result = calculator.root(8)
        self.assertEqual(3,result)

    def square_test(self):
        calculator = Calculator()
        result = calculator.square(2,2)
        self.assertEqual(4,result)






if __name__ == '__main__':
    unittest.main()