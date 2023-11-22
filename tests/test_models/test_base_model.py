#!/usr/bin/python3
"""Module for test BaseModel class"""
import unittest
from datetime import datetime
import json
from models.base_model import BaseModel
from os import remove
from uuid import UUID


class TestBaseModel(unittest.TestCase):
    """ Test for BaseModel class """

    def test_setup(self):
        super().setUp()
        self.name = 'BaseModel'
        self.value = BaseModel

    def tearDown(self):
        """ TearDown for the tests """
        try:
            remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """ Test default BaseModel """
        val = self.value()
        self.assertEqual(type(val), self.value)

    def test_kwargs(self):
        """ Test BaseModel with kwargs """
        val = self.value()
        copy = val.to_dict()
        new = BaseModel(**copy)
        self.assertEqual(new is val)

    def test_save(self):
        """ Test save method """
        val = self.value()
        val.save()
        key = self.name + '.' + val.id
        with open('file.json', mode='r', encoding='utf8') as my_file:
            obj = json.load(my_file)
            self.assertEqual(obj[key], val.to_dict())

    def test_str(self):
        """ Test __str__ method """
        val = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(
            self.name, val.id, val.to_dict()))

    def test_to_dict(self):
        """ Test to_dict method """
        val = self.value()
        obj = val.to_dict()
        self.assertEqual(val.to_dict(), obj)

    def test_uuid(self):
        """ Test uuid uniqueness """
        model = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model.id, model_2.id)

    def test_datetime_model(self):
        """ Test datetime attributes """
        model_3 = BaseModel()
        model_4 = BaseModel()
        self.assertNotEqual(model_3.created_at, model_3.updated_at)
        self.assertNotEqual(model_3.created_at, model_4.created_at)


if __name__ == '__main__':
    unittest.main()
