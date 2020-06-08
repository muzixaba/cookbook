import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(3,4), 7)
        self.assertEqual(calc.add(-3,4), 1)
        self.assertEqual(calc.add(-3,-4), -7)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertEqual(calc.divide(-3,-3), 1)
        self.assertEqual(calc.divide(-3, 1), -3)

        # catch a zero division error
        self.assertRaises(ValueError, calc.divide, 10, 0)

        # catch exceptions using context manager
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

# run unittest as main module (python -m unittest test_module_name.py)
# or
if __name__ == "__main__":
    unittest.main()