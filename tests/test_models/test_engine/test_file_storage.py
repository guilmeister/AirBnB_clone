#!/usr/bin/python3

"""
Unittest for FileStorage class
"""

import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """
    FileStorage class
    """

    @classmethod
    def setUpClass(cls):
        """
        Run at start of every test
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
        Run at start prior to each test in the class
        """
        dummy = FileStorage()

    def tearDown(self):
        """
        Run at the end of every test in the class
        """
        pass

    def test_all(self):
        """
        type of dictionary
        """
        storage.reload()
        self.assertEqual(type(self.dummy.all()), dict)

    def test_new(self):
        """
        new method
        """
        storage.reload()
        self.dummy.new(BaseModel())
        self.assertTrue(self.dummy.all())

    def test_save(self):
        """
        json file check
        """

        storage.reload()
        self.dummy.new(BaseModel())
        self.dummy.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_reload(self):
        """
        Reload method
        """
        storage.reload()
        my_model = BaseModel()
        key = "BaseModel" + "." + my_model.id
        self.dummy.new(my_model)
        self.dummy.save()
        self.dummy.reload()
        self.assertTrue(self.dummy.all()[key])

if __name__ == '__main__':
    unittest.main()
