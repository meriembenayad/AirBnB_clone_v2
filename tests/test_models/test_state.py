#!/usr/bin/python3
"""Module for test State class"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test State class implementation"""

    def test_class(self):
        """Validate the types of the attributes an class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(State, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(State.name, str)


if __name__ == '__main__':
    unittest.main()
