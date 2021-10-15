# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:50:28 2021

@author: catal
"""

import unittest
import employee
import requests
from unittest.mock import patch


class TestEmployee(unittest.TestCase):

    # def setupClass(cls):   # class method
    #     """is auto-run before the first test"""
    #     pass

    # def tearDownClass(cls):   # class method
    #     """is auto-run after the last test"""
    #     pass

    def setUp(self):  # instance method
        """is auto-run before each test"""
        self.emp_1 = employee.Employee("Hachi", "Goodyear", 80000)
        self.emp_2 = employee.Employee("Midas", "Goodyear", 90000)

    def tearDown(self):  # instance method
        """is auto-run after each test"""
        pass

    def test_email(self):  # instance method
        """tests employee.email()"""
        self.assertEqual(self.emp_1.email, "Hachi.Goodyear@email.com")
        self.assertEqual(self.emp_2.email, "Midas.Goodyear@email.com")

        self.emp_1.first = "Not-Muffin"
        self.emp_2.last = "Daoust"
        self.assertEqual(self.emp_1.email, "Not-Muffin.Goodyear@email.com")
        self.assertEqual(self.emp_2.email, "Midas.Daoust@email.com")

    def test_fullname(self):  # instance method
        """tests employee.fullname()"""
        self.assertEqual(self.emp_1.fullname, "Hachi Goodyear")
        self.assertEqual(self.emp_2.fullname, "Midas Goodyear")

        self.emp_1.first = "Not-Muffin"
        self.emp_2.last = "Daoust"
        self.assertEqual(self.emp_1.fullname, "Not-Muffin Goodyear")
        self.assertEqual(self.emp_2.fullname, "Midas Daoust")

    def test_apply_raise(self):  # instance method
        """tests employee.apply_raise()"""
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        self.assertEqual(self.emp_1.pay, 84000)
        self.assertEqual(self.emp_2.pay, 94500)

        self.emp_1.apply_raise()
        self.assertEqual(self.emp_1.pay, 88200)

    def test_monthly_schedule(self):  # instance method
        """tests employee.monthly_schedule"""
        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "sucess"
            schedule = self.emp_1.monthly_schedule("May")
            mocked_get.assert_called_with("http://company.com/Goodyear/May")
            self.assertEqual(schedule, "sucess")

            mocked_get.return_value.ok = False
            mocked_get.return_value.text = "Bad Response!"
            schedule = self.emp_2.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Goodyear/June")
            self.assertEqual(schedule, "Bad Response!")


if __name__ == "__main__":
    unittest.main()
