#!/usr/bin/python3
""" Define DBStorage class """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class DBStorage:
    """ Private attributes """
    __engine = None
    __session = None

    def __init__(self):
        """ Initilize a new instance of DBStorage class """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True
        )

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """  """
        all_classes = {
            "State": State,
            "City": City,
            "User": User,
        }
        new_dict = {}

        if cls is None:
            for class_name, class_obj in all_classes.items():
                objs = self.__session.query(class_obj).all()
                for obj in objs:
                    key = "{}.{}".format(class_name, obj.id)
                    new_dict[key] = obj
        elif cls in all_classes:
            objs = self.__session.query(all_classes[cls]).all()
            for obj in objs:
                key = "{}.{}".format(cls, obj.id)
                new_dict[key] = obj
        else:
            print("** class doesn't exist **")

        return new_dict

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database and the current database session """
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fact)
        self.__session = Session()