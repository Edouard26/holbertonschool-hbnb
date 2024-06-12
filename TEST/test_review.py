import unittest
from class_reviews import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        # Crée un objet Review pour les tests
        self.review = Review("1", "place", "user", 5, "Great experience!")

    def test_review_attributes(self):
        # Vérifie que les attributs de l'objet Review sont correctement définis
        self.assertEqual(self.review.ID, "1")
        self.assertEqual(self.review.place, "place")
        self.assertEqual(self.review.user, "user")
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, "Great experience!")

if __name__ == '__main__':
    unittest.main()
