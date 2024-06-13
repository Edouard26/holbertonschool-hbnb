import unittest
from datetime import datetime
from class_cityOK import city

class TestCity(unittest.TestCase):
    def test_city_creation(self):
        created_at = datetime.now()
        updated_at = datetime.now()
        paris = city("Paris", "FR", created_at, updated_at)
        self.assertEqual(paris.name, "Paris")
        self.assertEqual(paris.country_code, "FR")
        self.assertEqual(paris.created_at, created_at)
        self.assertEqual(paris.updated_at, updated_at)

if __name__ == '__main__':
    unittest.main()

