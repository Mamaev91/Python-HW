from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def do_something(self):
        pass


class Bird(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def do_something(self):
        print(f"Bird: {self.name}, age: {self.age} years and it can fly!")


class Dog(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def do_something(self):
        print(f"Dog: {self.name}, age: {self.age} years and it can woof!")


class Fish(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def do_something(self):
        print(f"Fish: {self.name}, age: {self.age} years and it can swim fast!")


class AnimalFactory:

    @staticmethod
    def get_animal(animal_type):
        name = input('Enter name: ')
        age = input("Enter age in years: ")

        if animal_type == 'Bird':
            return Bird(name, age)
        if animal_type == 'Dog':
            return Dog(name, age)
        if animal_type == 'Fish':
            return Fish(name, age)
        print("Invalid animal type")

        return -1


if __name__ == '__main__':
    choice = input("What type of animal do you want to create?\nBird, Dog, Fish\n>>> ")
    animal = AnimalFactory.get_animal(choice)
    animal.do_something()
    print()
    choice = input("What type of animal do you want to create?\nBird, Dog, Fish\n>>> ")
    animal2 = AnimalFactory.get_animal(choice)
    animal2.do_something()
