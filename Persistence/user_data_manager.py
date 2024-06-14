from ipersistence_manager import IPersistenceManager

class UserDataManager(IPersistenceManager):
    def __init__(self):
        self.users = {}

    def save(self, user):
        user_id = user.get_id()
        self.users[user_id] = user
        print(f"Saved User with ID {user_id}")

    def get(self, user_id):
        return self.users.get(user_id, None)

    def update(self, user):
        user_id = user.get_id()
        if user_id in self.users:
            self.users[user_id] = user
            print(f"Updated User with ID {user_id}")
        else:
            print(f"User with ID {user_id} does not exist")

    def delete(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            print(f"Deleted User with ID {user_id}")
        else:
            print(f"User with ID {user_id} does not exist")