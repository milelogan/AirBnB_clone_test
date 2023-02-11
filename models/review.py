#!/usr/bin/python3
"""This module defines Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines a users state"""

    place_id = ""
    user_id = ""
    text = ""
