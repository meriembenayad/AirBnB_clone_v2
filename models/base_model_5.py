#!usr/bin/python3
""" Import uuid & datetime modules """
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Define a BaseModel class """

    def __init__(self, *args, **kwargs):
        """
        Initilize a new instance of BaseModel class
        Args:
            args (tuple): Unused argument
            kwargs (dict):
        """
        self.id = str(uuid4())
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                    continue
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        String representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Method to update the 'updated_at' attribute to the current time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Method to return a dictionary representation of the BaseModel instance
        """
        dictionary = dict(self.__dict__).copy()
        dictionary['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            dictionary[key] = value
            if key == 'created_at' or key == 'updated_at':
                dictionary[key] = value.isoformat()
        return dictionary
