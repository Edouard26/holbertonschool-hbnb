import unittest
from class_user import users, customers, owners

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.user = users("username", "ID", "password", "email@example.com", "John", "Doe", 30)
    
    def test_user_attributes(self):
        self.assertEqual(self.user.username, "username")
        self.assertEqual(self.user.ID, "ID")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.email, "email@example.com")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.age, 30)

class TestCustomers(unittest.TestCase):
    def setUp(self):
        self.customer = customers("username", "ID", "password", "email@example.com", "John", "Doe", 30, "customer_id", "review")
    
    def test_customer_attributes(self):
        self.assertEqual(self.customer.username, "username")
        self.assertEqual(self.customer.ID, "ID")
        self.assertEqual(self.customer.password, "password")
        self.assertEqual(self.customer.email, "email@example.com")
        self.assertEqual(self.customer.first_name, "John")
        self.assertEqual(self.customer.last_name, "Doe")
        self.assertEqual(self.customer.age, 30)
        self.assertEqual(self.customer.customer_id, "customer_id")
        self.assertEqual(self.customer.review, "review")

class TestOwners(unittest.TestCase):
    def setUp(self):
        self.owner = owners("username", "ID", "password", "email@example.com", "John", "Doe", 30, "owner_id")
    
    def test_owner_attributes(self):
        self.assertEqual(self.owner.username, "username")
        self.assertEqual(self.owner.ID, "ID")
        self.assertEqual(self.owner.password, "password")
        self.assertEqual(self.owner.email, "email@example.com")
        self.assertEqual(self.owner.first_name, "John")
        self.assertEqual(self.owner.last_name, "Doe")
        self.assertEqual(self.owner.age, 30)
        self.assertEqual(self.owner.owner_id, "owner_id")

if __name__ == '__main__':
    unittest.main()
