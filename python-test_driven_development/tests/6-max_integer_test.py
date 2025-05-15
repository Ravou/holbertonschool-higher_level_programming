#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_all_equal(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-2, -4, -1, -10]), -1)

    def test_mix_positive_negative(self):
        self.assertEqual(max_integer([-1, 3, 2, -5]), 3)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_list_of_zeros(self):
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.3, 0.7]), 2.3)

    def test_mixed_int_float(self):
        self.assertEqual(max_integer([1, 2.5, 3, 2]), 3)

    def test_string_list(self):
