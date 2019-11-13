#!/usr/bin/python3

"""
Unittesting for class City
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCityClass(unittest.TestCase):
    """
    Test City Class unittesting
    """
    @classmethod
    def setUpClass(cls):
        """
        Run prior to each test
        """
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        """
        Run at end of test
        """
        print('teardownClass')
        return super().tearDownClass()

    def setUp(self):
        """
        Run setup method prior to each test in class
        """
        print('setup')
        self.self.dummy = City()
        self.self.dummy1 = City()
        self.self.dummy2 = City()

    def tearDown(self):
        """
        Run after end of each test in class
        """
        print('teardown')
        return super().tearDown()
