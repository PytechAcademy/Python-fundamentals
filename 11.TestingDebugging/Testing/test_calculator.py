import unittest
from calculator import add, product
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
    def test_product(self):
        self.assertEqual(product(5,6),30)
        self.assertEqual(product(-3,5),-15)
        self.assertEqual(product(0, 5), 0)

if __name__ == '__main__':
    unittest.main()