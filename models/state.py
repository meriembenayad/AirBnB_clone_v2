#!/usr/bin/python3
""" Define state class """
from models.base_model import BaseModel


class State(BaseModel):
    """ Define State instance """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize State instances """
        super().__init__(*args, **kwargs)
