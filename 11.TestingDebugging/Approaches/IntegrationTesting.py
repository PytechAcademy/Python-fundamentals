import unittest

def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

class TestMultiplyAndAddFunctions(unittest.TestCase):
    def test_multiply_and_add(self):
        result = multiply(2, 3) + add(1, 1)
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()