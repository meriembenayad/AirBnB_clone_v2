#!/usr/bin/python3
""" Import modules """
import uuid
from datetime import datetime


class BaseModel:
    """ class BaseModel """

    def __init__(self):
        """ Instanciate the instance attribues """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """ String representation """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Update updated date """
        self.updated_at = datetime.now()

    def to_dict(self):
        """  """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = dict_copy['created_at'].isoformat()
        dict_copy['updated_at'] = dict_copy['updated_at'].isoformat()
        return dict_copy
