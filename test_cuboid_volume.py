# -*- coding: utf-8 -*-
"""
Created on Fri May 28 15:45:52 2021

@author: catal
"""
import unittest
from cuboid_volume import cuboid_volume


class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(cuboid_volume(2), 8)
        self.assertAlmostEqual(cuboid_volume(1), 1)
        self.assertAlmostEqual(cuboid_volume(0), 0)
        self.assertAlmostEqual(cuboid_volume(5.5), 166.375)


if __name__ == '__main__':
    unittest.main()
