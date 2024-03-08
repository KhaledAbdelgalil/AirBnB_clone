#!/usr/bin/python3
"""
Module: file_storage.py

Defines the FileStorage class for managing serialization and deserialization of objects.
"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    
    """NOT COMPLETE msh fahma haga mn ely b3mlo paste :D"""
