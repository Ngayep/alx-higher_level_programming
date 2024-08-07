#!/usr/bin/python3

"""
 contains the class definition of a State
 and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """state class
    __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True,  primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
