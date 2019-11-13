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
        user1 = User()
        user1.first_name = "Edward"
        user1.last_name = "Guillermo"
        user1.email = "email@toolong.com"
        user1.password = "notpassword"
