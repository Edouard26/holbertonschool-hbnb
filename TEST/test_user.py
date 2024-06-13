import unittest
from datetime import datetime
import time
from class_user import users, customers, owners

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.user = users("testuser", "1", "password123", "test@example.com", "Test", "User", 25)

    def test_initialization(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.ID, "1")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.first_name, "Test")
        self.assertEqual(self.user.last_name, "User")
        self.assertEqual(self.user.age, 25)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_update_user(self):
        initial_updated_at = self.user.updated_at
        time.sleep(0.01)  # Assure que le temps a passé
        self.user.update_user(username="newuser", email="new@example.com", age=26)
        self.assertEqual(self.user.username, "newuser")
        self.assertEqual(self.user.email, "new@example.com")
        self.assertEqual(self.user.age, 26)
        self.assertGreater(self.user.updated_at, initial_updated_at)

class TestCustomers(unittest.TestCase):
    def setUp(self):
        self.customer = customers("custuser", "2", "custpassword", "cust@example.com", "Cust", "Omer", 30, "123", "Good customer")

    def test_initialization(self):
        self.assertEqual(self.customer.username, "custuser")
        self.assertEqual(self.customer.ID, "2")
        self.assertEqual(self.customer.password, "custpassword")
        self.assertEqual(self.customer.email, "cust@example.com")
        self.assertEqual(self.customer.first_name, "Cust")
        self.assertEqual(self.customer.last_name, "Omer")
        self.assertEqual(self.customer.age, 30)
        self.assertEqual(self.customer.customer_id, "123")
        self.assertEqual(self.customer.review, "Good customer")
        self.assertIsInstance(self.customer.created_at, datetime)
        self.assertIsInstance(self.customer.updated_at, datetime)

class TestOwners(unittest.TestCase):
    def setUp(self):
        self.owner = owners("ownuser", "3", "ownpassword", "own@example.com", "Own", "Er", 35, "456")

    def test_initialization(self):
        self.assertEqual(self.owner.username, "ownuser")
        self.assertEqual(self.owner.ID, "3")
        self.assertEqual(self.owner.password, "ownpassword")
        self.assertEqual(self.owner.email, "own@example.com")
        self.assertEqual(self.owner.first_name, "Own")
        self.assertEqual(self.owner.last_name, "Er")
        self.assertEqual(self.owner.age, 35)
        self.assertEqual(self.owner.owner_id, "456")
        self.assertIsInstance(self.owner.created_at, datetime)
        self.assertIsInstance(self.owner.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()

