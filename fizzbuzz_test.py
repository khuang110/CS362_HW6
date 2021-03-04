import unittest
from fizzbuzz import fizz_buzz


class TestCase(unittest.TestCase):
    # test case if it is not number 1-100
    def test_fizz1(self):
        self.assertIsNone(fizz_buzz(0))
