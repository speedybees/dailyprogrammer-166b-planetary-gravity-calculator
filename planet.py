from math import pi
import re, sys

# gravitational constant, to way too much precision
G = 6.671281903963040991511534289e-11 

class Planet(object):
    def __init__(self, name, radius, density):
        self.name = name
        self.radius = radius
        self.density = density

    def calculate_mass(self):
        return self.calculate_volume() * self.density

    def calculate_volume(self):
        return (4/3) * pi * self.radius ** 3

    def calculate_object_weight(self, object_mass, distance_from_center=None):
        if distance_from_center == None:
            distance_from_center = self.radius
        return G * (self.calculate_mass() * object_mass) / (distance_from_center ** 2)

class MassStore(object):
    def __init__(self, mass, planets):
        self.mass = mass
        self.planets = planets

    @staticmethod
    def parse(file):
        lines = file.readlines()
        if len(lines) < 2:
            raise IOException("Insufficient lines")
        mass = int(lines[0])
        number_of_planets = int(lines[1])
        planets = []
        for line in lines[2:]:
             if (len(planets) >= number_of_planets):
                 break
             try:
                 planets.append(MassStore.parse_planet(line))
             except ValueError:
                 print >> sys.stderr, "Improperly formatted line", line
        return MassStore(mass, planets)

    @staticmethod
    def parse_planet(line):
        match = re.match(r'(.*),\s*([^,]*),\s*(.*)', line)
        name, radius, density = match.group(1), float(match.group(2)), float(match.group(3))
        return Planet(name, radius, density)
