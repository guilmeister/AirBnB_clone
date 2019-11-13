#!/usr/bin/python3

"""
Testing outputs for BaseModel
"""

from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlaceClass(unittest.TestCase):
    """
    Test Place class unittesting
    """

    def instance_creation(self):
        """
        Create instance of Class Place
        """
        pl = Place()
        pl.city_id = "some city id"
        pl.user_id = "some user id"
        pl.name = "Holberton"
        pl.description = "Software Engineering school"
        pl.number_rooms = 4
        pl.number_bathrooms = 2
        pl.max_guest = 5
        pl.price_by_night = 1500
        pl.latitude = 1.5
        pl.longitude = 2.5
        pl.amenity_ids = ["some", "amenity", "string", "in list"]
