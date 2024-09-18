# Single Inheritance
# This is the simplest form of inheritance, where a child class inherits from one parent class.

# Base class (parent)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound."

# Derived class (child)
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Creating an object of the derived class
cat1 = Cat("Whiskers")
print(cat1.speak())  # Output: Whiskers says Meow!

# Multiple Inheritance
# A child class can inherit from more than one parent class. This can lead to complex scenarios but is useful in some cases.

# Parent class 1
class Animal:
    def eat(self):
        return "Animal is eating."

# Parent class 2
class Mammal:
    def breathe(self):
        return "Mammal is breathing."

# Child class inheriting from both Animal and Mammal
class Dog(Animal, Mammal):
    def bark(self):
        return "Dog is barking."

# Creating an object of the child class
dog = Dog()
print(dog.eat())       # Output: Animal is eating.
print(dog.breathe())   # Output: Mammal is breathing.
print(dog.bark())      # Output: Dog is barking.



# Multilevel Inheritance

# In multilevel inheritance, a child class inherits from a parent class, which in turn inherits from another class.

# Base class
class LivingBeing:
    def alive(self):
        return "This being is alive."

# Intermediate class (inherits from LivingBeing)
class Bird(LivingBeing):
    def fly(self):
        return "Bird can fly."

# Derived class (inherits from Bird)
class Parrot(Bird):
    def speak(self):
        return "Parrot can speak."

# Creating an object of the derived class
parrot = Parrot()
print(parrot.alive())  # Output: This being is alive.
print(parrot.fly())    # Output: Bird can fly.
print(parrot.speak())  # Output: Parrot can speak.

# Hierarchical Inheritance
# In this type of inheritance, multiple child classes inherit from a single parent class.

# Parent class
class Shape:
    def __init__(self, color):
        self.color = color

    def describe(self):
        return f"This shape is {self.color}."

# Child class 1
class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius

# Child class 2
class Square(Shape):
    def area(self, side):
        return side * side

# Creating objects of both child classes
circle = Circle("red")
square = Square("blue")

print(circle.describe())   # Output: This shape is red.
print(circle.area(5))      # Output: 78.5
print(square.describe())   # Output: This shape is blue.
print(square.area(4))      # Output: 16


#  Hybrid Inheritance
# Hybrid inheritance is a combination of two or more types of inheritance. Python resolves conflicts in method resolution using something called the Method Resolution Order (MRO).

# Parent class
class A:
    def method_a(self):
        return "Method A"

# Child class 1 (Single Inheritance)
class B(A):
    def method_b(self):
        return "Method B"

# Child class 2 (Multiple Inheritance)
class C(A):
    def method_c(self):
        return "Method C"

# Child class 3 (Hybrid Inheritance)
class D(B, C):
    def method_d(self):
        return "Method D"

# Creating object of class D
d = D()
print(d.method_a())    # Output: Method A
print(d.method_b())    # Output: Method B
print(d.method_c())    # Output: Method C
print(d.method_d())    # Output: Method D

# Checking the Method Resolution Order (MRO)
print(D.__mro__)
