#!/usr/bin/python3
"""Module for test City class"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test City class implementation"""

    def test_class(self):
        """Validate the types of the attributes an class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(City, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(City.name, str)
            self.assertIsInstance(City.state_id, str)


if __name__ == '__main__':
    unittest.main()
