#!/usr/bin/python3
"""
This module contains the TestState class which inherits from TestBaseModel.
"""
import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.state import State


class TestState(TestBaseModel):
    """
    TestState class to test the State model.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the TestState instance.
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """
        Test the name attribute of the State instance.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()
