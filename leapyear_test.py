import unittest
import io   # Used for io redirection
import sys
from leapyear import leap_year


class LeapYearTest(unittest.TestCase):
    # Test if year is divisible by 4
    def test_div_by_4(self):
        # Redirect stdout and capture output
        out = io.StringIO()
        sys.stdout = out
        leap_year(2016)
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "2016 is a leap year\n")
