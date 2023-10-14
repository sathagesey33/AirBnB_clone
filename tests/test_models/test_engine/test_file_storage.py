#!/usr/bin/python3
"""
import modules
"""
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json
import uuid


class TestFileStorage(unittest.TestCase):
    """
    parent class module for test cases
    """
    def setUp(self):
        """
        set up class for test
        """
        self.storage = FileStorage()
        self.path = "file.json"

    def tearDown(self):
        """
        tear down test after it finishes
        """
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_file_path(self):
        """
        check for correct path of file
        """
        file_storage = FileStorage()
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_file_path_type(self):
        """
        check file path type
        """
        self.assertIs(type(FileStorage._FileStorage__file_path), str)

    def test_objects_type(self):
        """
        test type
        """
        self.assertIs(type(FileStorage._FileStorage__objects), dict)

    def test_objects(self):
        """
        test all instances of objects in filestorage
        """
        storage = FileStorage()
        storage._FileStorage__objects = {}
        self.assertEqual(storage._FileStorage__objects, {})
        obj = BaseModel()
        storage.new(obj)
        objects = storage.all()
        self.assertIn("BaseModel.{}".format(obj.id), objects)
        self.assertEqual(objects["BaseModel.{}".format(obj.id)], obj)

    def test_all(self):
        """
        test if all methods return a dict
        """
        storage = FileStorage()
        all_obj = storage.all()
        self.assertIsInstance(all_obj, dict)

    def test_new(self):
        """
        test if new method creates a new instance
        """
        storage = FileStorage()
        new_obj = BaseModel()
        storage.new(new_obj)
        key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        all_obj = storage.all()
        self.assertIn(key, all_obj)

    def test_save(self):
        """
        test the save method to save objects to the json file
        """
        storage = FileStorage()
        obj = BaseModel()

        storage.save()

        with open("file.json", "r") as f:
            json_string = f.read()

        self.assertIn("BaseModel.{}".format(obj.id), json_string)

    def test_reload(self):
        """
        test the reload method to load objects from json file
        """
        storage = FileStorage()
        base_model = BaseModel()
        storage.save()
        models.storage.reload()
        objects = storage._FileStorage__objects

        self.assertIn("BaseModel.{}".format(base_model.id), objects)


if __name__ == "__main__":
    unittest.main()
