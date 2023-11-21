#!/usr/bin/python3
""" Define class City """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ class attributes """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    places = relationship("Places", backref="cities", cascade="all, delete")

    def __init__(self, *args, **kwargs):
        """ Initialize City instances """
        super().__init__(*args, **kwargs)
