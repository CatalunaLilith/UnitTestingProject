# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 11:21:51 2021

@author: catal
"""


def add(x, y):
    """assumes x and y are numbers
    returns a number, representing x + y"""
    return x + y


def subtract(x, y):
    """assumes x and y are numbers
    returns a number, representing x - y"""
    return x - y


def multiply(x, y):
    """assumes x and y are numbers
    returns a number, representing x * y"""
    return x * y


def divide(x, y):
    """assumes x and y are numbers
    returns a number, representing x / y"""
    if y == 0:
        raise ValueError("division by zero is forbiden")
    else:
        return x / y


def exponentiate(x, y):
    """assumes x and y are numbers
    returns a number, representing x ** y"""
    return x ** y
