#! /usr/bin/python

'''
Implementation of the abstract factory pattern
'''

import random

class PetShop:
    '''
    Client
    '''
    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print ("We have a lovely %s" % pet)
        print ("It says %s" % pet.speak())
        print ("We alaso have %s" % self.pet_factory.get_food())


class Dog:
    '''
    Concrete Product
    '''
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"

class Cat:
    '''
    Concrete Product
    '''
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"


class DogFactory:
    '''
    ConcreteFactory
    '''
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"

class CatFactory:
    '''
    ConcreteFactory
    '''
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"

def get_factory():
    return random.choice([DogFactory, CatFactory])()

if __name__ == "__main__":
    for i in range(3):
        shop = PetShop(get_factory())
        show.show_pet()
        print ("-" * 30)
