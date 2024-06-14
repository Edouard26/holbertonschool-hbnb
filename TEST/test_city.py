import json
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from class_city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city1 = City(city_code="NYC")

    def test_initialization(self):
        self.assertEqual(self.city1.city_code, "NYC")

    def test_to_dict(self):
        city_dict = self.city1.to_dict()
        self.assertEqual(city_dict['city_code'], "NYC")

    def test_json_serialization(self):
        city_json = json.dumps(self.city1.to_dict())
        city_dict = json.loads(city_json)
        self.assertEqual(city_dict['city_code'], "NYC")

if __name__ == "__main__":
    unittest.main()