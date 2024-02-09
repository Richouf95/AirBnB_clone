#!/usr/bin/python3
"""
    This module serializes instances to a JSON file
    and deserializes JSON file to instances
"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
        Class that serializes and instances JSON
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
             returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id
        """
        objectClassName = obj.__class__.__name__
        objectInstanceId = obj.id
        newObjectAttribute = "{}.{}".format(objectClassName, objectInstanceId)

        FileStorage.__objects[newObjectAttribute] = obj

    def save(self):
        """
            serializes __objects to the JSON file
        """
        dictionary = {}
        for x in FileStorage.__objects.keys():
            dictionary = {
                    **dictionary,
                    x: FileStorage.__objects[x].to_dict()
                    }
        with open(FileStorage.__file_path, "w") as fic:
            json.dump(dictionary, fic)

    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        if os.path.exists("./{}".format(FileStorage.__file_path)):
            with open(FileStorage.__file_path) as fic:
                dictionary = json.load(fic)
                for x in dictionary.values():
                    className = eval(x["__class__"])
                    self.new(className(**x))
