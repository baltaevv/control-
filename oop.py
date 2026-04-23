import math
from abc import ABC, abstractmethod

class Person:
    def __init__(self, age=0):
        self.age = age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Ошибка: Возраст не может быть отрицательным!")
        self.age = age

    def get_age(self):
        return self.age

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"

class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move(vehicle):
    return vehicle.move()

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
       self.width = width
       self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


if __name__ == '__main__':
    print("=== 1. Person ===")
    p = Person()
    p.set_age(25)
    print(p.get_age())

    try:
        p.set_age(-5)
    except ValueError as e:
        print(e)

    print("\n=== 2. Animal ===")
    dog = Dog("Moynok")
    cat = Cat("Zevs")
    print(dog.name, dog.speak())
    print(cat.name, cat.speak())

    print("\n=== 3. Полиморфизм ===")
    car = Car()
    bike = Bicycle()
    print(move(car))
    print(move(bike))

    print("\n=== 4. Абстракция ===")
    rect = Rectangle(10, 5)
    circle = Circle(7)
    print(rect.area())
    print(round(circle.area()))