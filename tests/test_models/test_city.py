<<<<<<< HEAD
from datetime import datetime
import inspect
import models
from models import city
from models.base_model import BaseModel
import unittest

class TestCity(unittest.TestCase):
    """Test the City class"""
    def setUp(self):
        print('setup')
        self.city = city()
        self.c = city()
 
    def tearDown(self):
        """teardown method"""
        print('Teardown')
        return super().tearDown()

    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""

        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_name_attr(self):
        """Test that City has attribute name, and it's an empty string"""

        self.assertTrue(hasattr(city, "name"))

    def test_state_id_attr(self):
        """Test that City has attribute state_id, and it's an empty string"""

        self.assertTrue(hasattr(city, "state_id"))

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

        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))
=======
#!/usr/bin/python3

"""
Unittesting for class City
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCityClass(unittest.TestCase):
    """
    Test City Class unittesting
    """
    @classmethod
    def setUpClass(cls):
        """
        Run prior to each test
        """
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        """
        Run at end of test
        """
        print('teardownClass')
        return super().tearDownClass()

    def setUp(self):
        """
        Run setup method prior to each test in class
        """
        print('setup')
        self.self.dummy = City()
        self.self.dummy1 = City()
        self.self.dummy2 = City()

    def tearDown(self):
        """
        Run after end of each test in class
        """
        print('teardown')
        return super().tearDown()

    def instance_creation(self):
        """
        create instance of class
        """
        ci = City()
        ci.state_id = "CA"
        ci.name = "California"
>>>>>>> 9e9ff79953b8a848b9a995b2fe48e246eef9d0b4
