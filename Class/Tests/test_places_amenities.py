import unittest
from class_amenities import amenities
from class_places import places, Appartment, House, Room

class TestPlacesAmenities(unittest.TestCase):
    
    def setUp(self):
        # Create amenities instances
        self.wifi = amenities(1, "Wi-Fi")
        self.pool = amenities(2, "Swimming Pool")
        
        # Create place instances
        self.appartment = Appartment(50, "40.7128° N, 74.0060° W", 2, 4)
        self.house = House(120, "34.0522° N, 118.2437° W", 4, 8)
        self.room = Room(20, "48.8566° N, 2.3522° E", 2)

    def test_add_amenity(self):
        # Test adding amenities to places
        self.appartment.add_amenity(self.wifi)
        self.house.add_amenity(self.pool)
        self.room.add_amenity(self.wifi)
        
        self.assertIn(self.wifi, self.appartment.amenities)
        self.assertIn(self.pool, self.house.amenities)
        self.assertIn(self.wifi, self.room.amenities)
        
    def test_details(self):
        # Test details method for different places
        self.assertEqual(self.appartment.details(), "Type: appartment\nArea: 50 m²\nGPS coordinates: 40.7128° N, 74.0060° W\nNumber of rooms: 2\nNumber max of guests: 4")
        self.assertEqual(self.house.details(), "Type: house\nArea: 120 m²\nGPS coordinates: 34.0522° N, 118.2437° W\nNumber of rooms: 4\nNumber max of guests: 8")
        self.assertEqual(self.room.details(), "Type: room\nArea: 20 m²\nGPS coordinates: 48.8566° N, 2.3522° E\nNumber of rooms: 1\nNumber max of guests: 2")
        
    def test_relations(self):
        # Test relations between places and amenities
        self.appartment.add_amenity(self.wifi)
        self.appartment.add_amenity(self.pool)
        
        self.assertEqual(len(self.appartment.amenities), 2)
        self.assertIn(self.wifi, self.appartment.amenities)
        self.assertIn(self.pool, self.appartment.amenities)

if __name__ == '__main__':
    unittest.main()

