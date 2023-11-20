#!/usr/bin/python3
""" Import unique FileStorage instance """
from models.engine.file_storage import FileStorage

""" an instance of FileStorage """
storage = FileStorage()
storage.reload()
