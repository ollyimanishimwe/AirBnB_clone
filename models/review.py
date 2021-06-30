#!/usr/bin/python3
"""
User class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class
    Attributes:
    place_id: string - empty string or the Place id
    user_id: string - empty string or the User id
    text: string - might be empty string
    """
    place_id = ""
    user_id = ""
    text = ""
