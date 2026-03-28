from src.exceptions import InvalidDescriptionError


class DescriptionDescriptor:
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        if not isinstance(value, str) or len(value) == 0:
            raise InvalidDescriptionError
        obj.__dict__[self.name] = value