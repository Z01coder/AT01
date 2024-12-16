import unittest
from main import add, subtract, multiply, divide, modulus

class TestMath(unittest.TestCase):
    def test_add(self):
       self.assertEqual(add(2, 5),7)
       self.assertNotEqual(add(3, 7), 9)

    def test_subtract(self):
       self.assertEqual(subtract(7, 4), 3)
       self.assertNotEqual(subtract(4, 2), 1)

    def test_multiply(self):
       self.assertNotEqual(multiply(2, 5), 12)
       self.assertEqual(multiply(3, 6), 18)

    def test_divide(self):
       self.assertNotEqual(divide(4, 2), 3)
       self.assertEqual(divide(20, 5), 4)

       with self.assertRaises(ZeroDivisionError):
          divide(10, 0)                                 # Проверка деления на ноль

    # Проверка функции modulus
    def test_modulus(self):
       self.assertEqual(modulus(10, 3), 1)
       self.assertEqual(modulus(15, 5), 0)
       self.assertNotEqual(modulus(10, 4), 3)
       self.assertEqual(modulus(9, 2), 1)
       self.assertEqual(modulus(-9, 2), -1)                # Проверка с отрицательными числами
       self.assertEqual(modulus(0, 5), 0)        # Остаток от деления нуля

       with self.assertRaises(ValueError):                     # Проверка деления на ноль с использованием assertRaises
          modulus(10, 0)

if __name__ == '__main__':
   unittest.main()
