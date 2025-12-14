**1. Class**

A class is a blueprint or template for creating objects. It defines the attributes (data) and methods (functions) that describe the behavior of its objects.
```Python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
```
---
**2. Object (Instance)**

An object is an instance of a class -- a specific realization of class's structure and behavior.
```Python
my_car = Car("Toyota", "Corolla")  # Object of class car
```
---
**3. Constructor (__init__method)**

A special method automatically called when a new object is created. It initializes the Object's attributes.
```Python
def __init__(self, name, age):
    self.name = name
    self.age = age
```
---
**4. *self* Keyword**

A reference to the current object being created or manipulated. It lets you access instance variables and methods within the class.
```Python
class Example:
    def show(self):
        print(self)  # refers to the current instance.
```
---
**5. Attributes (Fields, Variables)**

Variables that belong to a class or object.
- **Instance attributes** -> specific to each object
- **Class attributes** -> shared by all instances of the class
```Python
class Student:
    school = 'ABC High School' # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute
```
---
**6. Methods**

Functions defined inside a class that describe the behavior of the objects.
- Instance methods -> act on specific objects
- Class methods -> act on the class as a whole
- Static methods -> utility functions inside the class
---
**7. Instance Method**

Takes *self* as first parameter and operates on instance data.
```Python
def greet(self):
    print(f"Hello, my name is {self.name}")
```
---
**8. Class Method**

Declared with *@classmethod*, it takes cls (the class itself) as first argument and can modify class-level data.
```Python
@classmethod
def change_school(self, new_name):
    cls.school = new_name
```
---
**9. Static Method**

Declared with *@staticmethod*. Does not use self or cls. Acts like a regular function inside a class.
```Python
@staticmethod
def add(a,b):
    return a + b
```
---
