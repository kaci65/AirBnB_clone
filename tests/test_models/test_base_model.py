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

    def test_to_dict(self):
        """
        Test that to_dict() returns a dictionary containing all
        keys/values of __dict__
        """
        b1 = BaseModel()
        self.assertIsNotNone(b1.to_dict())
        self.assertTrue(type(b1.created_at), str)
        self.assertTrue(type(b1.updated_at), str)
        self.assertEqual(type(b1.to_dict()), dict)
        self.assertNotEqual(b1.to_dict().get('id'), None)
        self.assertNotEqual(b1.to_dict().get('created_at'), None)
        self.assertNotEqual(b1.to_dict().get('updated_at'), None)
        self.assertEqual(b1.to_dict().get('__class__'), 'BaseModel')
