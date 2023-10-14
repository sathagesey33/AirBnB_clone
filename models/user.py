#!/usr/bin/python3
<<<<<<< HEAD
"""
    class user
"""
=======
>>>>>>> bdde5e882fb19143e4dfab580f9b465c666e80dc

from models.base_model import BaseModel


class User(BaseModel):
    """User class represents a registered user."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

<<<<<<< HEAD
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
=======
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
>>>>>>> bdde5e882fb19143e4dfab580f9b465c666e80dc
