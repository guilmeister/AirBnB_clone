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
        rev = Review()
        rev.place_id = "place id"
        rev.user_ud = "Holberton"
        rev.text = "5 of 5 stars"
