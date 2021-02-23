#!/usr/bin/python3
"""Test module for the BaseModel class"""
import unittest
from from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """class with test functions for BaseModel"""
    def test_BaseModel(self):
        """BaseModel initialization"""
        b1 = BaseModel()
        self.assertIs(type(b1), BaseModel)

    def test_attributes(self):
        '''check attr'''
        self.assertTrue(hasattr(self.basemodel, "created_at"))
        self.assertTrue(hasattr(self.basemodel, "id"))
        self.basemodel.save()
        self.assertTrue(hasattr(self.basemodel, "updated_at"))

    def test_str(self):
        '''Test that __str__ prints dictionary of attributes'''
        aux = "[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id, self.__dict__)
        self.assertEqual(print(self.basemodel), print(aux))
