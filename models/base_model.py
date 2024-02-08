#!/usr/bin/python3
"""
    This module content the Base model
"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """
        This is the Base Model Class
    """
    def __init__(self, *args, **kwargs):
        """
            Initializing an instance
        """
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(
                            v, "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "__class__":
                    pass
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
            Updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

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
