#!/usr/bin/python3
"""
serializes/deserializes JSON
"""
import json
import sys
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    Attributes:
    __file_path: Path to JSON file
    __objects: Dictionary storing all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in _objects the obj with key
        <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + getattr(obj, "id")
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes _objects to the JSON file
        """
        with open(FileStorage.__file_path, mode='w', encoding='UTF-8') as f:
            my_obj = {}
            for k, v in FileStorage.__objects.items():
                my_obj[k] = v.to_dict()
            my_str = json.dumps(my_obj)
            f.write(my_str)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, mode='r') as f:
                r = json.load(f)
                for k, v in r.items():
                    cls_name = k.split('.')[0]
                    my_obj = eval(cls_name)(**v)
                    self.new(my_obj)
        except:
            pass
