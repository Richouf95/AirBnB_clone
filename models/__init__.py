#!/usr/bin/python3
"""
    Init the model modul
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
