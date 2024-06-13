import unittest
from CountryManager import CountryManager

class TestCountryManager(unittest.TestCase):

    def setUp(self):
        # Initialisation du CountryManager avant chaque test si nécessaire
        self.manager = CountryManager()

    def tearDown(self):
        # Nettoyage après chaque test si nécessaire
        pass

    def test_create_country(self):
        # Test de la création d'un pays
        country_name = "Test Country"
        created_country = self.manager.createCountry(country_name)
        self.assertEqual(created_country.name, country_name)

    def test_get_country(self):
        # Test de la récupération d'un pays par ID
        country_name = "Test Country"
        created_country = self.manager.createCountry(country_name)
        retrieved_country = self.manager.getCountry(created_country.id)
        self.assertEqual(retrieved_country.name, country_name)

    def test_update_country(self):
        # Test de la mise à jour d'un pays
        country_name = "Test Country"
        updated_country_name = "Updated Test Country"
        created_country = self.manager.createCountry(country_name)
        self.assertTrue(self.manager.updateCountry(created_country.id, name=updated_country_name))
        updated_country = self.manager.getCountry(created_country.id)
        self.assertEqual(updated_country.name, updated_country_name)

    def test_delete_country(self):
        # Test de la suppression d'un pays
        country_name = "Test Country"
        created_country = self.manager.createCountry(country_name)
        self.assertTrue(self.manager.deleteCountry(created_country.id))
        deleted_country = self.manager.getCountry(created_country.id)
        self.assertIsNone(deleted_country)

if __name__ == '__main__':
    unittest.main()
