# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:32:38 2021

@author: catal
"""

import unittest
import simpleFunctions


class TestSimpleFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(simpleFunctions.add(10, 5), 15)
        self.assertEqual(simpleFunctions.add(-10, -5), -15)
        self.assertEqual(simpleFunctions.add(1, -1), 0)

    def test_subtract(self):
        self.assertEqual(simpleFunctions.subtract(10, 2), 8)
        self.assertEqual(simpleFunctions.subtract(10, -2), 12)
        self.assertEqual(simpleFunctions.subtract(-10, 2), -12)
        self.assertEqual(simpleFunctions.subtract(-10, -2), -8)

    def test_multiply(self):
        self.assertEqual(simpleFunctions.multiply(10, 2), 20)
        self.assertEqual(simpleFunctions.multiply(-10, 0), 0)
        self.assertEqual(simpleFunctions.multiply(10, 0), 0)
        self.assertEqual(simpleFunctions.multiply(-10, 2), -20)
        self.assertEqual(simpleFunctions.multiply(-10, -2), 20)

    def test_divide(self):
        self.assertEqual(simpleFunctions.divide(10, 2), 5)
        self.assertEqual(simpleFunctions.divide(2, 10), 0.2)
        self.assertEqual(simpleFunctions.divide(10, -2), -5)
        self.assertEqual(simpleFunctions.divide(-2, 10), -0.2)
        self.assertEqual(simpleFunctions.divide(0, 10), 0)
        self.assertRaises(ValueError, simpleFunctions.divide, 10, 0)
        with self.assertRaises(ValueError):  # context manager
            simpleFunctions.divide(10, 0)

    def test_exponentiate(self):
        self.assertEqual(simpleFunctions.exponentiate(10, 2), 100)
        self.assertEqual(simpleFunctions.exponentiate(2, 10), 1024)
        self.assertEqual(simpleFunctions.exponentiate(-10, 2), 100)
        self.assertEqual(simpleFunctions.exponentiate(-10, 3), -1000)
        self.assertEqual(simpleFunctions.exponentiate(10, -2), 0.01)


if __name__ == "__main__":
    unittest.main()
