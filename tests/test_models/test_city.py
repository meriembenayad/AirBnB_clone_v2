#!/usr/bin/python3
"""Module for test City class"""
import unittest
from models.city import City
from tests.test_models.test_base_model import TestBaseModel


class TestCity(TestBaseModel):
    """Test City class implementation"""

    def __init__(self, *args, **kwargs):
        """
        Initializes the test case for City.
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Tests the state_id attribute of the City class.
        """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """
        Tests the name attribute of the City class.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()
