#!/usr/bin/python3
"""
Test cases for City class.
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class testCity(unittest.TestCase):
    """
    City test class.
    """

    def test_city(self):
        """
        Testing instances.
        """
        inst = City()
        self.assertTrue(isinstance(inst, City))
