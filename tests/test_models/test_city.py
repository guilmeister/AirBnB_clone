#!/usr/bin/python3

from datetime import datetime
import inspect
from models.city import City
from models.base_model import BaseModel
import unittest

class TestCity(unittest.TestCase):
    """Test the City class"""
    @classmethod
    def setUpClass(cls):
        """
        Run prior to each test in class
        """
        print('SetupClass City')

    @classmethod
    def tearDownClass(cls):
        """
        Run at end after test
        """
        print('tearDownClass City')
    
    
    def setUp(self):
        print('setup')
        self.city = City()
        self.c = City()
 
    def tearDown(self):
        """teardown method"""
        print('Teardown')
        return super().tearDown()

    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""

        self.assertIsInstance(self.city, BaseModel)
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_name_attr(self):
        """Test that City has attribute name, and it's an empty string"""

        self.assertTrue(hasattr(self.city, "name"))
    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        
        new_d = self.c.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in self.c.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""

        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        new_d = self.c.to_dict()
        self.assertEqual(new_d["__class__"], "City")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], self.c.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], self.c.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""

        string = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(string, str(self.city))
    
    def test_inheritence(self):
        """Checks to make sure City inherits from BaseModel"""

        self.assertTrue(issubclass(City, BaseModel))    
    
    def test_new_instances(self):
        """Checks that new instances were created"""

        self.assertTrue(self.city)
        self.assertTrue(self.city)