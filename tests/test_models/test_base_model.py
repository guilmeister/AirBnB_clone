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
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        return super().tearDownClass()

    def setUp(self):
        print('setup')
        self.self.dummy = BaseModel()
        self.self.dummy1 = BaseModel()
        self.self.dummy2 = BaseModel()
    

    def tearDown(self):
        print('teardown')
        return super().tearDown()

    def instance_creation(self):
        """ Create instance of Class Base Model name, number & class type."""

        self.assertTrue(type(self.dummy), BaseModel) 
        self.dummy.name = "Holberton"
        self.assertEqual(self.dummy, "Holberton")
        self.assertTrue(type(self.dummy.name), str)
        self.my_number = 89
        self.assertEqual(self.dummy.my_number, 89)
        self.assertEqua(type(self.dummy.my_number),int)

    def instance_creation2(self):
        """ Checking id, created and updated  *_at"""

        self.assertEqual(type(self.dummy.id), str)
        self.assertEqual(type(self.dummy.created_at), datetime)
        self.assertEqual(type(self.dummy.updated_at), datetime)
        
    def default_attributes(self):
        """ id, created_at, updated_at default attributes """

        self.assertTrue(hasattr(self.dummy, "id"))
        self.assertTrue(hasattr(self.dummy, "created_at"))
        self.assertTrue(hasattr(self.dummy, "updated_at"))

    def test_different_id(self):
        """ id should be different """

        self.assertNotEqual(self.dummy1.id, self.dummy2.id)
        self.assertEqual(len(self.dummy1.id), len(self.dummy2.id))

    def test_strMethod(self):
        """ check __str__ output """

        my_str = "[BaseModel] ({}) {}".format(self.dummy.id, self.dummy.__dict__)
        self.assertEqual(my_str, str(self.dummy))

    def test_save(self):
        """ save updated_at """

        dum1 = self.dummy.updated_at
        self.dummy.save()
        dum2 = self.dummy.updated_at
        self.assertNotEqual(dum1, dum2)

    def test_to_dict(self):
        """ dictionary conversion """

        self.dummy.name = "Akeem"
        self.dummy.my_number = 89
        dicti = self.dummy.to_dict()
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

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        dicti = self.dummy.to_dict()
        self.assertEqual(dicti["created_at"], self.dummy.created_at.strftime(time_format))
        self.assertEqual(dicti["updated_at"], self.dummy.updated_at.strftime(time_format))
        self.assertEqual(dicti["__class__"], "BaseModel")
        self.assertEqual(type(dicti["created_at"]), str)
        self.assertEqual(type(dicti["updated_at"]), str)

if __name__ == '__main__':
    unittest.main()
