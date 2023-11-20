#!/usr/bin/python3
""" Define class City """
from models.base_model import BaseModel


class City(BaseModel):
    """ class attributes """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize City instances """
        super().__init__(*args, **kwargs)
