from datetime import datetime

class users:
    def __init__(self, username, ID, password, email, first_name, last_name, age):
        self.username = username
        self.ID = ID
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_user(self, username=None, password=None, email=None, first_name=None, last_name=None, age=None):
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if age is not None:
            self.age = age
        self.updated_at = datetime.now()

class customers(users):
    def __init__(self, username, ID, password, email, first_name, last_name, age, customer_id, review):
        super().__init__(username, ID, password, email, first_name, last_name, age)
        self.customer_id = customer_id
        self.review = review

class owners(users):
    def __init__(self, username, ID, password, email, first_name, last_name, age, owner_id):
        super().__init__(username, ID, password, email, first_name, last_name, age)
        self.owner_id = owner_id
