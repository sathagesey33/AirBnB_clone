#!/usr/bin/python3
"""
import modules
"""

from models.base_model import BaseModel
import unittest
from datetime import datetime
from uuid import UUID
import uuid


class TestBaseModel(unittest.TestCase):
    """
    parent class module to test for various instances
    of class basemodel
    """
    def test_id_length(self):
        """
        test length
        """
        obj = BaseModel()
        self.assertEqual(len(obj.id), 36)

    def test_id_type(self):
        """
        test type
        """
        obj = BaseModel()
        self.assertIs(type(obj.id), str)

    def test_created_at_type(self):
        """
        test type
        """
        obj = BaseModel()
        self.assertIs(type(obj.created_at), datetime)

    def test_updated_at_type(self):
        """
        test type
        """
        obj = BaseModel()
        self.assertIs(type(obj.updated_at), datetime)

    def test_to_dict_type(self):
        """
        test type
        """
        obj = BaseModel()
        to_dict_dict = obj.to_dict()
        self.assertIn("__class__", to_dict_dict)
        self.assertIs(type(to_dict_dict["__class__"]), str)

    def test_dict_type(self):
        """
        test dict type
        """
        obj = BaseModel()
        to_dict_dict = obj.to_dict()
        self.assertIs(type(to_dict_dict["id"]), str)

    def test_uuid_version(self):
        """
        check uuid version
        """
        obj = BaseModel()
        to_uuid = uuid.UUID(obj.id)
        self.assertEqual(to_uuid.version, 4)

    def test_for_valid_id(self):
        """
        check if id is valid or not
        """
        obj = BaseModel()
        value = UUID(obj.id)
        self.assertIs(type(value), UUID)

    def test_valid_to_dict(self):
        """
        check valid instances of dictionary type
        """
        obj = BaseModel()
        to_dict_dict = obj.to_dict()
        created_at = datetime.fromisoformat(to_dict_dict["created_at"])
        updated_at = datetime.fromisoformat(to_dict_dict["updated_at"])

        self.assertEqual(to_dict_dict["updated_at"], updated_at.isoformat())
        self.assertEqual(to_dict_dict["created_at"], created_at.isoformat())
        self.assertIs(type(to_dict_dict["updated_at"]), str)
        self.assertIs(type(to_dict_dict["created_at"]), str)
        self.assertIn("updated_at", to_dict_dict)
        self.assertIn("created_at", to_dict_dict)


if __name__ == "__main__":
    unittest.main()
