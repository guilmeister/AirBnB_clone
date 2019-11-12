#!/usr/bin/python3

"""
Testing outputs for BaseModel
"""

from models.base_model import BaseModel


class TestBaseClass(unittest.TestCase):
    """
    Test Base Model class unittesting
    """

    def instance_creation(self):
        """
        Create instance of Class Base Model
        """
        self.base = BaseModel()
