# Defining a class
class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    # Constructor (Initializer) method
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    # Method (behavior of the object)
    def bark(self):
        return f"{self.name} says Woof!"

# Creating objects (instances of the class)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing attributes and methods
print(dog1.name)         # Output: Buddy
print(dog2.age)          # Output: 5
print(dog1.bark())       # Output: Buddy says Woof!
