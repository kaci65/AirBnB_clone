#!/usr/bin/python3
"""
class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json
import models


class FileStorage():
    """Define and initialize class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dict = {}
        with open(self.__file_path, mode="w") as fd:
            for key, value in self.__objects.items():
                dict[key] = value.to_dict()
            json.dump(dict, fd)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        path = self.__file_path
        try:
            with open(path, mode="r") as fd:
                # complete code
        except:
            pass
