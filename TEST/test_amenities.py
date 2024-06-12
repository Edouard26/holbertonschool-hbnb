import unittest
from class_amenities import amenities 

class TestAmenities(unittest.TestCase):
    def test_amenities_creation(self):
        # Test creation of amenities object
        amenity = amenities("1", "WiFi")
        self.assertEqual(amenity.ID, "1")
        self.assertEqual(amenity.name, "WiFi")

if __name__ == '__main__':
    unittest.main()
