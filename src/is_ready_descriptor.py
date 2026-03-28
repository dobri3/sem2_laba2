class IsReadyDescriptor:

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.status in ["new", "in_progress"]
