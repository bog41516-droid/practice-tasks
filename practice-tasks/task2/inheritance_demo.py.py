# task2/inheritance_demo.py
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

def demonstrate_polymorphism(animals):
    for animal in animals:
        print(animal.speak())

if __name__ == "__main__":
    animals = [Dog("Buddy"), Cat("Kitty"), Animal("Unknown")]
    demonstrate_polymorphism(animals)