from .DataManager import DataManager
from ..Model.Users import Users

class usersManager(DataManager):
    """
    Users Manager.
    """
    cloud_database = "users.json"
    cloud_entity_class = Users
    cloud_primary_key = "id"

    def __init__(self):
        self.cloud_PATH = self.cloud_database
        super().__init__()

    def getUser(self, user_id: int) -> (Users | None):
        return self.get(user_id)

    def createUser(self, email: str, password: str, first_name: str, last_name: str) -> Users:
        user_data = {
            "email": email,
            "password": password,
            "first_name": first_name,
            "last_name": last_name
        }
        return self.save(user_data)

    def updateUser(self, user_id: int, email: str = None, password: str = None, first_name: str = None, last_name: str = None) -> bool:
        user = self.getUser(user_id)
        if user is None:
            return False

        if email is not None:
            user.email = email
        if password is not None:
            user.password = password
        if first_name is not None:
            user.first_name = first_name
        if last_name is not None:
            user.last_name = last_name

        self.update(user.__dict__)
        return True

    def deleteUser(self, user_id: int) -> bool:
        return self.delete(user_id)
