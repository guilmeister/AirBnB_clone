#!/usr/bin/python3

"""
Testing outputs for BaseModel
"""

from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReviewClass(unittest.TestCase):
    """
    Test Review class unittesting
    """

    def instance_creation(self):
        """
        Create instance of Class Place
        """
        self.review = Review()
