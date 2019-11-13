#!/usr/bin/python3

"""
This is a module for FileStorage Class
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Class FileStorage
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Function that returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Function that sets in __object the obj
        with key <obj class name>.id
        """
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Function that serializes __object to the JSON file
        """
        with open(FileStorage.__file_path, 'w') as saves:
            copy_dict = {key: self.__objects[key].to_dict()
                         for key in self.__objects}
            json.dump(copy_dict, saves)

    def reload(self):
        """
        Function that deserializes JSON file to __objects
        if __file_path exists
        """
        try:
            with open(self.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.__objects[key] = eval(key.split('.')[0])(**value)
        except FileNotFoundError:
            pass
