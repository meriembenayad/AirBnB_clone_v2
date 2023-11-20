#!/usr/bin/python3
""" Define Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Define Review instances """
    place_id = ""
    user_id = ""
    text = ""
