#4.1
class Planet:

  def __init__(self, name, distance_from_sun, planet_type):
    self.name = name
    self.distance_from_sun = distance_from_sun
    self.planet_type = planet_type

  def get_distance_to_earth(self):
    distance_to_earth = abs(self.distance_from_sun - 147000000)
    return {f'distance to earth': distance_to_earth}

mars = Planet('Mars', 228000000, 'Terrestrial')
print(mars.get_distance_to_earth()) # {'distance to earth': 81000000}

# 4.2
class Mercury(Planet):
  
  def __init__(self, name, distance_from_sun, planet_type):
    super().__init__(name, distance_from_sun, planet_type)

  @staticmethod
  def happy_new_year():
    print("On Mercury, a year lasts 88 Earth days!")

mercury = Mercury('Mercury', 58000000, 'Terrestrial') 

print(mercury.name)
print(mercury.distance_from_sun)
print(mercury.planet_type) 
mercury.happy_new_year()
print(mercury.get_distance_to_earth())
