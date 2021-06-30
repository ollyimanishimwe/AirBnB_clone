#!/usr/bin/python3
"""
User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class
    Attributes:
    email: User's email
    password: User's password
    first_name: User's First name
    last_name: User's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
