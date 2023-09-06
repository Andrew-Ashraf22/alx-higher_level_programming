#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_normal_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 6]), 6)
        self.assertEqual(max_integer([22, 1, 3, 4, 2]), 22)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([512]), 512)
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([6, -1, 2, -8]), 6)
        self.assertEqual(max_integer([-52, -1, 0, -0.5]), 0)
        self.assertEqual(max_integer([1.0, 2.6, -7.7, 55.9]), 55.9)
        self.assertEqual(max_integer(["ss", "daw", "lol", "ze"]), "ze")

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))


if __name__ == '__main__':
    unittest.main()
