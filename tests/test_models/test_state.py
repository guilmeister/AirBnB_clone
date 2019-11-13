#!/usr/bin/python3

"""
Testing outputs for State class
"""

from models.base_model import BaseModel
from models.state import State
import unittest


class TestStateClass(unittest.TestCase):
    """
    Test State class unittesting
    """

    def instance_creation(self):
        """
        Create instance of Class State
        """
        self.state = State()
