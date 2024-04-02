#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user/passwrd"""
        if kwargs:
            passwrd = kwargs.pop("password", None)
            User.__set_pass(self, passwrd)
        super().__init__(*args, **kwargs)

    def __set_pass(self, passwd):
        """md5 """
        passwrdcach = md5(passwd.encode('utf-8')).hexdigest()
        setattr(self, "password", passwrdcach)
<<<<<<< HEAD
        
=======
>>>>>>> 9017e9a6f531ce8ca3950da589f11238636a5b97
