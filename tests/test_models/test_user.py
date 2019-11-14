#!/usr/bin/python3
""" Unittest for User """
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel
import os
import pep8


class TestUser(unittest.TestCase):
    """ Runs Test for User.py """

    def setUp(self):
        """ Sets Up Testing Environment """

        self.user1 = User()
        self.user2 = User()

        self.attributes = {
            "User":
            {"email": str,
             "password": str,
             "first_name": str,
             "last_name": str},
        }
    def tearDown(self):
        """Tears down testing environment"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_createNewUser(self):
        """Checks for successful creation of new user"""
        self.assertTrue(self.user1)

    def test_createUserId(self):
        """Checks ID is present"""
        self.assertTrue(self.user1.id)

    def test_uniqueUserId(self):
        """Checks IDs against eachother"""
        self.assertNotEqual(self.user1.id, self.user2.id)

    def test_Instantation(self):
        """Checks that User inherits from BaseModel"""
        self.assertIsInstance(self.user1, User)
        self.assertTrue(issubclass(type(self.user1), BaseModel))
        self.assertEqual(str(type(self.user1)), "<class 'models.user.User'>")

    def test_toDict(self):
        """Checks output when using to_dict()"""
        self.assertFalse("__class__" in self.user1.__dict__)
        self.assertFalse("__class__" in self.user2.__dict__)
        dict_check = self.user1.to_dict()
        self.assertTrue("__class__" in dict_check)
        self.assertFalse("__class__" in self.user2.__dict__)

    def test_setting_attributeValues(self):
        """Checks you can change the name"""
        self.user1.first_name = "Akeem"
        self.user1.last_name = "Seymens"
        self.user1.email = "akeemseymens@test.com"
        self.user1.password = "pass"
        self.assertTrue(self.user1.first_name, "Akeem")
        self.assertTrue(self.user1.last_name, "Seymens")
        self.assertTrue(self.user1.email, "Akeem@test.com")
        self.assertTrue(self.user1.password, "pass")

    def test_attribute_and_values(self):
        """Checks through attributes"""
        attributes = self.attributes["User"]
        akeem = User()
        for k, v in attributes.items():
            self.assertTrue(hasattr(akeem, k))
            self.assertEqual(type(getattr(akeem, k, None)), v)
            self.assertTrue(type(v), str)

    def test_compare_create_and_update(self):
        """Makes sure create and update are slightly different"""
        self.assertNotEqual(self.user1.created_at, self.user2.updated_at)

    def test_updateAt_updates(self):
        """Makes sure updated_at updates"""
        tmp = self.user1.updated_at
        self.user1.save()
        self.assertNotEqual(tmp, self.user1.updated_at)

    def test_consistent_idLength(self):
        """Checks to make sure id is the right amount of characters"""
        self.assertTrue(len(self.user1.id), 33)
        self.assertTrue(len(self.user2.id), 33)

    def test_diff_ids(self):
        """Checks to make sure id is the right amount of characters"""
        self.assertNotEqual(self.user1.id, self.user2.id)

    def test_to_dict(self):
        """Tests the to_dict() method"""
        self.assertEqual(dict, type(self.user1.to_dict()))
        self.assertEqual(dict, type(self.user2.to_dict()))

    def test_pep8_conformance(self):
        """test for pep8 conformance"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "Found pep8 errors")