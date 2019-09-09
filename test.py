""" Author: Michael Harmon
    Last Date Modified: 09/07/2019
    Description: These unit tests with test the average()
    from average_scores.py
"""


import unittest
from unittest import mock

from format_output import average_scores as avg


class MyTestCase(unittest.TestCase):
    def test_average_positive(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert avg.average() == 90

    def test_average_negative(self):
        with mock.patch('builtins.input', side_effect=[98, 93, 88]):
            assert avg.average() != 91


if __name__ == '__main__':
    unittest.main()

"""The unit tests ensured that the average method was actually returning the average.
    I added a positive test that returned the correct average and a negative test
    that would not return the correct average.
    This will ensure the average() method is calculating correctly.
"""
