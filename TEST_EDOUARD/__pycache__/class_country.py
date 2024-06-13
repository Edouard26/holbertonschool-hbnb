from base_model import basemodel
from datetime import datetime
import uuid

class Country(basemodel):
    def __init__(self, name, country_code, created_at=None, updated_at=None):
        # Générer un UUID pour le pays
        unique_id = str(uuid.uuid4())
        # Si created_at ou updated_at ne sont pas fournis, utilisez la date actuelle
        created_at = created_at or datetime.now()
        updated_at = updated_at or datetime.now()
        super().__init__(unique_id, name, created_at, updated_at)
        self.country_code = country_code

    def __repr__(self):
        return f"Country(name={self.name}, country_code={self.country_code})"
