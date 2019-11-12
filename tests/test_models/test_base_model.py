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
        creation_inst = BaseModel()
        self.assertTrue(type(creation_inst), BaseModel) 
        creation_inst.name = "Holberton"
        self.assertEqual(creation_inst, "Holberton")
        self.assertTrue(type(creation_inst.name), str)
        self.my_number = 89
        self.assertEqual(creation_inst.my_number, 89)
        self.assertEqua(type(creation_inst.my_number),int)

    def instance_creation2(self):
        """ Checking id, created and updated  *_at"""
        creation_inst = BaseModel()
        self.assertEqual(type(creation_inst.id), str)
        self.assertEqual(type(creation_inst.created_at), datetime)
        self.assertEqual(type(creation_inst.updated_at), datetime)

