#!/usr/bin/python3

"""
This is a module for Base Class

"""

import uuid
import datetime
import models


class BaseModel:
    """
    Class BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        Function that initializes attributes
        """
        formatting = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key,
                            datetime.datetime.strptime(value, formatting))
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return string representation of an object
        """
        string = "[{}] ({}) {}".format(self.__class__.__name__,
                                       self.id,
                                       self.__dict__)
        return string

    def save(self):
        """
        Function that updates the public instance attribute
        updated_at with current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Function that returns a dictionary with the class name
        of the object and created_at and updated_at attributes
        are converted to string format in ISO format
        """
        my_dict = self.__dict__.copy()
        my_dict.update({'__class__': str(type(self).__name__)})
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["created_at"] = self.created_at.isoformat()
        return my_dict
