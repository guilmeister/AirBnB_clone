#!/usr/bin/python3

"""
This module is for Review Class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class Review
    """
    place_id = ""
    user_id = ""
    text = ""
