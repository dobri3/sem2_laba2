from src.constants import PRIORITY_VALUES
from src.exceptions import InvalidPriorityError


class PriorityDescriptor:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if value not in PRIORITY_VALUES:
            raise InvalidPriorityError
        obj.__dict__[self.name] = value
