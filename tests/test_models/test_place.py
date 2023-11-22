#!/usr/bin/python3
"""Module for test Place class"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(TestBaseModel):
    """Test for Place model"""

    def setUp(self):
        """Set up test variables."""
        self.model = Place()
        self.model_name = "Place"

    def test_city_id(self):
        """Test that city_id is a string."""
        self.assertEqual(type(self.model.city_id), str)

    def test_user_id(self):
        """Test that user_id is a string."""
        self.assertEqual(type(self.model.user_id), str)

    def test_name(self):
        """Test that name is a string."""
        self.assertEqual(type(self.model.name), str)

    def test_description(self):
        """Test that description is a string."""
        self.assertEqual(type(self.model.description), str)

    def test_number_rooms(self):
        """Test that number_rooms is an integer."""
        self.assertEqual(type(self.model.number_rooms), int)

    def test_number_bathrooms(self):
        """Test that number_bathrooms is an integer."""
        self.assertEqual(type(self.model.number_bathrooms), int)

    def test_max_guest(self):
        """Test that max_guest is an integer."""
        self.assertEqual(type(self.model.max_guest), int)

    def test_price_by_night(self):
        """Test that price_by_night is an integer."""
        self.assertEqual(type(self.model.price_by_night), int)

    def test_latitude(self):
        """Test that latitude is a float."""
        self.assertEqual(type(self.model.latitude), float)

    def test_longitude(self):
        """Test that longitude is a float."""
        self.assertEqual(type(self.model.longitude), float)

    def test_amenity_ids(self):
        """Test that amenity_ids is a list."""
        self.assertEqual(type(self.model.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
