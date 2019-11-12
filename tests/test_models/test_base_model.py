#!/usr/bin/python3

"""
Testing outputs for BaseModel
"""
import unittest
from datetime import datetime, date, time
import uuid
from models import storage
from models.base_model import BaseModel


class TestBaseClass(unittest.TestCase):
    """
    Test Base Model class unittesting
    """

    def instance_creation(self):
        """
        Create instance of Class Base Model name, number & class type.
        """
        dummy = BaseModel()
        self.assertTrue(type(dummy), BaseModel) 
        dummy.name = "Holberton"
        self.assertEqual(dummy, "Holberton")
        self.assertTrue(type(dummy.name), str)
        self.my_number = 89
        self.assertEqual(dummy.my_number, 89)
        self.assertEqua(type(dummy.my_number),int)

    def instance_creation2(self):
        """ Checking id, created and updated  *_at"""
        dummy = BaseModel()
        self.assertEqual(type(dummy.id), str)
        self.assertEqual(type(dummy.created_at), datetime)
        self.assertEqual(type(dummy.updated_at), datetime)
        
    def default_attributes(self):
        """ id, created_at, updated_at default attributes """
        dummy = BaseModel()
        self.assertTrue(hasattr(dummy, "id"))
        self.assertTrue(hasattr(dummy, "created_at"))
        self.assertTrue(hasattr(dummy, "updated_at"))

