"""FileStorage Model

"""
import json
from datetime import datetime
from ..person import Person

class FileStorage:

    __objects = {}
    __filepath = f"{datetime.now().date()}.json"

    def add(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def remove(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        if key in self.__objects:
            del self.__objects[key]

    def save(self):
        json_data = {}

        for key, value in self.__objects.items():
            value = value.to_dict()
            json_data[key] = value

        with open(self.__filepath, "w", encoding="utf8") as file:
            file.write(json.dumps(json_data))

    def load(self):
        json_data = {}

        try:
            with open(self.__filepath, "r", encoding="utf8") as file:
                json_data = json.loads(file.read())
        except IOError:
            pass
        else:
            for key, value in json_data.items():
                value = Person(**value)
                self.__objects[key] = value

    def all(self):
        objs = []
        for obj in self.__objects.values():
            objs.append(obj)
        return objs

    def today(self):
        objs = []
        for obj in self.__objects.values():
            tday = datetime.today()
            if obj.actual_dtime.date() == tday.date():
                objs.append(obj)
        return objs
