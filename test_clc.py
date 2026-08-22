import unittest
import calculator

class test_calculator(unittest.TestCase):
    def setUp(self):
        self.calc = calculator

    def test_square(self):
        result = self.calc.square(4)
        self.assertEqual(result,16,"The square should be 16")

if __name__ == "__main__":
    unittest.main()