#!/usr/bin/python3
"""
This module contains the TestUser class which inherits from TestBaseModel.
"""
import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.user import User


class TestUser(TestBaseModel):
    """
    TestUser class to test the User model.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the TestUser instance.
        """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """
        Test the first_name attribute of the User instance.
        """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """
        Test the last_name attribute of the User instance.
        """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """
        Test the email attribute of the User instance.
        """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """
        Test the password attribute of the User instance.
        """
        new = self.value()
        self.assertEqual(type(new.password), str)


if __name__ == '__main__':
    unittest.main()
