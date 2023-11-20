#!/usr/bin/python3
""" Unitest test console """
import unittest
from unittest.mock import patch
from io import StringIO
import console
import pycodestyle
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    """ Test HBNBCommand class """

    def setUp(self):
        """Set up test cases"""
        self.cli = console.HBNBCommand()
        self.storage = FileStorage()
        self.storage.reload()
        self.storage._FileStorage__objects = {}

    def test_pycodestyle(self):
        """Test that the code conforms to pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_quit_command(self):
        """Test the quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('quit')
            output = f.getvalue().strip()
            self.assertEqual(output, '')


if __name__ == '__main__':
    unittest.main()
