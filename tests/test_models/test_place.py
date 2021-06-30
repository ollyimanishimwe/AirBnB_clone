#!/usr/bin/python3
"""
Test cases for Place class.
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class testPlace(unittest.TestCase):
    """
    Place test class.
    """

    def test_place(self):
        """
        Testing instances.
        """
        inst = Place()
        self.assertTrue(isinstance(inst, Place))
