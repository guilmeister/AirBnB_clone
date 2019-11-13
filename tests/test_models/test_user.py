#!/usr/bin/python3

"""
Testing outputs for User
"""

from models.base_model import BaseModel
from models.user import User
import unittest


class TestUserClass(unittest.TestCase):
    """
    Test User class unittesting
    """

    def instance_creation(self):
        """
        Create instance of Class User
        """
        self.user = User()
