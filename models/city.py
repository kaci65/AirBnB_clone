#!/usr/bin/python3
"""City module"""
import models
from models.base_model import BaseModel


class City(BaseModel):
    """city class inheriting from BaseModel"""
    state_id = ""
    name = ""
