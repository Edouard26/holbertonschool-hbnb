import json
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from class_country import Country

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country1 = Country(country_code="USA")

    def test_initialization(self):
        self.assertEqual(self.country1.country_code, "USA")

    def test_to_dict(self):
        country_dict = self.country1.to_dict()
        self.assertEqual(country_dict['country_code'], "USA")

    def test_json_serialization(self):
        country_json = json.dumps(self.country1.to_dict())
        country_dict = json.loads(country_json)
        self.assertEqual(country_dict['country_code'], "USA")

if __name__ == "__main__":
    unittest.main()