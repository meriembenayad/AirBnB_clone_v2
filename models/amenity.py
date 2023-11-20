#!/usr/bin/python3
""" Define Amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ class attributes """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize class instances """
        super().__init__(*args, **kwargs)
