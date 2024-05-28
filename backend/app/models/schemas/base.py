#!/usr/bin/python3
"""
Contains class BaseModel
"""
from datetime import datetime
from sqlalchemy import Column, String, DateTime  # type: ignore
import uuid
from app.models.storage_engine import storage
time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """The BaseModel class from which future classes will be derived"""

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, **kward):
        """Initialization of the base model"""
        print(kward, "ANOTHER")
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        for key, value in kward.items():
            if key != "__class__":
                setattr(self, key, value)

    def __str__(self) -> str:
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    @classmethod
    def add(cls: object, users: list) -> list:
        """method for adding objetc to table"""
        storage.get_instance().add_all(users)
        storage.get_instance().commit()
        return users

    # def delete(self):
    #     """delete the current instance from the storage"""
    #     storage.delete(self)
