# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:32:38 2021

@author: catal
"""

import unittest
import simpleFunctions

# print(simpleFunctions.add(1, 2))


class TestSimpleFunctions(unittest.TestCase):

    def test_add(self):
        result = simpleFunctions.add(10, 5)
        self.assertEqual(result, 15)
