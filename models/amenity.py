#!/usr/bin/python3
"""
    class amenity
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class represents a feature or service offered."""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
