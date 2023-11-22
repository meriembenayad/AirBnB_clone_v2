#!/usr/bin/python3
"""Module for test Amenity class"""
import unittest
from models.amenity import Amenity
from tests.test_models.test_base_model import TestBaseModel


class TestAmenity(TestBaseModel):
    """
    The test_Amenity class is used to test the functionality of the Amenity class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the test_Amenity instance.
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """
        Test if the 'name' attribute of an Amenity instance is a string.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()
