
import unittest
from fibonacci_series import get_fibonacci_numbers, fibonacci_up_to

class TestFibonacciGenerator(unittest.TestCase):
    def test_first_ten_fibonacci(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(get_fibonacci_numbers(10), expected)

    def test_invalid_count(self):
        with self.assertRaises(ValueError):
            get_fibonacci_numbers(-5)

    def test_fibonacci_up_to(self):
        self.assertEqual(fibonacci_up_to(10), [0, 1, 1, 2, 3, 5, 8])

    def test_limit_invalid_input(self):
        with self.assertRaises(ValueError):
            fibonacci_up_to(-10)


if __name__ == "__main__":
    unittest.main(verbosity=2)
