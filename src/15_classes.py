# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    lat = 0
    lon = 0

    def __init__(self, la, lg):
        self.lat = la
        self.lon = lg 
    def __str__(self): 
        return f"{self.lat} and {self.lon}"
       
    
# creating object of the class 
# this will invoke parameterized constructor 
obj = LatLon(14, -721) 
  
# display result 
print("LatLon:", obj)

        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):

    def __init__(self, name, la, lg):

        super().__init__(la, lg) # taking these params from the above class
        self.name = name

    def __str__(self): 
        return f"{self.name} is at {self.lat} and {self.lon}"

waypoint = Waypoint("Miami", 142, -431) 
print("Waypoint:", waypoint)
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):

    def __init__(self, name, difficulty, size, la, lg):
        super().__init__(name, la, lg) # taking these params from the above class
        self.difficulty = difficulty
        self.size = size
    def __str__(self):
        return f"{self.name} is at {self.lat} and {self.lon} {self.difficulty} {self.size}"

geocache = Geocache("Miami", "4.2", "1", 243, -423)
print("Geogache:", geocache)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
# YOUR CODE HERE
waypoint2 = Waypoint("Catacombs", 41.70505, -121.51521) 
print("Waypoint2:", waypoint2)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
# YOUR CODE HERE
geocache2 = Geocache("Newberry Views", "diff 1.5", "size 2", 44.052137, -121.41556)
print("Geogache2:", geocache2)


# Print it--also make this print more nicely
