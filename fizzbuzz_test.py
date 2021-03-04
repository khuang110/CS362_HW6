import unittest
import io
import sys
from fizzbuzz import fizz_buzz


class TestCase(unittest.TestCase):
    # test case if it is not number 1-100.
    def test_fizz1(self):
        self.assertIsNone(fizz_buzz(0))

    # Test case for a good number between 1-100.
    # Not a multiple of 3 or 3 and 5
    def test_fizz2(self):
        # Redirect stdout and capture output
        out = io.StringIO()
        sys.stdout = out
        fizz_buzz(1)
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "1\n")

    # Test case for a good number
    # Test for a multiple of 3
    def test_fizz3(self):
        # Redirect stdout and capture output
        out = io.StringIO()
        sys.stdout = out
        fizz_buzz(6)
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "Fizz\n")  # Fizz expected output

    # Test case for a good number
    # Test for a multiple of 3 and 5
    def test_fizz4(self):
        # Redirect stdout and capture output
        out = io.StringIO()
        sys.stdout = out
        fizz_buzz(15)
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "FizzBuzz\n") # FizzBuzz expected output

