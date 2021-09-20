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
loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")
loc2.myLocation()
loc3.myLocation()
your_loc = Location("Your_Name", "Your_Country")
your_loc.myLocation()


# Define a class with variables for **name** and **country**.
# Then define a method that belongs to the class. The method’s 
# purpose is to print a sentence that uses the variables.
class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")

# First instantiation of the Location class
loc1 = Location("Tomas", "Portugal")
# Call a method from the instantiated class
loc1.myLocation()

# Three more instantiations and method calls for the Location class
loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")
loc2.myLocation()
loc3.myLocation()
your_loc = Location("Your_Name", "Your_Country")
your_loc.myLocation()




# Given a radius value, print the circumference of a circle.
# Formula for a circumference is c = pi * 2 * radius

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
      pi = 3.14
      circumferenceValue = pi * self.radius * 2
      return circumferenceValue

    def printCircumference(self):
      myCircumference = self.circumference()
      print ("Circumference of a circle with a radius of " + str(self.radius) + " is " + str(myCircumference))

# First instantiation of the Circle class.
circle1 = Circle(2)
# Call the printCircumference for the instantiated circle1 class.
circle1.printCircumference()

# Two more instantiations and method calls for the Circle class.
circle2 = Circle(5)
circle2.printCircumference()

circle3 = Circle(7)
circle3.printCircumference()
End of document









