class Person:
    def __init__(self, name, age):
        self.name = name          # Public attribute
        self.__age = age          # Private attribute (can't be accessed directly outside the class)
    
    # Getter method for age
    def get_age(self):
        return self.__age
    
    # Setter method for age
    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Invalid age")

# Creating an object
person1 = Person("Alice", 30)

# Accessing public attribute
print(person1.name)      # Output: Alice

# Accessing private attribute via getter
print(person1.get_age()) # Output: 30

# Setting new age using setter
person1.set_age(35)
print(person1.get_age()) # Output: 35

# Directly accessing private attribute will give an error
# print(person1.__age)   # AttributeError: 'Person' object has no attribute '__age'
