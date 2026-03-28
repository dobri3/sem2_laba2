from datetime import datetime
import uuid

from src.description_descriptor import DescriptionDescriptor
from src.is_ready_descriptor import IsReadyDescriptor
from src.priority_descriptor import PriorityDescriptor
from src.status_descriptor import StatusDescriptor


class Task:
    description = DescriptionDescriptor()
    priority = PriorityDescriptor()
    status = StatusDescriptor()
    is_ready = IsReadyDescriptor()

    def __init__(self, description, priority, status):
        self._id = str(uuid.uuid4())
        self.description = description
        self.priority = priority
        self.status = status
        self._created_at = datetime.now()
    
    @property
    def id(self):
        return self._id
    
    @property
    def created_at(self):
        return self._created_at
    