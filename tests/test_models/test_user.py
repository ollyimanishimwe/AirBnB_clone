#!/usr/bin/python3
"""
Test cases for User class.
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class testUser(unittest.TestCase):
    """
    User test class.
    """

    def test_user(self):
        """
        Testing instances.
        """
        inst = User()
        self.assertTrue(isinstance(inst, User))
