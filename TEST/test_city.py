import unittest
from class_city import city

class TestCity(unittest.TestCase):
    def test_add_place(self):
        # Créer une ville
        city_instance = city("1", "Paris", "FR")  # Utiliser la classe City pour créer une instance de la ville

        # Vérifier que la ville est initialement vide
        self.assertEqual(len(city_instance.places), 0)

        # Ajouter un lieu à la ville
        city_instance.add_place({"name": "Eiffel Tower", "type": "Landmark"})

        # Vérifier que le lieu a été ajouté avec succès
        self.assertEqual(len(city_instance.places), 1)
        self.assertEqual(city_instance.places[0]["name"], "Eiffel Tower")
        self.assertEqual(city_instance.places[0]["type"], "Landmark")

        # Ajouter un deuxième lieu à la ville
        city_instance.add_place({"name": "Louvre Museum", "type": "Museum"})

        # Vérifier que le deuxième lieu a été ajouté avec succès
        self.assertEqual(len(city_instance.places), 2)
        self.assertEqual(city_instance.places[1]["name"], "Louvre Museum")
        self.assertEqual(city_instance.places[1]["type"], "Museum")

if __name__ == '__main__':
    unittest.main()