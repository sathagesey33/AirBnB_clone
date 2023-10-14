#!/usr/bin/python3
"""
    class city
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class represents a city within a state."""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
