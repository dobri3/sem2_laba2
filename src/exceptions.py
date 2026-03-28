class InvalidPriorityError(ValueError):

    def __init__(self, message="приоритет может быть только 1, 2 или 3"):
        super().__init__(message)

class InvalidStatusError(ValueError):
    def __init__(self, message="статус может быть только 'in_proccess', 'new' или 'done'"):
        super().__init__(message)

class InvalidDescriptionError(ValueError):
    def __init__(self, message="описание может быть только непустой строкой"):
        super().__init__(message)
