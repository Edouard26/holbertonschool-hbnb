class users(basemodel):
    def __init__(self, basemodel, username, password, email, first_name, last_name, age):
        super().__init__(uuid4, name, created_at, updated_at)
        self.basemodel
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.age = age