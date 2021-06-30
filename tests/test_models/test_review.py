#!/usr/bin/python3
"""
Test cases for Review class.
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class testReview(unittest.TestCase):
    """
    Review test class.
    """

    def test_review(self):
        """
        Testing instances.
        """
        inst = Review
        self.assertTrue(issubclass(inst, BaseModel))
