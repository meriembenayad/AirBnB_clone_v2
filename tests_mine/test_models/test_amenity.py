#!/usr/bin/python3
"""Module for test Amenity class"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test State class implementation"""

    def test_class(self):
        """Validate the types of the attributes an class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Amenity, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Amenity.name, str)


if __name__ == '__main__':
    unittest.main()
