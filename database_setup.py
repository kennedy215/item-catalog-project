# -*- coding: utf-8 -*-
import sys
import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()
# reference sqlalchemy create engine

class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer,primary_key=True)
    name = Column(String(150),nullable=False)

@property
def serialize(self):
    return {
        'name': self.name,
        'id': self.id,
    }

class Fighter(Base):
    __tablename__ = 'fighter'

    id = Column(Integer,primary_key=True)
    name = Column(String(150),nullable=False)
    description = Column(String(1000))
    style = Column(String(300))
    country_id = Column(Integer, ForeignKey('country.id'))
    country = relationship(Country)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'style': self.style,
        }

engine = create_engine('sqlite:///tournament.db')
Base.metadata.create_all(engine)



print "database works"
