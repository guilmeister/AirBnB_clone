#!/usr/bin/python3

"""
huehuehue
"""

import json

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary."""
        return __objects

    def new(self, obj):
        """sets the objects with key"""
        self.__objects = obj.__class__.__name__.id

    def save(self):
        return json.dumps(__file_path)

    def reload(self):
        return json.loads(__file_path)
