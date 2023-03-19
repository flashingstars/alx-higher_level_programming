#!/usr/bin/python3

""" sql alchemy """
from sqlalchemy import create_engine, Sequence, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class State(Base):
    """ State object """
    __tablename__ = 'states'
    id = Column(
        Integer,
        Sequence('my_sequence'),
        primary_key=True,
        nullable=False
        )
    name = Column(String(128), nullable=False)
