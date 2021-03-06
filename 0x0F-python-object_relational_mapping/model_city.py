#!/usr/bin/python3
"""Model City"""
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from model_state import Base, State


class City(Base):
    """ class cyty """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
