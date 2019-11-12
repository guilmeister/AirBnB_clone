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

def test_different_id(self):
        """ id should be different """
        dummy1 = BaseModel()
        dummy2 = BaseModel()
        self.assertNotEqual(dummy1.id, dummy2.id)
        self.assertEqual(len(dummy1.id), len(dummy2.id))

def test_strMethod(self):
        """ check __str__ output """
        dummy = BaseModel()
        my_str = "[BaseModel] ({}) {}".format(dummy.id, dummy.__dict__)
        self.assertEqual(my_str, str(dummy))

def test_save(self):
        """ save updated_at """
        dummy = BaseModel()
        dum1 = dummy.updated_at
        dummy.save()
        dum2 = dummy.updated_at
        self.assertNotEqual(dum1, dum2)

def test_to_dict(self):
        """ dictionary conversion """
        dummy = BaseModel()
        dummy.name = "Akeem"
        dummy.my_number = 89
        dicti = dummy.to_dict()
        my_keys = ["id",
                   "name",
                   "my_number",
                   "created_at",
                   "updated_at",
                   "__class__"]
        self.assertEqual(dicti["name"], "Akeem")
        self.assertEqual(dicti["my_number"], 89)
        self.assertEqual(dicti["__class__"], "BaseModel")
        self.assertCountEqual(dicti.keys(), my_keys)

def test_to_dict_attr(self):
        """ created_at, updated_at values """
        dummy = BaseModel()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        dicti = dummy.to_dict()
        self.assertEqual(dicti["created_at"], dummy.created_at.strftime(time_format))
        self.assertEqual(dicti["updated_at"], dummy.updated_at.strftime(time_format))
        self.assertEqual(dicti["__class__"], "BaseModel")
        self.assertEqual(type(dicti["created_at"]), str)
        self.assertEqual(type(dicti["updated_at"]), str)

if __name__ == '__main__':
    unittest.main()
