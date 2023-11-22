#!/usr/bin/python3
""" Tests for class fileStorage """
import unittest
from os import remove
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage

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
        """ Set up test environment """
        keys = list(storage._FileStorage__objects.keys())
        for key in keys:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            remove('file.json')
        except FileNotFoundError:
            pass

    def test_obj_list_empty(self):
        """ Test if __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ Test if new object is correctly added to __objects """
        new = BaseModel()
        self.assertIn(new, storage.all().values())

    def test_all(self):
        """ Test if __objects is properly returned """
        new = BaseModel()
        self.assertIsInstance(storage.all(), dict)

    def test_base_model_instantiation(self):
        """ Test if file is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Test if data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ Test FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Test if storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Test load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Test if nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ Test if BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Test if __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Test if __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Test if key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ Test if FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(storage), FileStorage)

if __name__ == '__main__':
    unittest.main()
