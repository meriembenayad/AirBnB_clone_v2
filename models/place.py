#!/usr/bin/python3
""" Define class Place """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os

if os.getenv('HBNB_TYPE_STORAGE') == "db":
    place_amenity = Table(
        'place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id')),
        Column('amenity_id', String(60), ForeignKey('amenities.id'))
    )


class Place(BaseModel, Base):
    """ class attributes """
    __tablename__ = 'places'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        reviews = relationship('Review', backref='place',
                               cascade="all, delete")
        amenity_ids = relationship(
            'Amenity', secondary='place_amenity', back_populates='place_amenities', viewonly=False)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """
                Getter attribute reviews that returns the list of Review instances
                with place_id equals to the current Place.id
            """
            from models import storage
            return [review for review in storage.all(Review).values() if review.place_id == self.id]
