#!/usr/bin/python3

"""
asdsada
"""

import uuid
import datetime

class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        string = "[{}] ({}) <{}>".format(self.__class__.__name__,
                                         self.id,
                                         self.__dict__)
        return string

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        my_dict = {'my_number': self.my_number,
                   'name': self.name,
                   '__class__': self.__class__.__name__,
                   'updated_at:': self.updated_at.isoformat(),
                   'id': self.id,
                   'created_at': self.created_at.isoformat()}
        return my_dict
