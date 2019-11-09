#!/usr/bin/python3

"""
huehuehue
"""

import json
from models.base_model import BaseModel

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary."""
        return self.__objects

    def new(self, obj):
        """sets the objects with key"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as g:
            copy_dict = {key: self.__objects[key].to_dict()
                        for key in self.__objects}
            json.dump(copy_dict, g)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.__objects[key] = eval(key.split('.')[0])(**value)
        except FileNotFoundError:
            pass
