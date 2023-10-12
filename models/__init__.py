#!/usr/bin/python3
"""
models/__init__.py
This module initializes the FileStorage instance for the application.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
