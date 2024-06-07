class Users:
    def __init__(self, username, ID, password, email, first_name, last_name, age):
        self.username = username
        self.ID = ID
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

class Customers(Users):
    def __init__(self, username, ID, password, email, first_name, last_name, age, customer_id):
        super().__init__(username, ID, password, email, first_name, last_name, age)
        self.customer_id = customer_id


class Owners(Users):
    def __init__(self, username, ID, password, email, first_name, last_name, age, owner_id):
        super().__init__(username, ID, password, email, first_name, last_name, age)
        self.owner_id = owner_id
