from uuid import uuid4
from base_model import basemodel

class city(basemodel):
    def __init__(self, name, country_code, created_at=None, updated_at=None):
        super().__init__(uuid4(), name, created_at, updated_at)
        self.country_code = country_code
    
    def __repr__(self):
        return f"city(name={self.name}, country_code={self.country_code})"
    
    def save(self):
        print(f"Saving {self.name} with ID {self.uuid4}")

    def delete(self):
        print(f"Deleting {self.name} with ID {self.uuid4}")
