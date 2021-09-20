def myCity(city):
     print("I live in " + city + ".")
myCity("Austin")
myCity("Tokyo")
myCity("Salzburg")

class Location:
    |<-- cursor should now be here
    def __init__(self, name, country):
        self.name = name
        self.country = country

|<-- cursor should now be here
loc = Location("Your_Name", "Your_Country")
print(loc.name)
print(loc.country)
print(type(loc))
