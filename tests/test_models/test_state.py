#!/usr/bin/python3
"""
Test cases for State class.
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class testState(unittest.TestCase):
    """
    State test class.
    """

    def test_state(self):
        """
        Testing instances.
        """
        inst = State()
        self.assertTrue(isinstance(inst, State))
