#!/usr/bin/python3

"""
This is to mark directories as Python package directories
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
