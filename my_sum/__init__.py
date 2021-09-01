# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:02:51 2020

@author: Barbara
"""

import unittest


def sum_stuff(arg):
    total = 0
    for val in arg:
        total += val 
    return total