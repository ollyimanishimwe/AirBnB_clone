#!/usr/bin/python3
"""
FileStorage class Unittest cases.
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review


class testFileStorage(unittest.TestCase):
    """
    FileStorage class test cases.
    """

    def test_fs(self):
        """
        verify fs
        """
        st = FileStorage()
        objs = st.all()
        for k, v in objs.items():
            self.assertTrue(issubclass(eval(k.split('.')[0]), BaseModel))
