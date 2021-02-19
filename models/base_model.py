#!/usr/bin/python3
"""
Base class module for AirBnB project which all othe clases will inherit from
"""


import uuid
from datetime import datetime
import models


class BaseModel():
    """Defines all common attributes/methods fo other classes"""
    def __init__(self, *args, **kwargs):
        """initialize class BaseModel"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key in kwargs:
                if key == "created_at":
                    kwargs["created_at"] = datetime.strptime(
                            kwargs["created_at"], time_format)
                if key == "updated_at":
                    kwargs["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], time_format)
                self.__dict__[key] = kwargs[key]

    def __str__(self):
        """prints dictionary of attributes"""
        return "[{}], ({}), {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates public instance attribute updated_at with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        new_dict = {}
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        if "created_at" in new_dict:
            new_dict["created_at"] = self.created_at.isoformat()
        if "updated_at" in new_dict:
            new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
