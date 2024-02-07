#!/usr/bin/python3
"""
    This module content the Base model
"""


from uuid import uuid4
from datetime import datetime


class BaseModel():
    """
        This is the Base Model Class
    """
    def __init__(self):
        """
            Initializing an instance
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
            Updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            Make a dictionary representation of a class
        """
        dict_format = {
                **self.__dict__,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat(),
                "__class__": self.__class__.__name__
                }
        return dict_format

    def __str__(self):
        """
            String representation of the class
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)
