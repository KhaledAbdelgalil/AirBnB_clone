#!/usr/bin/python3
"""
Module: file_storage.py

Defines the FileStorage class for managing
serialization and deserialization of objects.
"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    __nameToClass = {"BaseModel": BaseModel, "User": User, "State":State,
                      "City": City, "Amenity":Amenity, "Place":Place, "Review": Review}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        try:
            saved_dic = {}
            for key, object in self.all().items():
                saved_dic[key] = object.to_dict()

            with open(self.__file_path, "w") as write_file:
                json.dump(saved_dic, write_file)
        except Exception:
            return

    def reload(self):
        read_dic = {}
        try:
            with open(self.__file_path, "r") as read_file:
                read_dic = json.load(read_file)
        except Exception:
            return
        # key(class name.id) ==> object dict
        for key, object_dic in read_dic.items():
            if object_dic["__class__"] in self.__nameToClass:
                obj = self.__nameToClass[object_dic["__class__"]](**object_dic)
                self.__objects[key] = obj
