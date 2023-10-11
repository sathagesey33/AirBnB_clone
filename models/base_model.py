#!/usr/bin/python3
"""
    a class BaseModel
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    a base class for common methods.
    """
    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        Updates the 'updated_at' attribute with the current date.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys of __dict__ of the instance.
        """
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
