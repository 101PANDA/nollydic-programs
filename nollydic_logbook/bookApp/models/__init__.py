"""Initialization

"""

from .storages.file_storage import FileStorage

storage = FileStorage()

storage.load()