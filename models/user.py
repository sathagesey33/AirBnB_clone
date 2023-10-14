#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """User class represents a registered user."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
