planets = [
    {'name': 'Mercury', 'type': 'Terrestrial', 'order': 1, 'moons': 0},
    {'name': 'Venus', 'type': 'Terrestrial', 'order': 2, 'moons': 0},
    {'name': 'Earth', 'type': 'Terrestrial', 'order': 3, 'moons': 1},
    {'name': 'Mars', 'type': 'Terrestrial', 'order': 4, 'moons': 2},
    {'name': 'Jupiter', 'type': 'Gas Giant', 'order': 5, 'moons': 95},
    {'name': 'Saturn', 'type': 'Gas Giant', 'order': 6, 'moons': 146},
    {'name': 'Uranus', 'type': 'Ice Giant', 'order': 7, 'moons': 28},
    {'name': 'Neptune', 'type': 'Ice Giant', 'order': 8, 'moons': 16}
]

def query_by_type(planet_type):
    return [p['name'] for p in planets if p['type'].lower() == planet_type.lower()]

def has_moons():
    return [p['name'] for p in planets if p['moons'] > 0]

def get_planet_info(name):
    for p in planets:
        if p['name'].lower() == name.lower():
            return p
    return None

print("Terrestrial Planets:", query_by_type('Terrestrial'))
print("Gas Giants:", query_by_type('Gas Giant'))
print("Planets with Moons:", has_moons())
print("Details of Earth:", get_planet_info('Earth'))
