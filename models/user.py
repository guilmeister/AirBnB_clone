#!/usr/bin/python3

"""
This is a module for the User class
"""

from models.base_model import BaseModel


class User(BaseModel):

    email = ""
    password = ""
    first_name = ""
    last_name = ""
