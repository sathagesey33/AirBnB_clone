#!/usr/bin/python3
"""
    class state
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class represents a geographical state."""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
