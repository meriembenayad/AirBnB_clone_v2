#!/usr/bin/python3
""" IMPORT MODULES """
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        """
            INITIALIZE THE INSTANCES ATTRIBUTES
            ARGS:
                *args (tuple): UNUSED
                **kwargs (dictionary): keywords arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
            Method returns string represention of the instance
            including class name, id, and other attributes
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Method updates the 'updated_at' attribute to current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            Method returns a dictionary representation of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = dict_copy['created_at'].isoformat()
        dict_copy['updated_at'] = dict_copy['updated_at'].isoformat()
        return dict_copy
