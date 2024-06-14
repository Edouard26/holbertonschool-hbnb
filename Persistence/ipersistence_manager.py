from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    @abstractmethod
    def save(self, entity):
        """Saves an entity to the storage."""
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        """Retrieves an entity from the storage by its ID and type."""
        pass

    @abstractmethod
    def update(self, entity):
        """Updates an existing entity in the storage."""
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        """Deletes an entity from the storage by its ID and type."""
        pass