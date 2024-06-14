import json
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from class_amenity import Amenity

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity1 = Amenity()

    def test_initialization(self):
        self.assertIsNotNone(self.amenity1.id)

    def test_to_dict(self):
        amenity_dict = self.amenity1.to_dict()
        self.assertIn('id', amenity_dict)

    def test_json_serialization(self):
        amenity_json = json.dumps(self.amenity1.to_dict())
        amenity_dict = json.loads(amenity_json)
        self.assertIn('id', amenity_dict)

if __name__ == "__main__":
    unittest.main()