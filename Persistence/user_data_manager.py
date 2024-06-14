from ipersistence_manager import IPersistenceManager

class UserDataManager(IPersistenceManager):
    def __init__(self):
        self.user = {}

    def save(self, user):
        user_id = user.get_id()
        self.user[user_id] = user
        print(f"Saved User with ID {user_id}")

    def get(self, user_id):
        return self.user.get(user_id, None)

    def update(self, user):
        user_id = user.get_id()
        if user_id in self.user:
            self.user[user_id] = user
            print(f"Updated User with ID {user_id}")
        else:
            print(f"User with ID {user_id} does not exist")

    def delete(self, user_id):
        if user_id in self.user:
            del self.user[user_id]
            print(f"Deleted User with ID {user_id}")
        else:
            print(f"User with ID {user_id} does not exist")