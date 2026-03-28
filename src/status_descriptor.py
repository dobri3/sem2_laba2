from src.constants import STATUS_VALUES
from src.exceptions import InvalidStatusError


class StatusDescriptor:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if value not in STATUS_VALUES:
            raise InvalidStatusError
        obj.__dict__[self.name] = value
