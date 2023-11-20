#!/usr/bin/python3
""" Tests for class fileStorage """
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """ Sets up the class test """
        self.base = BaseModel()
        self.amen = Amenity()
        self.cit = City()
        self.pla = Place()
        self.rev = Review()
        self.sta = State()
        self.use = User()
        self.fs = FileStorage("file.json")
        self.storage = FileStorage()
        self.storage.save()

    def tearDown(self):
        """ Tears down the testing environment """
        del self.base
        del self.amen
        del self.cit
        del self.pla
        del self.rev
        del self.sta
        del self.use
        del self.storage
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """ test all method """
        obj = self.storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, self.storage._FileStorage__objects)

    def test_storage_empty(self):
        """ Test storage not empty """
        self.assertIsNotNone(self.storage.all())

    def test_storage_all_type(self):
        """ Test type storage """
        self.assertEqual(dict, type(self.storage.all()))

    def test_new(self):
        """Test the new method"""
        my_model = BaseModel()
        self.storage.new(my_model)
        key = f"BaseModel.{my_model.id}"
        all_objs = self.storage.all()
        self.assertIn(key, all_objs.keys())
        self.assertEqual(all_objs[key], my_model)

    def test_check_json_loading(self):
        """ Test load of json file """
        with open("file.json") as my_file:
            dic = json.load(my_file)
            self.assertEqual(isinstance(dic, dict), True)

    def test_file_existence(self):
        """
            Test working of Storage Engine's methods
        """
        with open("file.json") as my_file:
            self.assertTrue(len(my_file.read()) > 0)

    def test_save(self):
        """ Test save() method """
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        with open(self.file_path, 'r') as my_file:
            content = my_file.read()
            key = f"BaseModel.{my_model.id}"
            self.assertIn(key, content)

    def test_reload(self):
        """ Test reload() """
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        key = f"BaseModel.{my_model.id}"
        self.assertIn(key, all_objs.keys())


if __name__ == '__main__':
    unittest.main()
