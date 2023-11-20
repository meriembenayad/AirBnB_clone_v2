#!/usr/bin/python3
"""Module for test BaseModel class"""
import unittest
from datetime import datetime
import json
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test for BaseModel class """

    def test_first_task(self):
        """Test creation of class and to_dict"""
        my_model = BaseModel()
        self.assertIs(type(my_model), BaseModel)
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)
        model_types_json = {
            "my_number": int,
            "name": str,
            "__class__": str,
            "updated_at": str,
            "id": str,
            "created_at": str
        }
        my_model_json = my_model.to_dict()
        for key, value in model_types_json.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, my_model_json)
                self.assertIs(type(my_model_json[key]), value)

    def test_init(self):
        """ Test __init__ method of the BaseModel class """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_base_types(self):
        """Testing dict model"""
        second_model = BaseModel()
        self.assertIs(type(second_model), BaseModel)
        second_model.name = "Mira"
        second_model.my_number = 80
        self.assertEqual(second_model.name, "Mira")
        self.assertEqual(second_model.my_number, 80)
        model_types = {
            "my_number": int,
            "name": str,
            "updated_at": datetime,
            "id": str,
            "created_at": datetime
        }
        for key, value in model_types.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, second_model.__dict__)
                self.assertIs(type(second_model.__dict__[key]), value)

    def test_uuid(self):
        """ testing differents uuid """
        model = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model.id, model_2.id)

    def test_datetime_model(self):
        """testing datetime base model"""
        model_3 = BaseModel()
        model_4 = BaseModel()
        self.assertNotEqual(model_3.created_at, model_3.updated_at)
        self.assertNotEqual(model_3.created_at, model_4.created_at)

    def test_string_representation(self):
        """Test the magic method str"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        id_model = my_model.id

        expected = '[BaseModel] ({}) {}'\
                   .format(id_model, my_model.__dict__)
        self.assertEqual(str(my_model), expected)

    def test_constructor_kwargs(self):
        """Test constructor that has kwargs as attributes values"""
        obj = BaseModel()
        obj.name = "My First Model"
        obj.my_number = 89
        json_attributes = obj.to_dict()

        obj2 = BaseModel(**json_attributes)

        self.assertIsInstance(obj2, BaseModel)
        self.assertIsInstance(json_attributes, dict)
        self.assertIsNot(obj, obj2)

    def test_file_save(self):
        """Test that info is saved to file"""
        b3 = BaseModel()
        b3.save()
        with open("file.json", 'r') as f:
            self.assertIn(b3.id, f.read())


if __name__ == '__main__':
    unittest.main()
