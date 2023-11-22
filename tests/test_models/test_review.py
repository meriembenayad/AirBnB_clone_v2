#!/usr/bin/python3
"""Module for test Review class"""
import unittest
from models.review import Review
from tests.test_models.test_base_model import TestBaseModel


class TestReview(TestBaseModel):
    """Test Review class implementation"""

    def setUp(self):
        """
        Sets up the initial instance of review before each test
        """
        self.value = Review()
        self.name = "Review"

    def test_place_id(self):
        """
        Test the place_id attribute type
        """
        self.assertEqual(type(self.value.place_id), str)

    def test_user_id(self):
        """
        Test the user_id attribute type
        """
        self.assertEqual(type(self.value.user_id), str)

    def test_text(self):
        """
        Test the text attribute type
        """
        self.assertEqual(type(self.value.text), str)


if __name__ == '__main__':
    unittest.main()
