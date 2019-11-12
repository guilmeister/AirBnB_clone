#!/usr/bin/python3

"""
Testing output for FileStorage
"""

from models.engine.file_storage import FileStorage


class TestFileStorageClass(unittest.Testcase):
    """
    Test file storage unittesting
    """

    def instance_creation(self):
        """
        Create instance of Class File Storage
        """
        self.s = FileStorage()
