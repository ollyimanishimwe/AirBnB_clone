#!/usr/bin/python3
"""
Unittest for BaseModel class.
"""
import models
from models.base_model import BaseModel
import datetime
import unittest
import uuid


class test_file(unittest.TestCase):
    """
    Test BaseModel class.
    """

    def test_bm(self):
        """
        Test BaseModel class id values.
        """
        bs1 = BaseModel()
        bs2 = BaseModel()
        self.assertTrue(isinstance(bs1, BaseModel))
        self.assertNotEqual(bs1.id, bs2.id)
        bs1.name = "Holberton"
        self.assertEqual(bs1.name, "Holberton")
        self.assertTrue(isinstance(bs1.name, str))
        bs1.age = 5
        self.assertEqual(bs1.age, 5)
        self.assertTrue(isinstance(bs1.age, int))
        self.assertTrue(isinstance(bs1.created_at, datetime.datetime))
        self.assertTrue(isinstance(bs1.updated_at, datetime.datetime))
        self.assertTrue(isinstance(bs1.id, str))
        self.assertTrue(isinstance(bs1.to_dict(), dict))
        self.assertTrue(hasattr(bs1, 'id'))
        self.assertTrue(hasattr(bs1, 'created_at'))
        self.assertTrue(hasattr(bs1, 'updated_at'))
        self.assertTrue(hasattr(bs1, 'age'))
        self.assertTrue(hasattr(bs1, 'name'))
        self.assertTrue(hasattr(eval(bs1.__class__.__name__), '__str__'))
        dic = bs1.to_dict()
        self.assertTrue(hasattr(dic, '__class__'))

        self.assertTrue(hasattr(bs1, 'to_dict'))
        self.assertTrue(hasattr(bs1, '__str__'))

        self.assertTrue(callable(type(bs1.to_dict())))
        self.assertTrue(callable(type(bs1.__str__())))

        s0 = str(bs1)
        self.assertMultiLineEqual(bs1.__str__(), str(bs1))

        my_dict = {}
        for k, v in bs1.__dict__.items():
            if k == 'created_at':
                my_dict[k] = v.isoformat()
            elif k == 'updated_at':
                my_dict[k] = v.isoformat()
            else:
                my_dict[k] = v
            my_dict['__class__'] = bs1.__class__.__name__

        self.assertDictEqual(bs1.to_dict(), my_dict)

        d1 = bs1.updated_at
        bs1.save()
        objs = models.storage.all()
        key = 'BaseModel' + '.' + bs1.id
        if key in objs:
            r = objs[key].to_dict()
            for k, v in r.items():
                self.assertEqual(r[k], bs1.to_dict()[k])
        d2 = bs1.updated_at
        self.assertNotEqual(d1, d2)

        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        for key in my_model_json.keys():
            self.assertTrue(
                hasattr(my_model, key)
                )
