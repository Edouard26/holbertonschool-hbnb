import json
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from class_review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review1 = Review(user_id="user_1", rating=5)

    def test_initialization(self):
        self.assertEqual(self.review1.user_id, "user_1")
        self.assertEqual(self.review1.rating, 5)

    def test_to_dict(self):
        review_dict = self.review1.to_dict()
        self.assertEqual(review_dict['user_id'], "user_1")
        self.assertEqual(review_dict['rating'], 5)

    def test_json_serialization(self):
        review_json = json.dumps(self.review1.to_dict())
        review_dict = json.loads(review_json)
        self.assertEqual(review_dict['user_id'], "user_1")
        self.assertEqual(review_dict['rating'], 5)

if __name__ == "__main__":
    unittest.main()