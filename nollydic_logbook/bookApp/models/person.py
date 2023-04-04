"""Person Model

"""
from uuid import uuid4
import models
from datetime import datetime


class Person:

    name = ""
    actual_dtime = None
    input_dtime = None
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
        attrs["actual_dtime"] = datetime.isoformat(attrs["actual_dtime"])
        attrs["input_dtime"] = datetime.isoformat(attrs["input_dtime"])
        return attrs

    def update(self, **kwargs):
        if "id" in kwargs:
            self.__dict__.update({'id': kwargs["id"]})
        if "name" in kwargs:
            self.__dict__.update({"name": kwargs["name"]})
        if "actual_dtime" in kwargs:
            self.__dict__.update({"actual_dtime": datetime.fromisoformat(kwargs["actual_dtime"])})
        if "input_dtime" in kwargs:
            self.__dict__.update({"input_dtime": datetime.fromisoformat(kwargs["input_dtime"])})
        if "role" in kwargs:
            self.__dict__.update({"role": kwargs["role"]})
        if "role_info" in kwargs:
            self.__dict__.update({"role_info": kwargs["role_info"]})
        if "phone" in kwargs:
            self.__dict__.update({"phone": kwargs["phone"]})

    def save(self):
        models.storage.load()
        models.storage.save()
