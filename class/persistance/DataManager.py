import json
import datetime
import uuid
from .IPersistenceManager import IPersistenceManager

class DataManager(IPersistenceManager):

    def __init__(self):
        for attr_name in ['cloud_database', 'cloud_entity_class', 'cloud_primary_key']:
            attr_value = getattr(self, attr_name, None)
            if not attr_value:
                raise Exception(
                    "[{} # DataManager # Error] {} not defined.".format(
                        self.cloud_entity_class.__name__ if self.cloud_entity_class != None else "None",
                        attr_name
                    )
                )

    def save(self, entity: dict):
        """
        Logic to save entity to storage.
        Arguments:
            entity (dict): Data of the entity to save.
        Return:
            Entity in the "database" saved.
        """
        entity['id'] = str(uuid.uuid4())
        with open(self.cloud_PATH, 'r', encoding="utf-8") as file:
            datas: dict = json.load(file)
            entity_id = entity.get(self.cloud_primary_key, None)

            entity_attrs = {attr: typ for attr, typ in self.cloud_entity_class.__annotations__.items()}
            keys1 = set(entity_attrs.keys())
            keys2 = set(entity.keys())
            if keys1 != keys2:
                raise Exception(
                    "[{} # DataManager # save()] Attributs list not same to excepted.".format(
                        self.cloud_entity_class.__name__,
                    )
                )

            entity["created_at"] = str(datetime.datetime.now())
            entity["updated_at"] = str(datetime.datetime.now())
            datas[entity_id] = entity

            with open(self.cloud_PATH, "w", encoding="utf-8") as file:
                json.dump(datas, file, indent=4)

        return self.get(entity_id)

    def get(self, entity_id: int | str, entity_type=None):
        """
        Logic to retrieve an entity based on ID and type.
        Arguments:
            entity_id (int | str): Entity ID.
            entity_type (str): ???
        Return:
            Entity in the "database" or None if not exist.
        """
        with open(self.cloud_PATH, "r", encoding="utf-8") as file:
            datas: dict = json.load(file)
            data = datas.get(str(entity_id), None)
            if not data:
                return None
            return self.cloud_entity_class(data)

    def update(self, entity: dict):
        """
        Logic to update an entity in storage.
        Arguments:
            entity (dict): Data of the entity to save.
        Return:
            Entity in the "database" updated.
        """
        entity["updated_at"] = str(datetime.datetime.now())

        with open(self.cloud_PATH, 'r', encoding="utf-8") as file:
            datas: dict = json.load(file)
            entity_id = entity.get(self.primary_key, None)
            if entity_id not in datas:
                raise Exception(
                    "[{} # DataManager # update()] ID entity not found.".format(
                        self.cloud_entity_class.__name__,
                    )
                )

            for key, value in entity.items():
                if key != self.cloud_primary_key:
                    datas[entity_id][key] = value

            with open(self.cloud_PATH, "w", encoding="utf-8") as file:
                json.dump(datas, file, indent=4)

        return self.get(entity_id)

    def delete(self, entity_id, entity_type=None) -> None:
        """
        Logic to delete an entity from storage.
        Arguments:
            entity_id (int | str): Entity ID.
            entity_type (str): ???
        """
        with open(self.cloud_PATH, 'r', encoding="utf-8") as file:
            datas: dict = json.load(file)
            if entity_id in datas:
                del datas[entity_id]
                with open(self.cloud_PATH, "w", encoding="utf-8") as file:
                    json.dump(datas, file, indent=4)

    @property
    def cloud_PATH(self):
        return f"data/{self.cloud_database}.json"

