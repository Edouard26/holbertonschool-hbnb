#!/user/bin/python3
from uuid import uuid4
from datetime import datetime, timezone

class BaseModel:
    
    def __init__(self, uuid4, name, created_at, updated_at):
        self.uuid4 = uuid4
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at

        def save(self):
            print(f"Saving {self.name} with ID {self.id}")

        def delete(self):
            print(f"Deleting {self.name} with ID {self.id}")
class ModelBase:
    created_at = None
    updated_at = None