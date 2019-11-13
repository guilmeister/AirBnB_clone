#!/usr/bin/python3

"""
Unittesting for class Amenity
"""

from datetime import datetime
import inspect
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestAmenity(unittest.TestCase):
    """
    Test the Amenity class
    """
    def setUp(self):
        """
        Run prior to each test in the class
        """
        print('setup')
        self.dummy_amenity = Amenity()
        self.dummy_amenity.name = "Yerba Mate"

    def tearDown(self):
        """
        Run at end of every test
        """
        print('tearDown\n')

    def test_is_subclass(self):
        """
        Test that Amenity is a subclass of BaseModel
        """
        self.assertIsInstance(self.dummy_amenity, BaseModel)
        self.assertTrue(hasattr(self.dummy_amenity, "id"))
        self.assertTrue(hasattr(self.dummy_amenity, "created_at"))
        self.assertTrue(hasattr(self.dummy_amenity, "updated_at"))

    def test_name_attr(self):
        """
        Test that Amenity has attribute name, and it's as an empty string
        """
        self.assertTrue(hasattr(self.dummy_amenity, "name"))

    def test_to_dict_creates_dict(self):
        """
        Test to_dict method creates a dictionary with proper attrs
        """
        am = Amenity()
        new_d = am.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in am.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """
        Test that values in dict returned from to_dict are correct
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Amenity()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "Amenity")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], am.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], am.updated_at.strftime(t_format))

    def test_str(self):
        """
        Test that the str method has the correct output
        """
        string = "[Amenity] ({}) {}".format(self.dummy_amenity.id,
                                            self.dummy_amenity.__dict__)
        self.assertEqual(string, str(self.dummy_amenity))
