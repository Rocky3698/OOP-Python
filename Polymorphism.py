# Method Overriding

# Parent class
class Animal:
    def speak(self):
        return "The animal makes a sound."

# Child class 1
class Dog(Animal):
    def speak(self):
        return "Dog barks."

# Child class 2
class Cat(Animal):
    def speak(self):
        return "Cat meows."

# Using polymorphism
def animal_sound(animal):
    print(animal.speak())

# Creating instances of different classes
dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Dog barks.
animal_sound(cat)  # Output: Cat meows.


# Method Overloading
# Using Default Arguments:

class MathOperations:
    def add(self, a, b=0, c=0):
        return a + b + c

# Creating an object
math_op = MathOperations()

# Calling the method with different numbers of arguments
print(math_op.add(5))        # Output: 5
print(math_op.add(5, 10))    # Output: 15
print(math_op.add(5, 10, 15)) # Output: 30


# Using Variable-Length Arguments (*args):

class MathOperations:
    def add(self, *args):
        return sum(args)

# Creating an object
math_op = MathOperations()

# Calling the method with different numbers of arguments
print(math_op.add(5))          # Output: 5
print(math_op.add(5, 10))      # Output: 15
print(math_op.add(5, 10, 15))  # Output: 30
