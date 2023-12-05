import unittest

from math_operations import addition_operation
from math_operations import subtraction_operation
 
class TestMathOperations(unittest.TestCase):
    @unittest.skip('Operação de Adição')
    def test_addition_operation(self):
        math_addition_result = addition_operation(num_1=5, num_2=10)
        self.assertEqual(math_addition_result, 15)

    @unittest.skip('Operação de Subtração')
    def test_subtraction_operation(self):
        math_subtraction_result = subtraction_operation(num_1=10, num_2=10)
        self.assertEqual(math_subtraction_result, 0)

if __name__ == '__main__':
    unittest.main()    