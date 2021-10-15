# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:08:59 2020

@author: Barbara
"""

import unittest
from my_sum import sum_stuff


class TestSum(unittest.TestCase):

    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        print("running test_list_int")
        data = [1, 2, 3]
        result = sum_stuff(data)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
