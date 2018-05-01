# -*- coding: utf-8 -*-
import sys
import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()
# reference sqlalchemy create engine

class Gym(Base):
    __tablename__ = 'gym'

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
    country = Column(String(100)) 
    gym_id = Column(Integer, ForeignKey('gym.id'))
    gym = relationship(Gym)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'style': self.style,
            'country': self.country,
        }

engine = create_engine('sqlite:///tournament.db')
Base.metadata.create_all(engine)



print "database works"
