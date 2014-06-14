import os, sys
sys.path.insert(0, os.path.abspath(".."))
import unittest

from planet import Planet

class PlanetTestCase(unittest.TestCase):
    def setUp(self):
        self.planet = Planet('Earth', 6367445, 5515)

    def tearDown(self):
        self.planet = None

    def test_calculate_mass(self):
        planet_mass = self.planet.calculate_mass()
        self.assertTrue(4.47291861801e+24 < planet_mass < 4.47291861803e+24, 'planet mass is wrong, got ' + str(planet_mass))

    def test_calculate_volume(self):
        planet_volume = self.planet.calculate_volume()
        self.assertTrue(8.11045986947e+20 < planet_volume < 8.11045986949e+20, 'planet volume is wrong, got ' + str(planet_volume))

    def test_calculate_object_weight(self):
        object_weight = self.planet.calculate_object_weight(1)
        self.assertTrue(7.35986561504 < object_weight < 7.35986561506, 'object weight is wrong, got ' + str(object_weight))

if __name__ == '__main__':
    unittest.main()
