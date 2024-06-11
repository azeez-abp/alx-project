#!/usr/bin/python
""" holds class City"""
from app.models.schemas.base import BaseModel
from app.models.storage_engine.db import Base
from app.models.storage_engine import storage
from sqlalchemy import Column, String, ForeignKey, Integer  # type: ignore


class Addresses(BaseModel, Base):
    """Representation of an address"""

    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    user_id = Column(String(60), ForeignKey("users_account.user_id"), nullable=False)
    street = Column(String(128), nullable=False)
    city = Column(String(128), nullable=False)
    state = Column(String(128), nullable=False)
    zip_code = Column(String(20), nullable=False)

    def __init__(self, **kw):
        """initializes city"""
        super().__init__(**kw)


Base.metadata.create_all(storage.get_engine())
