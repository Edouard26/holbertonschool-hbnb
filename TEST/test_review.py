import unittest
from datetime import datetime
import time
from class_reviews import Review

class MockPlace:
    def __init__(self, name):
        self.name = name
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

class MockUser:
    def __init__(self, name):
        self.name = name
        self.reviews = []

class TestReview(unittest.TestCase):
    def setUp(self):
        self.mock_place = MockPlace("MockPlace")
        self.mock_user = MockUser("MockUser")
        self.review = Review("1", self.mock_place, self.mock_user, 5, "Incredible experience!")

    def test_initialization(self):
        self.assertEqual(self.review.ID, "1")
        self.assertEqual(self.review.place, self.mock_place)
        self.assertEqual(self.review.user, self.mock_user)
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, "Great experience!")
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_update_review(self):
        initial_updated_at = self.review.updated_at
        time.sleep(0.01)
        self.review.update_review(new_rating=4, new_comment="Good experience.")
        self.assertEqual(self.review.rating, 4)
        self.assertEqual(self.review.comment, "Good experience.")
        self.assertGreater(self.review.updated_at, initial_updated_at)

if __name__ == '__main__':
    unittest.main()
