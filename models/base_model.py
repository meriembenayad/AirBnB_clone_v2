#!usr/bin/python3
""" Import uuid & datetime modules """
from uuid import uuid4
from datetime import datetime
import models

from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from hashlib import md5

Base = declarative_base()


class BaseModel:
    """ Define a BaseModel class """
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

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

    def __str__(self):
        """
        String representation of the BaseModel instance.
        """
        dict_copy = self.to_dict()
        dict_copy.pop('__class__', None)
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, dict_copy)

    def save(self):
        """
        Method to update the 'updated_at' attribute to the current time
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
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
                dictionary[key] = value
        dictionary.pop('_sa_instance_state', None)
        return dictionary

    def delete(self):
        """
            Delete the current instance from storage
        """
        models.storage.delete(self)

    def hash_password(self):
        """
        Method to hash the password using SHA-256
        """
        if self.password:
            # Create a hash object using MD5
            md5 = hashlib.md5()
            # Update the hash object with the password
            md5.update(self.password.encode('utf-8'))
            # Get the hexadecimal representation of the hash
            hashed_password = md5.hexdigest()
            # Update the instance's password with the hashed password
            self.password = hashed_password
