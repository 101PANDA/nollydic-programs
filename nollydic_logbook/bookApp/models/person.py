"""Person Model

"""
from uuid import uuid4
import models
from datetime import datetime


class Person:

    name = ""
    datetime = None
    role = ""
    role_info = ""
    phone = ""

    def __init__(self, **kwargs):
        if kwargs:
            self.update(**kwargs)
        else:
            self.id = str(uuid4())
            models.storage.add(self)

    def to_dict(self):
        attrs = self.__dict__.copy()
        attrs["datetime"] = datetime.isoformat(attrs["datetime"])
        return attrs

    def update(self, **kwargs):
        if "id" in kwargs:
            self.__dict__.update({'id': kwargs["id"]})
        if "name" in kwargs:
            self.__dict__.update({"name": kwargs["name"]})
        if "datetime" in kwargs:
            self.__dict__.update({"datetime": datetime.fromisoformat(kwargs["datetime"])})
        if "role" in kwargs:
            self.__dict__.update({"role": kwargs["role"]})
        if "department" in kwargs:
            self.__dict__.update({"role_info": kwargs["role_info"]})
        if "phone" in kwargs:
            self.__dict__.update({"phone": kwargs["phone"]})

        models.storage.save()
