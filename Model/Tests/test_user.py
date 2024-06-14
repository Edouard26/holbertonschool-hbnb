import json
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Class.users import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user1 = User(username="john_doe", password="1234", email="john@example.com",
                          first_name="John", last_name="Doe", age=30)

    def test_initialization(self):
        self.assertEqual(self.user1.username, "john_doe")
        self.assertEqual(self.user1.password, "1234")
        self.assertEqual(self.user1.email, "john@example.com")
        self.assertEqual(self.user1.first_name, "John")
        self.assertEqual(self.user1.last_name, "Doe")
        self.assertEqual(self.user1.age, 30)

    def test_to_dict(self):
        user_dict = self.user1.to_dict()
        self.assertEqual(user_dict['username'], "john_doe")
        self.assertEqual(user_dict['email'], "john@example.com")

    def test_json_serialization(self):
        user_json = json.dumps(self.user1.to_dict())
        user_dict = json.loads(user_json)
        self.assertEqual(user_dict['username'], "john_doe")
        self.assertEqual(user_dict['email'], "john@example.com")

if __name__ == "__main__":
    unittest.main()