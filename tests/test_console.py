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

    def test_do_create_command(self):
        """ Test do_create command """
        with patch('sys.stdout', new=StringIO()) as fc:
            # Test with no arguments
            self.cli.onecmd('create')
            output = fc.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

            # Test with invalid class
            self.cli.onecmd('create MyClass')
            output = fc.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

            # Test with valid class and parameters
            self.cli.onecmd('create BaseModel name="John" age=23')
            output = fc.getvalue().strip()
            self.assertEqual(output)

            # Test if instance is created and attribute are set
            instance = self.cli.storage.all()['BaseModel.' + output]
            self.assertEqual(instance.name, 'John')
            self.assertEqual(instance.age, 23)


if __name__ == '__main__':
    unittest.main()
