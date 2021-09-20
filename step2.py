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


class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.country = country

    |<--Your cursor should be here
def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")

          
          
# First instantiation of the class Location 
loc1 = Location("Tomas", "Portugal")
# Call a method from the instantiated class
loc1.myLocation()
